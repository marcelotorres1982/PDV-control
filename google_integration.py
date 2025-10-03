"""
Módulo de integração com Google Drive e Google Sheets
Usa OAuth2 para funcionar com contas pessoais do Google
"""

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import streamlit as st
import pickle
import os
from pathlib import Path
from io import BytesIO
from config import DRIVE_FOLDER_NAME, SHEET_NAME

# Escopos necessários
SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/spreadsheets'
]

class GoogleIntegration:
    """Classe para gerenciar integração com Google Drive e Sheets usando OAuth2"""
    
    def __init__(self):
        self.credentials = None
        self.drive_service = None
        self.sheets_service = None
        self.main_folder_id = None
        self.spreadsheet_id = None
        self.authenticate()
        self._setup_drive_structure()

    def _load_token_from_secrets(self):
        """Carrega token do Streamlit Secrets (para Streamlit Cloud)"""
        try:
            if hasattr(st, 'secrets') and 'google_token_base64' in st.secrets:
                import base64
                token_bytes = base64.b64decode(st.secrets['google_token_base64'])
                self.credentials = pickle.loads(token_bytes)
                st.info("🔐 Token carregado do Streamlit Secrets")
                return True
        except Exception as e:
            st.warning(f"⚠️ Erro ao carregar token dos secrets: {e}")
        return False

    def authenticate(self):
        """Autentica usando OAuth2 (funciona local e no Streamlit Cloud)"""
        try:
            # PRIORIDADE 1: Tenta carregar do Streamlit Secrets (para Streamlit Cloud)
            if self._load_token_from_secrets():
                # Verifica se o token precisa ser renovado
                if self.credentials.expired and self.credentials.refresh_token:
                    try:
                        self.credentials.refresh(Request())
                        st.info("🔄 Token renovado automaticamente")
                    except Exception as e:
                        st.error(f"❌ Erro ao renovar token: {e}")
                        st.info("Gere um novo token localmente e atualize o secret no Streamlit Cloud")
                        st.stop()
                
                # Inicializa os serviços
                self.drive_service = build('drive', 'v3', credentials=self.credentials)
                self.sheets_service = build('sheets', 'v4', credentials=self.credentials)
                st.success("✅ Conectado ao Google Drive e Sheets!")
                return
            
            # PRIORIDADE 2: Se não encontrou nos secrets, tenta carregar token local
            token_path = Path('credentials/token.pickle')
            
            if token_path.exists():
                with open(token_path, 'rb') as token:
                    self.credentials = pickle.load(token)
                st.info("🔐 Token local carregado")
            
            # PRIORIDADE 3: Se não tem credenciais válidas, precisa autenticar
            if not self.credentials or not self.credentials.valid:
                if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                    # Tenta renovar
                    try:
                        self.credentials.refresh(Request())
                        st.info("🔄 Token renovado automaticamente")
                    except Exception as e:
                        st.warning(f"⚠️ Erro ao renovar token: {e}")
                        self.credentials = None
                
                # Se ainda não tem credenciais, precisa autenticar localmente
                if not self.credentials:
                    # Verifica se está no Streamlit Cloud
                    if self._is_streamlit_cloud():
                        st.error("❌ Não foi possível carregar credenciais no Streamlit Cloud!")
                        st.warning("""
                        **Como corrigir:**
                        
                        1. Execute localmente: `streamlit run app.py`
                        2. Complete a autenticação
                        3. Gere o token base64:
                           ```bash
                           base64 credentials/token.pickle
                           ```
                        4. Adicione ao Streamlit Secrets:
                           ```toml
                           google_token_base64 = "COLE_AQUI_O_TOKEN"
                           ```
                        5. Reinicie a aplicação no Streamlit Cloud
                        """)
                        st.stop()
                    
                    # Execução local - verifica se existe credentials.json
                    creds_path = Path('credentials/credentials.json')
                    if not creds_path.exists():
                        st.error("❌ Arquivo credentials/credentials.json não encontrado!")
                        st.info("""
                        **Como obter o credentials.json:**
                        
                        1. Acesse: https://console.cloud.google.com/apis/credentials?project=pdv-control
                        2. Clique em "CREATE CREDENTIALS" → "OAuth client ID"
                        3. Application type: "Desktop app"
                        4. Nome: "PDV Control App"
                        5. Baixe o JSON e salve como `credentials/credentials.json`
                        """)
                        st.stop()
                    
                    # Fluxo de autenticação local
                    flow = InstalledAppFlow.from_client_secrets_file(
                        str(creds_path), 
                        SCOPES
                    )
                    
                    st.info("🔐 Abrindo navegador para autenticação...")
                    self.credentials = flow.run_local_server(port=8080)
                    st.success("✅ Autenticação concluída!")
                    
                    # Salva o token para futuras execuções
                    token_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(token_path, 'wb') as token:
                        pickle.dump(self.credentials, token)
                    st.success("💾 Token salvo com sucesso!")
            
            # Inicializa os serviços
            self.drive_service = build('drive', 'v3', credentials=self.credentials)
            self.sheets_service = build('sheets', 'v4', credentials=self.credentials)
            st.success("✅ Conectado ao Google Drive e Sheets!")
            
        except Exception as e:
            st.error(f"❌ Erro na autenticação: {e}")
            st.info("💡 Tente deletar o arquivo `credentials/token.pickle` e autenticar novamente")
            st.stop()
    
    def _is_streamlit_cloud(self):
        """Detecta se está rodando no Streamlit Cloud"""
        return os.getenv('STREAMLIT_RUNTIME_ENV') == 'cloud' or \
               os.getenv('STREAMLIT_SHARING_MODE') is not None or \
               not os.isatty(0)
    
    def _setup_drive_structure(self):
        """Cria/obtém pasta principal e planilha"""
        try:
            # Pasta principal
            query = f"name='{DRIVE_FOLDER_NAME}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
            results = self.drive_service.files().list(
                q=query, 
                spaces='drive',
                fields='files(id, name)'
            ).execute()
            
            folders = results.get('files', [])
            
            if folders:
                self.main_folder_id = folders[0]['id']
                st.success(f"📁 Pasta '{DRIVE_FOLDER_NAME}' encontrada")
            else:
                folder_metadata = {
                    'name': DRIVE_FOLDER_NAME,
                    'mimeType': 'application/vnd.google-apps.folder'
                }
                folder = self.drive_service.files().create(
                    body=folder_metadata,
                    fields='id'
                ).execute()
                self.main_folder_id = folder.get('id')
                st.success(f"📁 Pasta '{DRIVE_FOLDER_NAME}' criada")
        
        except Exception as e:
            st.error(f"❌ Erro ao configurar pasta: {e}")
            st.stop()
        
        try:
            # Planilha principal
            query = f"name='{SHEET_NAME}' and mimeType='application/vnd.google-apps.spreadsheet' and trashed=false"
            results = self.drive_service.files().list(
                q=query,
                spaces='drive',
                fields='files(id, name)'
            ).execute()
            
            sheets = results.get('files', [])
            
            if sheets:
                self.spreadsheet_id = sheets[0]['id']
                st.success(f"📊 Planilha '{SHEET_NAME}' encontrada")
            else:
                # Cria planilha
                spreadsheet = {
                    'properties': {'title': SHEET_NAME},
                    'sheets': [{
                        'properties': {'title': 'Registros'}
                    }]
                }
                spreadsheet = self.sheets_service.spreadsheets().create(
                    body=spreadsheet,
                    fields='spreadsheetId'
                ).execute()
                self.spreadsheet_id = spreadsheet.get('spreadsheetId')
                
                # Adiciona cabeçalhos
                headers = [['Data', 'Hora', 'Promotor', 'PDV', 'Valor Deslocamento',
                           'Nº Entradas', 'Observações', 'Fotos']]
                self.sheets_service.spreadsheets().values().update(
                    spreadsheetId=self.spreadsheet_id,
                    range='Registros!A1:H1',
                    valueInputOption='RAW',
                    body={'values': headers}
                ).execute()
                
                # Move planilha para pasta principal
                file = self.drive_service.files().get(
                    fileId=self.spreadsheet_id,
                    fields='parents'
                ).execute()
                previous_parents = ",".join(file.get('parents', []))
                self.drive_service.files().update(
                    fileId=self.spreadsheet_id,
                    addParents=self.main_folder_id,
                    removeParents=previous_parents,
                    fields='id, parents'
                ).execute()
                st.success(f"📊 Planilha '{SHEET_NAME}' criada e movida para a pasta")
                
        except Exception as e:
            st.error(f"❌ Erro ao configurar planilha: {e}")
            st.stop()
    
    def _get_or_create_folder(self, folder_path):
        """Cria ou obtém ID de uma pasta no caminho especificado"""
        folders = folder_path.split('/')
        parent_id = self.main_folder_id
        
        for folder_name in folders:
            query = f"name='{folder_name}' and '{parent_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
            results = self.drive_service.files().list(
                q=query,
                spaces='drive',
                fields='files(id, name)'
            ).execute()
            items = results.get('files', [])
            
            if items:
                parent_id = items[0]['id']
            else:
                folder_metadata = {
                    'name': folder_name,
                    'mimeType': 'application/vnd.google-apps.folder',
                    'parents': [parent_id]
                }
                folder = self.drive_service.files().create(
                    body=folder_metadata,
                    fields='id'
                ).execute()
                parent_id = folder.get('id')
                
        return parent_id

    def upload_photo(self, file_data, folder_path, file_name):
        """Faz upload de uma foto para o Google Drive e retorna link público"""
        try:
            folder_id = self._get_or_create_folder(folder_path)
            file_data.seek(0)
            
            media = MediaIoBaseUpload(
                file_data,
                mimetype='image/jpeg',
                resumable=True
            )
            file_metadata = {
                'name': file_name,
                'parents': [folder_id]
            }
            
            file = self.drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id, webViewLink'
            ).execute()
            
            # Adiciona permissão pública (opcional)
            try:
                self.drive_service.permissions().create(
                    fileId=file.get('id'),
                    body={'type': 'anyone', 'role': 'reader'}
                ).execute()
            except Exception as e:
                # Não é crítico se falhar
                pass
            
            return file.get('webViewLink')
            
        except Exception as e:
            st.error(f"❌ Erro ao fazer upload da foto: {e}")
            return None

    def add_to_sheet(self, registro):
        """Adiciona um registro à planilha do Google Sheets"""
        try:
            # Garante que fotos é uma lista e filtra valores None
            fotos = registro.get('fotos', [])
            if fotos:
                fotos = [f for f in fotos if f is not None]
            fotos_links = '\n'.join(fotos) if fotos else ''
            
            values = [[
                str(registro.get('data', '')),
                str(registro.get('hora', '')),
                str(registro.get('promotor', '')),
                str(registro.get('pdv', '')),
                str(registro.get('valor_deslocamento', 0)),
                str(registro.get('num_entradas', 1)),
                str(registro.get('observacoes', '')),
                fotos_links
            ]]
            
            body = {'values': values}
            
            result = self.sheets_service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range='Registros!A:H',
                valueInputOption='RAW',
                body=body
            ).execute()
            
            st.success(f"✅ Registro salvo com sucesso!")
            
            return True
            
        except Exception as e:
            st.error(f"❌ Erro ao adicionar registro à planilha: {e}")
            return False

    def get_spreadsheet_url(self):
        """Retorna URL da planilha"""
        return f"https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}"

    def get_all_records_from_sheet(self):
        """Obtém todos os registros da planilha"""
        try:
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range='Registros!A2:H'
            ).execute()
            
            values = result.get('values', [])
            records = []
            
            for row in values:
                record = {
                    'data': row[0] if len(row) > 0 else '',
                    'hora': row[1] if len(row) > 1 else '',
                    'promotor': row[2] if len(row) > 2 else '',
                    'pdv': row[3] if len(row) > 3 else '',
                    'valor_deslocamento': float(row[4]) if len(row) > 4 and row[4] else 0,
                    'num_entradas': int(row[5]) if len(row) > 5 and row[5] else 1,
                    'observacoes': row[6] if len(row) > 6 else '',
                    'fotos': row[7].split('\n') if len(row) > 7 and row[7] else []
                }
                records.append(record)
                
            return records
            
        except Exception as e:
            st.error(f"❌ Erro ao ler registros da planilha: {e}")
            return []