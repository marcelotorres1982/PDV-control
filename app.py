import streamlit as st
from datetime import datetime
import json
from pathlib import Path
from google_integration import GoogleIntegration
from database import Database
from config import *
import base64
from io import BytesIO

# Carregar configurações
try:
    load_config()
except:
    pass

# Configuração da página
st.set_page_config(
    page_title="PDV Control",
    page_icon="📍",
    layout="wide"
)

# CSS customizado
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        padding: 1rem 0;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #1E88E5;
        padding-bottom: 0.5rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #4CAF50;
        color: white;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #2196F3;
        color: white;
        margin: 1rem 0;
    }
    .warning-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #FF9800;
        color: white;
        margin: 1rem 0;
    }
    .stat-card {
        background-color: #f5f5f5;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1E88E5;
        margin: 0.5rem 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1565C0;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar sessão
if 'db' not in st.session_state:
    st.session_state.db = Database()
if 'google' not in st.session_state:
    st.session_state.google = GoogleIntegration()
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def format_currency(value):
    """Formata valor monetário"""
    return f"{MOEDA} {value:.2f}"

def save_config_to_file():
    """Salva configurações em arquivo JSON"""
    try:
        config_data = {
            'promotores': PROMOTORES,
            'pdvs': PDVS
        }
        
        with open('config_data.json', 'w', encoding='utf-8') as f:
            json.dump(config_data, f, ensure_ascii=False, indent=2)
        
        return True
    except Exception as e:
        st.error(f"Erro ao salvar configurações: {e}")
        return False

def load_config_from_file():
    """Carrega configurações do arquivo JSON"""
    try:
        if Path('config_data.json').exists():
            with open('config_data.json', 'r', encoding='utf-8') as f:
                config_data = json.load(f)
            
            # Atualizar listas globais
            PROMOTORES.clear()
            PROMOTORES.extend(config_data.get('promotores', []))
            PDVS.clear()
            PDVS.extend(config_data.get('pdvs', []))
            
            return True
    except Exception as e:
        st.warning(f"Não foi possível carregar configurações salvas: {e}")
    
    return False

def show_admin_panel():
    """Painel administrativo"""
    st.markdown('<h2 class="sub-header">⚙️ Painel Administrativo</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Links", "👥 Promotores", "📍 PDVs", "🗑️ Duplicados"])
    
    # TAB 1: Links
    with tab1:
        st.subheader("Links Importantes")
        
        col1, col2 = st.columns(2)
        
        with col1:
            try:
                spreadsheet_url = st.session_state.google.get_spreadsheet_url()
                st.markdown(f"""
                ### 📊 Planilha Google Sheets
                
                Acesse a planilha para visualizar todos os registros:
                
                **[Abrir Planilha]({spreadsheet_url})**
                
                ```
                {spreadsheet_url}
                ```
                """)
            except:
                st.warning("Conecte ao Google Drive primeiro")
        
        with col2:
            try:
                drive_url = st.session_state.google.get_drive_folder_url()
                st.markdown(f"""
                ### 📁 Pasta Google Drive
                
                Acesse a pasta com todas as fotos:
                
                **[Abrir Pasta]({drive_url})**
                
                ```
                {drive_url}
                ```
                """)
            except:
                st.warning("Conecte ao Google Drive primeiro")
    
    # TAB 2: Promotores
    with tab2:
        st.subheader("Gerenciar Promotores")
        
        st.markdown("#### ➕ Adicionar Promotor")
        new_promotor = st.text_input("Nome do promotor", key="new_promotor")
        if st.button("Adicionar Promotor"):
            if new_promotor and new_promotor not in PROMOTORES:
                PROMOTORES.append(new_promotor)
                save_config_to_file()
                st.success(f"Promotor '{new_promotor}' adicionado!")
                st.rerun()
            else:
                st.error("Nome inválido ou promotor já existe")
        
        st.divider()
        
        st.markdown("#### ➖ Remover Promotor")
        if len(PROMOTORES) > 0:
            promotor_to_remove = st.selectbox(
                "Selecione o promotor para remover",
                PROMOTORES,
                key="remove_promotor"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🗑️ Remover Promotor", type="primary", use_container_width=True):
                    if promotor_to_remove in PROMOTORES:
                        PROMOTORES.remove(promotor_to_remove)
                        save_config_to_file()
                        st.success(f"Promotor '{promotor_to_remove}' removido!")
                        st.rerun()
        else:
            st.warning("Nenhum promotor cadastrado")
        
        st.divider()
        
        st.markdown("#### 📋 Promotores Cadastrados")
        for idx, promotor in enumerate(PROMOTORES, 1):
            st.write(f"{idx}. {promotor}")
    
    # TAB 3: PDVs
    with tab3:
        st.subheader("Gerenciar PDVs")
        
        st.markdown("#### ➕ Adicionar PDV")
        new_pdv = st.text_input("Nome do PDV", key="new_pdv")
        if st.button("Adicionar PDV"):
            if new_pdv and new_pdv not in PDVS:
                PDVS.append(new_pdv)
                save_config_to_file()
                st.success(f"PDV '{new_pdv}' adicionado!")
                st.rerun()
            else:
                st.error("Nome inválido ou PDV já existe")
        
        st.divider()
        
        st.markdown("#### ➖ Remover PDV")
        if len(PDVS) > 0:
            pdv_to_remove = st.selectbox(
                "Selecione o PDV para remover",
                PDVS,
                key="remove_pdv"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🗑️ Remover PDV", type="primary", use_container_width=True):
                    if pdv_to_remove in PDVS:
                        PDVS.remove(pdv_to_remove)
                        save_config_to_file()
                        st.success(f"PDV '{pdv_to_remove}' removido!")
                        st.rerun()
        else:
            st.warning("Nenhum PDV cadastrado")
        
        st.divider()
        
        st.markdown("#### 📋 PDVs Cadastrados")
        for idx, pdv in enumerate(PDVS, 1):
            st.write(f"{idx}. {pdv}")
    
    # TAB 4: Duplicados
    with tab4:
        st.subheader("Gerenciar Check-ins Duplicados")
        
        if st.button("🔍 Buscar Duplicados", type="primary"):
            with st.spinner("Procurando duplicados..."):
                try:
                    duplicates = st.session_state.google.find_duplicates()
                    
                    if duplicates:
                        st.warning(f"⚠️ Encontrados {len(duplicates)} check-ins duplicados")
                        
                        for idx, dup in enumerate(duplicates, 1):
                            with st.expander(f"Duplicado {idx}: {dup['duplicate']['promotor']} - {dup['duplicate']['pdv']}"):
                                col1, col2 = st.columns(2)
                                
                                with col1:
                                    st.markdown("**Original (manter)**")
                                    st.write(f"Data: {dup['original']['data']}")
                                    st.write(f"Hora: {dup['original']['hora']}")
                                    st.write(f"Linha: {dup['original']['row_number']}")
                                
                                with col2:
                                    st.markdown("**Duplicado**")
                                    st.write(f"Data: {dup['duplicate']['data']}")
                                    st.write(f"Hora: {dup['duplicate']['hora']}")
                                    st.write(f"Linha: {dup['duplicate']['row_number']}")
                                    
                                    if st.button("🗑️ Remover", key=f"remove_dup_{idx}"):
                                        if st.session_state.google.delete_row_from_sheet(dup['duplicate']['row_number']):
                                            st.success("Removido!")
                                            st.rerun()
                    else:
                        st.success("✅ Nenhum duplicado encontrado!")
                except Exception as e:
                    st.error(f"Erro ao buscar duplicados: {e}")

def main():
    # Header
    st.markdown('<h1 class="main-header">📍 PDV Control</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">Sistema de Controle de Promotores em PDV</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/200x80/1E88E5/FFFFFF?text=PDV+Control", width=200)
        st.markdown("---")
        
        # Menu principal
        opcoes_menu = ["📝 Novo Check-in", "📊 Ver Registros", "📸 Galeria de Fotos", "⚙️ Configurações"]
        
        # Adicionar painel admin se autenticado
        if st.session_state.authenticated:
            opcoes_menu.append("🔧 Painel Admin")
        
        menu = st.radio(
            "Menu Principal",
            opcoes_menu,
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Estatísticas rápidas
        st.markdown("### 📈 Estatísticas")
        registros = st.session_state.db.get_all_records()
        st.metric("Total de Visitas", len(registros))
        st.metric("Promotores Ativos", len(set([r['promotor'] for r in registros])))
        
        # Status da conexão Google
        st.markdown("---")
        if st.session_state.authenticated:
            st.success("✅ Google Drive conectado")
        else:
            st.warning("⚠️ Google Drive desconectado")
            if st.button("🔗 Conectar Google"):
                try:
                    st.session_state.google.authenticate()
                    st.session_state.authenticated = True
                    st.success("Conectado com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao conectar: {str(e)}")
    
    # Conteúdo principal
    if menu == "📝 Novo Check-in":
        novo_checkin()
    elif menu == "📊 Ver Registros":
        ver_registros()
    elif menu == "📸 Galeria de Fotos":
        galeria_fotos()
    elif menu == "⚙️ Configurações":
        configuracoes()
    elif menu == "🔧 Painel Admin":
        show_admin_panel()

def novo_checkin():
    """Tela de novo check-in"""
    st.markdown('<h2 class="sub-header">📝 Novo Check-in</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Informações do Promotor")
        
        promotor = st.selectbox(
            "Nome do Promotor",
            options=[""] + PROMOTORES,
            key="promotor_select"
        )
        
        if promotor == "":
            novo_promotor = st.text_input("Ou digite um novo nome:", key="novo_promotor")
            if novo_promotor:
                promotor = novo_promotor
        
        pdv = st.selectbox(
            "PDV",
            options=[""] + PDVS,
            key="pdv_select"
        )
        
        if pdv == "":
            novo_pdv = st.text_input("Ou digite um novo PDV:", key="novo_pdv")
            if novo_pdv:
                pdv = novo_pdv
        
        valor_deslocamento = st.number_input(
            "Valor do Deslocamento",
            min_value=0.0,
            value=VALOR_DESLOCAMENTO_PADRAO,
            step=5.0,
            format="%.2f"
        )
        
        num_entradas = st.number_input(
            "Número de Entradas",
            min_value=1,
            max_value=10,
            value=1,
            step=1
        )
        
        observacoes = st.text_area("Observações (opcional)", height=100)
    
    with col2:
        st.markdown("#### Upload de Fotos")
        st.info("📸 Você pode fazer upload de múltiplas fotos do PDV")
        
        uploaded_files = st.file_uploader(
            "Selecione as fotos",
            type=['png', 'jpg', 'jpeg'],
            accept_multiple_files=True,
            key="foto_upload"
        )
        
        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)} foto(s) selecionada(s)")
            
            st.markdown("##### Preview das Fotos:")
            cols = st.columns(3)
            for idx, file in enumerate(uploaded_files):
                with cols[idx % 3]:
                    st.image(file, caption=file.name, use_container_width=True)
    
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ Confirmar Check-in", key="confirmar_checkin", use_container_width=True):
            if not promotor or not pdv:
                st.error("❌ Preencha todos os campos obrigatórios!")
            else:
                try:
                    data_hora = datetime.now()
                    
                    registro = {
                        'data': data_hora.strftime("%Y-%m-%d"),
                        'hora': data_hora.strftime("%H:%M:%S"),
                        'promotor': promotor,
                        'pdv': pdv,
                        'valor_deslocamento': valor_deslocamento,
                        'num_entradas': num_entradas,
                        'observacoes': observacoes,
                        'fotos': []
                    }
                    
                    if uploaded_files and st.session_state.authenticated:
                        with st.spinner("📤 Fazendo upload das fotos..."):
                            folder_path = f"{promotor}/{data_hora.strftime('%Y-%m-%d')}"
                            foto_links = []
                            
                            for idx, file in enumerate(uploaded_files):
                                file_name = f"{pdv}_{idx+1:03d}.jpg"
                                link = st.session_state.google.upload_photo(
                                    file, 
                                    folder_path, 
                                    file_name
                                )
                                foto_links.append(link)
                            
                            registro['fotos'] = foto_links
                    
                    st.session_state.db.add_record(registro)
                    
                    if st.session_state.authenticated:
                        st.session_state.google.add_to_sheet(registro)
                    
                    st.markdown('<div class="success-box">✅ Check-in registrado com sucesso!</div>', unsafe_allow_html=True)
                    
                    st.markdown("#### 📋 Resumo do Check-in")
                    st.write(f"**Promotor:** {promotor}")
                    st.write(f"**PDV:** {pdv}")
                    st.write(f"**Data/Hora:** {data_hora.strftime('%d/%m/%Y %H:%M')}")
                    st.write(f"**Valor:** {format_currency(valor_deslocamento)}")
                    st.write(f"**Entradas:** {num_entradas}")
                    if uploaded_files:
                        st.write(f"**Fotos:** {len(uploaded_files)} foto(s) enviada(s)")
                    
                except Exception as e:
                    st.error(f"❌ Erro ao registrar check-in: {str(e)}")

def ver_registros():
    """Tela de visualização de registros"""
    st.markdown('<h2 class="sub-header">📊 Registros de Check-in</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filtro_data = st.date_input("Filtrar por Data", value=None)
    
    with col2:
        registros = st.session_state.db.get_all_records()
        promotores_unicos = ["Todos"] + list(set([r['promotor'] for r in registros]))
        filtro_promotor = st.selectbox("Filtrar por Promotor", promotores_unicos)
    
    with col3:
        pdvs_unicos = ["Todos"] + list(set([r['pdv'] for r in registros]))
        filtro_pdv = st.selectbox("Filtrar por PDV", pdvs_unicos)
    
    registros_filtrados = registros.copy()
    
    if filtro_data:
        data_str = filtro_data.strftime("%Y-%m-%d")
        registros_filtrados = [r for r in registros_filtrados if r['data'] == data_str]
    
    if filtro_promotor != "Todos":
        registros_filtrados = [r for r in registros_filtrados if r['promotor'] == filtro_promotor]
    
    if filtro_pdv != "Todos":
        registros_filtrados = [r for r in registros_filtrados if r['pdv'] == filtro_pdv]
    
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="stat-card"><h4>📝 Total de Registros</h4><h2>{}</h2></div>'.format(len(registros_filtrados)), unsafe_allow_html=True)
    
    with col2:
        total_deslocamento = sum([r['valor_deslocamento'] for r in registros_filtrados])
        st.markdown('<div class="stat-card"><h4>💰 Total Deslocamento</h4><h2>{}</h2></div>'.format(format_currency(total_deslocamento)), unsafe_allow_html=True)
    
    with col3:
        total_entradas = sum([r.get('num_entradas', 1) for r in registros_filtrados])
        st.markdown('<div class="stat-card"><h4>🔢 Total Entradas</h4><h2>{}</h2></div>'.format(total_entradas), unsafe_allow_html=True)
    
    with col4:
        total_fotos = sum([len(r.get('fotos', [])) for r in registros_filtrados])
        st.markdown('<div class="stat-card"><h4>📸 Total Fotos</h4><h2>{}</h2></div>'.format(total_fotos), unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📋 Detalhes dos Registros")
    
    if not registros_filtrados:
        st.info("ℹ️ Nenhum registro encontrado com os filtros aplicados.")
    else:
        for idx, registro in enumerate(sorted(registros_filtrados, key=lambda x: f"{x['data']} {x['hora']}", reverse=True)):
            with st.expander(f"📍 {registro['promotor']} - {registro['pdv']} | {registro['data']} {registro['hora']}"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Promotor:** {registro['promotor']}")
                    st.write(f"**PDV:** {registro['pdv']}")
                    st.write(f"**Data:** {registro['data']}")
                    st.write(f"**Hora:** {registro['hora']}")
                    st.write(f"**Valor Deslocamento:** {format_currency(registro['valor_deslocamento'])}")
                    st.write(f"**Número de Entradas:** {registro.get('num_entradas', 1)}")
                    if registro.get('observacoes'):
                        st.write(f"**Observações:** {registro['observacoes']}")
                
                with col2:
                    if registro.get('fotos'):
                        st.write(f"**Fotos:** {len(registro['fotos'])} foto(s)")
                        if st.button(f"Ver Fotos", key=f"ver_fotos_{idx}"):
                            for foto_link in registro['fotos']:
                                st.markdown(f"[📸 Abrir Foto]({foto_link})")

def galeria_fotos():
    """Tela de galeria de fotos"""
    st.markdown('<h2 class="sub-header">📸 Galeria de Fotos</h2>', unsafe_allow_html=True)
    
    registros = st.session_state.db.get_all_records()
    registros_com_fotos = [r for r in registros if r.get('fotos')]
    
    if not registros_com_fotos:
        st.warning("⚠️ Nenhuma foto encontrada.")
        return
    
    for registro in sorted(registros_com_fotos, key=lambda x: f"{x['data']} {x['hora']}", reverse=True):
        st.markdown(f"### 📍 {registro['promotor']} - {registro['pdv']}")
        st.write(f"**Data:** {registro['data']} | **Hora:** {registro['hora']}")
        
        for idx, foto_link in enumerate(registro['fotos']):
            st.markdown(f"[📸 Foto {idx+1}]({foto_link})")
        
        st.markdown("---")

def configuracoes():
    """Tela de configurações"""
    st.markdown('<h2 class="sub-header">⚙️ Configurações</h2>', unsafe_allow_html=True)
    
    if st.session_state.authenticated:
        st.success("✅ Conectado ao Google Drive")
        
        if st.button("🔓 Desconectar"):
            st.session_state.authenticated = False
            st.rerun()
    else:
        st.warning("⚠️ Não conectado ao Google Drive")
        
        if st.button("🔗 Conectar"):
            try:
                st.session_state.google.authenticate()
                st.session_state.authenticated = True
                st.success("✅ Conectado!")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Erro: {str(e)}")

if __name__ == "__main__":
    main()