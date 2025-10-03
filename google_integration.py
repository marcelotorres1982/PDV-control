"""
Módulo de integração com Google Drive e Google Sheets
"""

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload
import pickle
import os
from pathlib import Path
from config import DRIVE_FOLDER_NAME, SHEET_NAME
from io import BytesIO

# Escopos necessários
SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/spreadsheets'
]

class GoogleIntegration:
    """Classe para gerenciar integração com Google Drive e Sheets"""
    
    def __init__(self):
        self.creds = None
        self.drive_service = None
        self.sheets_service = None
        self.main_folder_id = None
        self.spreadsheet_id = None
        
    def authenticate(self):
        """Autentica com Google OAuth"""
        token_path = Path('credentials/token.pickle')
        credentials_path = Path('credentials/credentials.json')
        
        # Carrega credenciais salvas
        if token_path.exists():
            with open(token_path, 'rb') as token:
                self.creds = pickle.load(token)
        
        # Se não há credenciais válidas, faz login
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                if not credentials_path.exists():
                    raise FileNotFoundError(
                        "Arquivo credentials.json não encontrado! "
                        "Coloque-o na pasta credentials/"
                    )
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials/credentials.json', 
                    scopes=SCOPES,
                    redirect_uri='http://localhost:8080/'
                )
                # CORREÇÃO: atribuir a self.creds em vez de creds
                self.creds = flow.run_local_server(port=8080, open_browser=True)
            
            # Salva as credenciais
            token_path.parent.mkdir(exist_ok=True)
            with open(token_path, 'wb') as token:
                pickle.dump(self.creds, token)
        
        # Inicializa os serviços
        self.drive_service = build('drive', 'v3', credentials=self.creds)
        self.sheets_service = build('sheets', 'v4', credentials=self.creds)
        
        # Cria/localiza pasta principal e planilha
        self._setup_drive_structure()
        
    def _setup_drive_structure(self):
        """Configura estrutura de pastas no Drive"""
        # Busca ou cria pasta principal
        query = f"name='{DRIVE_FOLDER_NAME}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        results = self.drive_service.files().list(q=query, fields='files(id, name)').execute()
        folders = results.get('files', [])
        
        if folders:
            self.main_folder_id = folders[0]['id']
        else:
            # Cria pasta principal
            folder_metadata = {
                'name': DRIVE_FOLDER_NAME,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = self.drive_service.files().create(
                body=folder_metadata,
                fields='id'
            ).execute()
            self.main_folder_id = folder.get('id')
        
        # Busca ou cria planilha
        query = f"name='{SHEET_NAME}' and mimeType='application/vnd.google-apps.spreadsheet' and trashed=false"
        results = self.drive_service.files().list(q=query, fields='files(id, name)').execute()
        sheets = results.get('files', [])
        
        if sheets:
            self.spreadsheet_id = sheets[0]['id']
        else:
            # Cria planilha
            spreadsheet = {
                'properties': {'title': SHEET_NAME},
                'sheets': [{
                    'properties': {'title': 'Registros'},
                    'data': [{
                        'startRow': 0,
                        'startColumn': 0,
                        'rowData': [{
                            'values': [
                                {'userEnteredValue': {'stringValue': 'Data'}},
                                {'userEnteredValue': {'stringValue': 'Hora'}},
                                {'userEnteredValue': {'stringValue': 'Promotor'}},
                                {'userEnteredValue': {'stringValue': 'PDV'}},
                                {'userEnteredValue': {'stringValue': 'Valor Deslocamento'}},
                                {'userEnteredValue': {'stringValue': 'Número de Entradas'}},
                                {'userEnteredValue': {'stringValue': 'Observações'}},
                                {'userEnteredValue': {'stringValue': 'Links das Fotos'}}
                            ]
                        }]
                    }]
                }]
            }
            spreadsheet = self.sheets_service.spreadsheets().create(
                body=spreadsheet,
                fields='spreadsheetId'
            ).execute()
            self.spreadsheet_id = spreadsheet.get('spreadsheetId')
            
            # Move planilha para pasta principal
            file = self.drive_service.files().get(
                fileId=self.spreadsheet_id,
                fields='parents'
            ).execute()
            previous_parents = ",".join(file.get('parents'))
            
            self.drive_service.files().update(
                fileId=self.spreadsheet_id,
                addParents=self.main_folder_id,
                removeParents=previous_parents,
                fields='id, parents'
            ).execute()
    
    def _get_or_create_folder(self, folder_path):
        """Cria ou obtém ID de uma pasta no caminho especificado"""
        folders = folder_path.split('/')
        parent_id = self.main_folder_id
        
        for folder_name in folders:
            # Busca pasta
            query = f"name='{folder_name}' and '{parent_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
            results = self.drive_service.files().list(
                q=query,
                fields='files(id, name)'
            ).execute()
            items = results.get('files', [])
            
            if items:
                parent_id = items[0]['id']
            else:
                # Cria pasta
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
        """
        Faz upload de uma foto para o Google Drive
        
        Args:
            file_data: Dados do arquivo (BytesIO ou similar)
            folder_path: Caminho da pasta (ex: "Promotor1/2025-01-15")
            file_name: Nome do arquivo
            
        Returns:
            Link público da foto
        """
        # Cria estrutura de pastas
        folder_id = self._get_or_create_folder(folder_path)
        
        # Prepara arquivo para upload
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        
        # Reseta ponteiro do arquivo
        file_data.seek(0)
        
        # Cria MediaIoBaseUpload
        media = MediaIoBaseUpload(
            file_data,
            mimetype='image/jpeg',
            resumable=True
        )
        
        # Faz upload
        file = self.drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, webViewLink'
        ).execute()
        
        # Torna o arquivo público (opcional)
        try:
            self.drive_service.permissions().create(
                fileId=file.get('id'),
                body={'type': 'anyone', 'role': 'reader'}
            ).execute()
        except:
            pass  # Ignora erro se não conseguir tornar público
        
        return file.get('webViewLink')
    
    def add_to_sheet(self, registro):
        """
        Adiciona um registro à planilha do Google Sheets
        
        Args:
            registro: Dicionário com os dados do registro
        """
        # Formata links das fotos
        fotos_links = '\n'.join(registro.get('fotos', []))
        
        # Prepara linha de dados
        values = [[
            registro.get('data', ''),
            registro.get('hora', ''),
            registro.get('promotor', ''),
            registro.get('pdv', ''),
            registro.get('valor_deslocamento', 0),
            registro.get('num_entradas', 1),
            registro.get('observacoes', ''),
            fotos_links
        ]]
        
        body = {'values': values}
        
        # Adiciona à planilha
        self.sheets_service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id,
            range='Registros!A:H',
            valueInputOption='RAW',
            body=body
        ).execute()
    
    def get_spreadsheet_url(self):
        """Retorna URL da planilha"""
        return f"https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}"
    
    def get_all_records_from_sheet(self):
        """Obtém todos os registros da planilha"""
        result = self.sheets_service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range='Registros!A2:H'
        ).execute()
        
        values = result.get('values', [])
        
        records = []
        for row in values:
            if len(row) >= 5:  # Pelo menos os campos obrigatórios
                record = {
                    'data': row[0] if len(row) > 0 else '',
                    'hora': row[1] if len(row) > 1 else '',
                    'promotor': row[2] if len(row) > 2 else '',
                    'pdv': row[3] if len(row) > 3 else '',
                    'valor_deslocamento': float(row[4]) if len(row) > 4 else 0,
                    'num_entradas': int(row[5]) if len(row) > 5 else 1,
                    'observacoes': row[6] if len(row) > 6 else '',
                    'fotos': row[7].split('\n') if len(row) > 7 and row[7] else []
                }
                records.append(record)
        
        return records