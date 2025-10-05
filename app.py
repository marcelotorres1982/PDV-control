import streamlit as st
from datetime import datetime
import json
from pathlib import Path
from google_integration import GoogleIntegration
from database import Database
from config import *
import base64
from io import BytesIO

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

def main():
    # Header
    st.markdown('<h1 class="main-header">📍 PDV Control</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">Sistema de Controle de Promotores em PDV</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/200x80/1E88E5/FFFFFF?text=PDV+Control", width=200)
        st.markdown("---")
        
        menu = st.radio(
            "Menu Principal",
            ["📝 Novo Check-in", "📊 Ver Registros", "📸 Galeria de Fotos", "⚙️ Configurações"],
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

def novo_checkin():
    """Tela de novo check-in"""
    st.markdown('<h2 class="sub-header">📝 Novo Check-in</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Informações do Promotor")
        
        # Nome do promotor
        promotor = st.selectbox(
            "Nome do Promotor",
            options=[""] + PROMOTORES,
            key="promotor_select"
        )
        
        if promotor == "":
            novo_promotor = st.text_input("Ou digite um novo nome:", key="novo_promotor")
            if novo_promotor:
                promotor = novo_promotor
        
        # PDV
        pdv = st.selectbox(
            "PDV",
            options=[""] + PDVS,
            key="pdv_select"
        )
        
        if pdv == "":
            novo_pdv = st.text_input("Ou digite um novo PDV:", key="novo_pdv")
            if novo_pdv:
                pdv = novo_pdv
        
        # Valor do deslocamento
        valor_deslocamento = st.number_input(
            "Valor do Deslocamento",
            min_value=0.0,
            value=VALOR_DESLOCAMENTO_PADRAO,
            step=5.0,
            format="%.2f"
        )
        
        # Número de entradas
        num_entradas = st.number_input(
            "Número de Entradas",
            min_value=1,
            max_value=10,
            value=1,
            step=1
        )
        
        # Observações
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
            
            # Preview das fotos
            st.markdown("##### Preview das Fotos:")
            cols = st.columns(3)
            for idx, file in enumerate(uploaded_files):
                with cols[idx % 3]:
                    st.image(file, caption=file.name, use_container_width=True)
    
    # Botão de confirmação
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ Confirmar Check-in", key="confirmar_checkin", use_container_width=True):
            if not promotor or not pdv:
                st.error("❌ Preencha todos os campos obrigatórios!")
            else:
                try:
                    # Criar registro
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
                    
                    # Upload das fotos para o Google Drive
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
                    
                    # Salvar no banco local
                    st.session_state.db.add_record(registro)
                    
                    # Sincronizar com Google Sheets
                    if st.session_state.authenticated:
                        st.session_state.google.add_to_sheet(registro)
                    
                    st.markdown('<div class="success-box">✅ Check-in registrado com sucesso!</div>', unsafe_allow_html=True)
                    
                    # Mostrar resumo
                    st.markdown("#### 📋 Resumo do Check-in")
                    st.write(f"**Promotor:** {promotor}")
                    st.write(f"**PDV:** {pdv}")
                    st.write(f"**Data/Hora:** {data_hora.strftime('%d/%m/%Y %H:%M')}")
                    st.write(f"**Valor:** {format_currency(valor_deslocamento)}")
                    st.write(f"**Entradas:** {num_entradas}")
                    if uploaded_files:
                        st.write(f"**Fotos:** {len(uploaded_files)} foto(s) enviada(s)")
                    
                    # Limpar formulário
                    st.session_state.pop('promotor_select', None)
                    st.session_state.pop('pdv_select', None)
                    
                except Exception as e:
                    st.error(f"❌ Erro ao registrar check-in: {str(e)}")

def ver_registros():
    """Tela de visualização de registros"""
    st.markdown('<h2 class="sub-header">📊 Registros de Check-in</h2>', unsafe_allow_html=True)
    
    # Filtros
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
    
    # Aplicar filtros
    registros_filtrados = registros.copy()
    
    if filtro_data:
        data_str = filtro_data.strftime("%Y-%m-%d")
        registros_filtrados = [r for r in registros_filtrados if r['data'] == data_str]
    
    if filtro_promotor != "Todos":
        registros_filtrados = [r for r in registros_filtrados if r['promotor'] == filtro_promotor]
    
    if filtro_pdv != "Todos":
        registros_filtrados = [r for r in registros_filtrados if r['pdv'] == filtro_pdv]
    
    # Estatísticas dos filtros
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
    
    # Tabela de registros
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
                            st.write("Links das fotos:")
                            for foto_link in registro['fotos']:
                                st.markdown(f"[📸 Abrir Foto]({foto_link})")
                    else:
                        st.write("**Fotos:** Nenhuma foto")

def galeria_fotos():
    """Tela de galeria de fotos"""
    st.markdown('<h2 class="sub-header">📸 Galeria de Fotos</h2>', unsafe_allow_html=True)
    
    st.info("🔗 Esta seção mostra os links das fotos armazenadas no Google Drive")
    
    registros = st.session_state.db.get_all_records()
    registros_com_fotos = [r for r in registros if r.get('fotos')]
    
    if not registros_com_fotos:
        st.warning("⚠️ Nenhuma foto encontrada nos registros.")
        return
    
    # Filtros
    col1, col2 = st.columns(2)
    
    with col1:
        promotores_unicos = ["Todos"] + list(set([r['promotor'] for r in registros_com_fotos]))
        filtro_promotor = st.selectbox("Filtrar por Promotor", promotores_unicos, key="galeria_promotor")
    
    with col2:
        datas_unicas = ["Todas"] + list(set([r['data'] for r in registros_com_fotos]))
        filtro_data = st.selectbox("Filtrar por Data", datas_unicas, key="galeria_data")
    
    # Aplicar filtros
    registros_filtrados = registros_com_fotos.copy()
    
    if filtro_promotor != "Todos":
        registros_filtrados = [r for r in registros_filtrados if r['promotor'] == filtro_promotor]
    
    if filtro_data != "Todas":
        registros_filtrados = [r for r in registros_filtrados if r['data'] == filtro_data]
    
    # Exibir fotos
    st.markdown("---")
    
    for registro in sorted(registros_filtrados, key=lambda x: f"{x['data']} {x['hora']}", reverse=True):
        st.markdown(f"### 📍 {registro['promotor']} - {registro['pdv']}")
        st.write(f"**Data:** {registro['data']} | **Hora:** {registro['hora']}")
        
        for idx, foto_link in enumerate(registro['fotos']):
            st.markdown(f"[📸 Foto {idx+1}]({foto_link})")
        
        st.markdown("---")

def configuracoes():
    """Tela de configurações"""
    st.markdown('<h2 class="sub-header">⚙️ Configurações</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["👥 Promotores", "🏪 PDVs", "🔗 Google Drive"])
    
    with tab1:
        st.markdown("#### Gerenciar Promotores")
        
        # Listar promotores
        st.write("**Promotores cadastrados:**")
        for promotor in PROMOTORES:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"• {promotor}")
        
        st.markdown("---")
        
        # Adicionar novo promotor
        st.markdown("##### Adicionar Novo Promotor")
        novo_promotor = st.text_input("Nome do Promotor", key="add_promotor")
        if st.button("➕ Adicionar Promotor"):
            if novo_promotor:
                st.success(f"✅ Promotor '{novo_promotor}' adicionado com sucesso!")
                st.info("💡 Edite o arquivo config.py para salvar permanentemente")
            else:
                st.error("❌ Digite um nome para o promotor")
    
    with tab2:
        st.markdown("#### Gerenciar PDVs")
        
        # Listar PDVs
        st.write("**PDVs cadastrados:**")
        for pdv in PDVS:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"• {pdv}")
        
        st.markdown("---")
        
        # Adicionar novo PDV
        st.markdown("##### Adicionar Novo PDV")
        novo_pdv = st.text_input("Nome do PDV", key="add_pdv")
        if st.button("➕ Adicionar PDV"):
            if novo_pdv:
                st.success(f"✅ PDV '{novo_pdv}' adicionado com sucesso!")
                st.info("💡 Edite o arquivo config.py para salvar permanentemente")
            else:
                st.error("❌ Digite um nome para o PDV")
    
    with tab3:
        st.markdown("#### Configurações do Google Drive")
        
        if st.session_state.authenticated:
            st.success("✅ Conectado ao Google Drive")
            
            st.markdown("##### Informações da Conexão")
            st.write(f"**Pasta no Drive:** {DRIVE_FOLDER_NAME}")
            st.write(f"**Planilha:** {SHEET_NAME}")
            
            st.markdown("---")
            
            if st.button("🔄 Sincronizar Dados"):
                with st.spinner("Sincronizando..."):
                    try:
                        registros = st.session_state.db.get_all_records()
                        for registro in registros:
                            st.session_state.google.add_to_sheet(registro)
                        st.success("✅ Dados sincronizados com sucesso!")
                    except Exception as e:
                        st.error(f"❌ Erro na sincronização: {str(e)}")
            
            if st.button("🔓 Desconectar"):
                st.session_state.authenticated = False
                st.success("Desconectado com sucesso!")
                st.rerun()
        
        else:
            st.warning("⚠️ Não conectado ao Google Drive")
            
            st.markdown("##### Como Configurar")
            st.markdown("""
            1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
            2. Crie um novo projeto
            3. Ative as APIs:
               - Google Drive API
               - Google Sheets API
            4. Crie credenciais OAuth 2.0
            5. Baixe o arquivo `credentials.json`
            6. Coloque na pasta `credentials/`
            """)
            
            if st.button("🔗 Conectar ao Google Drive"):
                try:
                    st.session_state.google.authenticate()
                    st.session_state.authenticated = True
                    st.success("✅ Conectado com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Erro ao conectar: {str(e)}")
                    st.info("💡 Certifique-se de que o arquivo credentials.json está na pasta credentials/")

if __name__ == "__main__":
    main()