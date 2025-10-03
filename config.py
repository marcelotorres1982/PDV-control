"""
Arquivo de configurações do sistema PDV Control
"""

# ==========================================
# CONFIGURAÇÕES GERAIS
# ==========================================

APP_NAME = "PDV Control"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Sistema de Controle de Promotores em PDV"

# ==========================================
# PROMOTORES
# ==========================================

PROMOTORES = [
    "João Silva",
    "Maria Santos",
    "Pedro Oliveira",
    "Ana Costa",
    "Carlos Mendes"
]

# ==========================================
# PONTOS DE VENDA (PDVs)
# ==========================================

PDVS = [
    "Supermercado Central",
    "Supermercado Zona Sul",
    "Supermercado Zona Norte",
    "Farmácia São João",
    "Farmácia Popular",
    "Drogaria Preço Bom",
    "Loja de Conveniência 24h",
    "Minimercado Bairro Alto",
    "Mercadinho da Esquina",
    "Atacadão Família"
]

# ==========================================
# VALORES E MOEDA
# ==========================================

VALOR_DESLOCAMENTO_PADRAO = 50.00
MOEDA = "R$"

# Faixas de valores para relatórios
FAIXAS_VALOR = [
    (0, 50, "Até R$ 50"),
    (50, 100, "R$ 50 - R$ 100"),
    (100, 150, "R$ 100 - R$ 150"),
    (150, float('inf'), "Acima de R$ 150")
]

# ==========================================
# GOOGLE DRIVE E SHEETS
# ==========================================

# Nome da pasta principal no Google Drive
DRIVE_FOLDER_NAME = "PDV Control"

# Nome da planilha do Google Sheets
SHEET_NAME = "Registros PDV"

# Formato de data para organização de pastas
DATE_FOLDER_FORMAT = "%Y-%m-%d"

# Formato de nome de arquivo para fotos
PHOTO_NAME_FORMAT = "{pdv}_{index:03d}.jpg"

# ==========================================
# CONFIGURAÇÕES DE UPLOAD
# ==========================================

# Tipos de arquivo permitidos para upload
ALLOWED_IMAGE_TYPES = ['png', 'jpg', 'jpeg']

# Tamanho máximo de arquivo (em MB)
MAX_FILE_SIZE_MB = 10

# Número máximo de fotos por check-in
MAX_PHOTOS_PER_CHECKIN = 20

# ==========================================
# CONFIGURAÇÕES DE HORÁRIO
# ==========================================

# Formato de exibição de data
DATE_FORMAT = "%d/%m/%Y"

# Formato de exibição de hora
TIME_FORMAT = "%H:%M:%S"

# Formato de exibição de data/hora completo
DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"

# ==========================================
# CONFIGURAÇÕES DE BANCO DE DADOS
# ==========================================

# Caminho do banco de dados local
DATABASE_PATH = "data/local_backup.json"

# Caminho para backups automáticos
BACKUP_PATH = "data/backups"

# Frequência de backup automático (em dias)
AUTO_BACKUP_DAYS = 7

# ==========================================
# CONFIGURAÇÕES DE RELATÓRIOS
# ==========================================

# Tipos de relatório disponíveis
REPORT_TYPES = [
    "Diário",
    "Semanal",
    "Mensal",
    "Customizado"
]

# Formatos de exportação
EXPORT_FORMATS = [
    "CSV",
    "Excel",
    "PDF",
    "JSON"
]

# ==========================================
# CONFIGURAÇÕES DE INTERFACE
# ==========================================

# Cores do tema
THEME_COLORS = {
    'primary': '#1E88E5',
    'secondary': '#424242',
    'success': '#4CAF50',
    'warning': '#FF9800',
    'error': '#F44336',
    'info': '#2196F3'
}

# Ícones por categoria
ICONS = {
    'checkin': '📝',
    'registros': '📊',
    'fotos': '📸',
    'config': '⚙️',
    'promotor': '👤',
    'pdv': '🏪',
    'dinheiro': '💰',
    'calendario': '📅',
    'relogio': '🕐',
    'camera': '📷',
    'drive': '☁️',
    'sheets': '📊',
    'sucesso': '✅',
    'erro': '❌',
    'aviso': '⚠️',
    'info': 'ℹ️'
}

# ==========================================
# MENSAGENS DO SISTEMA
# ==========================================

MESSAGES = {
    'checkin_success': '✅ Check-in registrado com sucesso!',
    'checkin_error': '❌ Erro ao registrar check-in',
    'upload_success': '✅ Fotos enviadas com sucesso!',
    'upload_error': '❌ Erro ao enviar fotos',
    'sync_success': '✅ Dados sincronizados com Google Sheets',
    'sync_error': '❌ Erro ao sincronizar com Google Sheets',
    'connection_success': '✅ Conectado ao Google Drive',
    'connection_error': '❌ Erro ao conectar com Google Drive',
    'validation_error': '❌ Preencha todos os campos obrigatórios',
    'no_records': 'ℹ️ Nenhum registro encontrado',
    'no_photos': 'ℹ️ Nenhuma foto disponível'
}

# ==========================================
# VALIDAÇÕES
# ==========================================

# Tamanho mínimo do nome do promotor
MIN_NAME_LENGTH = 3

# Tamanho máximo do nome do promotor
MAX_NAME_LENGTH = 50

# Valor mínimo de deslocamento
MIN_DESLOCAMENTO_VALUE = 0.0

# Valor máximo de deslocamento
MAX_DESLOCAMENTO_VALUE = 999.99

# Número mínimo de entradas
MIN_ENTRADAS = 1

# Número máximo de entradas
MAX_ENTRADAS = 10

# ==========================================
# CONFIGURAÇÕES AVANÇADAS
# ==========================================

# Habilitar modo debug
DEBUG_MODE = False

# Habilitar logs detalhados
VERBOSE_LOGGING = False

# Timeout para operações de rede (segundos)
NETWORK_TIMEOUT = 30

# Tentativas de retry em caso de falha
MAX_RETRY_ATTEMPTS = 3

# Intervalo entre tentativas (segundos)
RETRY_DELAY = 5

# Habilitar cache local
ENABLE_LOCAL_CACHE = True

# Tempo de validade do cache (minutos)
CACHE_VALIDITY_MINUTES = 30

# ==========================================
# PERMISSÕES E SEGURANÇA
# ==========================================

# Requer autenticação Google
REQUIRE_GOOGLE_AUTH = True

# Permitir modo offline
ALLOW_OFFLINE_MODE = True

# Criptografar dados sensíveis
ENCRYPT_SENSITIVE_DATA = False

# ==========================================
# NOTIFICAÇÕES
# ==========================================

# Habilitar notificações
ENABLE_NOTIFICATIONS = True

# Tipos de notificação
NOTIFICATION_TYPES = {
    'checkin': True,
    'sync': True,
    'error': True,
    'backup': False
}

# ==========================================
# FUNCIONALIDADES EXPERIMENTAIS
# ==========================================

# Habilitar geolocalização
ENABLE_GEOLOCATION = False

# Habilitar reconhecimento de imagem
ENABLE_IMAGE_RECOGNITION = False

# Habilitar analytics
ENABLE_ANALYTICS = False

# ==========================================
# INFORMAÇÕES DO DESENVOLVEDOR
# ==========================================

DEVELOPER_INFO = {
    'name': 'Marcelo Torres',
    'email': 'marcelotorres1982@gmail.com',
    'github': 'https://github.com/marcelotorres1982',
    'linkedin': 'https://www.linkedin.com/in/marcelo-t-554b8045/'
}

# ==========================================
# LINKS ÚTEIS
# ==========================================

USEFUL_LINKS = {
    'documentation': 'https://github.com/marcelotorres1982/pdv-control',
    'support': 'https://github.com/marcelotorres1982/pdv-control/issues',
    'google_console': 'https://console.cloud.google.com/',
    'streamlit_docs': 'https://docs.streamlit.io/'
}