"""
Módulo de funções utilitárias
"""

from datetime import datetime, timedelta
from pathlib import Path
import re
from config import *

def format_currency(value):
    """
    Formata valor monetário
    
    Args:
        value: Valor numérico
        
    Returns:
        String formatada
    """
    return f"{MOEDA} {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def format_date(date_obj):
    """
    Formata data para exibição
    
    Args:
        date_obj: Objeto datetime ou string ISO
        
    Returns:
        String formatada
    """
    if isinstance(date_obj, str):
        date_obj = datetime.fromisoformat(date_obj)
    return date_obj.strftime(DATE_FORMAT)

def format_time(time_obj):
    """
    Formata hora para exibição
    
    Args:
        time_obj: Objeto datetime ou string
        
    Returns:
        String formatada
    """
    if isinstance(time_obj, str):
        if 'T' in time_obj:
            time_obj = datetime.fromisoformat(time_obj)
        else:
            return time_obj
    return time_obj.strftime(TIME_FORMAT)

def format_datetime(datetime_obj):
    """
    Formata data/hora completo
    
    Args:
        datetime_obj: Objeto datetime ou string ISO
        
    Returns:
        String formatada
    """
    if isinstance(datetime_obj, str):
        datetime_obj = datetime.fromisoformat(datetime_obj)
    return datetime_obj.strftime(DATETIME_FORMAT)

def validate_promotor_name(name):
    """
    Valida nome do promotor
    
    Args:
        name: Nome a validar
        
    Returns:
        Tupla (válido, mensagem_erro)
    """
    if not name or not name.strip():
        return False, "Nome não pode estar vazio"
    
    if len(name) < MIN_NAME_LENGTH:
        return False, f"Nome deve ter no mínimo {MIN_NAME_LENGTH} caracteres"
    
    if len(name) > MAX_NAME_LENGTH:
        return False, f"Nome deve ter no máximo {MAX_NAME_LENGTH} caracteres"
    
    # Verifica se contém apenas letras, espaços e caracteres acentuados
    if not re.match(r'^[a-zA-ZÀ-ÿ\s]+$', name):
        return False, "Nome deve conter apenas letras"
    
    return True, ""

def validate_pdv_name(name):
    """
    Valida nome do PDV
    
    Args:
        name: Nome a validar
        
    Returns:
        Tupla (válido, mensagem_erro)
    """
    if not name or not name.strip():
        return False, "Nome do PDV não pode estar vazio"
    
    if len(name) < MIN_NAME_LENGTH:
        return False, f"Nome deve ter no mínimo {MIN_NAME_LENGTH} caracteres"
    
    if len(name) > MAX_NAME_LENGTH:
        return False, f"Nome deve ter no máximo {MAX_NAME_LENGTH} caracteres"
    
    return True, ""

def validate_valor_deslocamento(valor):
    """
    Valida valor de deslocamento
    
    Args:
        valor: Valor a validar
        
    Returns:
        Tupla (válido, mensagem_erro)
    """
    try:
        valor = float(valor)
    except (ValueError, TypeError):
        return False, "Valor inválido"
    
    if valor < MIN_DESLOCAMENTO_VALUE:
        return False, f"Valor mínimo é {format_currency(MIN_DESLOCAMENTO_VALUE)}"
    
    if valor > MAX_DESLOCAMENTO_VALUE:
        return False, f"Valor máximo é {format_currency(MAX_DESLOCAMENTO_VALUE)}"
    
    return True, ""

def validate_num_entradas(num):
    """
    Valida número de entradas
    
    Args:
        num: Número a validar
        
    Returns:
        Tupla (válido, mensagem_erro)
    """
    try:
        num = int(num)
    except (ValueError, TypeError):
        return False, "Número inválido"
    
    if num < MIN_ENTRADAS:
        return False, f"Mínimo de {MIN_ENTRADAS} entrada(s)"
    
    if num > MAX_ENTRADAS:
        return False, f"Máximo de {MAX_ENTRADAS} entradas"
    
    return True, ""

def validate_image_file(file, max_size_mb=MAX_FILE_SIZE_MB):
    """
    Valida arquivo de imagem
    
    Args:
        file: Objeto do arquivo
        max_size_mb: Tamanho máximo em MB
        
    Returns:
        Tupla (válido, mensagem_erro)
    """
    if not file:
        return False, "Arquivo inválido"
    
    # Verifica extensão
    ext = file.name.split('.')[-1].lower()
    if ext not in ALLOWED_IMAGE_TYPES:
        return False, f"Tipo de arquivo não permitido. Use: {', '.join(ALLOWED_IMAGE_TYPES)}"
    
    # Verifica tamanho
    file.seek(0, 2)  # Vai para o final do arquivo
    size_mb = file.tell() / (1024 * 1024)
    file.seek(0)  # Volta para o início
    
    if size_mb > max_size_mb:
        return False, f"Arquivo muito grande. Máximo: {max_size_mb}MB"
    
    return True, ""

def get_date_range(period_type, custom_start=None, custom_end=None):
    """
    Retorna intervalo de datas baseado no tipo de período
    
    Args:
        period_type: "Diário", "Semanal", "Mensal" ou "Customizado"
        custom_start: Data inicial para período customizado
        custom_end: Data final para período customizado
        
    Returns:
        Tupla (data_inicial, data_final)
    """
    today = datetime.now().date()
    
    if period_type == "Diário":
        return today, today
    
    elif period_type == "Semanal":
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        return start, end
    
    elif period_type == "Mensal":
        start = today.replace(day=1)
        if today.month == 12:
            end = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            end = today.replace(month=today.month + 1, day=1) - timedelta(days=1)
        return start, end
    
    elif period_type == "Customizado":
        if custom_start and custom_end:
            return custom_start, custom_end
        return today, today
    
    return today, today

def calculate_statistics(registros):
    """
    Calcula estatísticas dos registros
    
    Args:
        registros: Lista de registros
        
    Returns:
        Dicionário com estatísticas
    """
    if not registros:
        return {
            'total_registros': 0,
            'total_deslocamento': 0,
            'total_entradas': 0,
            'total_fotos': 0,
            'media_deslocamento': 0,
            'media_entradas': 0,
            'media_fotos': 0
        }
    
    total_registros = len(registros)
    total_deslocamento = sum(r.get('valor_deslocamento', 0) for r in registros)
    total_entradas = sum(r.get('num_entradas', 1) for r in registros)
    total_fotos = sum(len(r.get('fotos', [])) for r in registros)
    
    return {
        'total_registros': total_registros,
        'total_deslocamento': total_deslocamento,
        'total_entradas': total_entradas,
        'total_fotos': total_fotos,
        'media_deslocamento': total_deslocamento / total_registros if total_registros > 0 else 0,
        'media_entradas': total_entradas / total_registros if total_registros > 0 else 0,
        'media_fotos': total_fotos / total_registros if total_registros > 0 else 0
    }

def generate_photo_filename(pdv, index):
    """
    Gera nome de arquivo para foto
    
    Args:
        pdv: Nome do PDV
        index: Índice da foto
        
    Returns:
        Nome do arquivo
    """
    # Remove caracteres especiais do nome do PDV
    pdv_clean = re.sub(r'[^a-zA-Z0-9]', '_', pdv)
    return PHOTO_NAME_FORMAT.format(pdv=pdv_clean, index=index)

def generate_folder_path(promotor, date):
    """
    Gera caminho da pasta para organização
    
    Args:
        promotor: Nome do promotor
        date: Data (string ou datetime)
        
    Returns:
        Caminho da pasta
    """
    if isinstance(date, str):
        date_str = date
    else:
        date_str = date.strftime(DATE_FOLDER_FORMAT)
    
    # Remove caracteres especiais do nome
    promotor_clean = re.sub(r'[^a-zA-Z0-9]', '_', promotor)
    
    return f"{promotor_clean}/{date_str}"

def parse_date_string(date_str):
    """
    Converte string de data para objeto datetime
    
    Args:
        date_str: String da data (vários formatos aceitos)
        
    Returns:
        Objeto datetime ou None
    """
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%Y/%m/%d",
        "%d-%m-%Y"
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    return None

def get_week_number(date):
    """
    Retorna número da semana do ano
    
    Args:
        date: Objeto datetime ou string
        
    Returns:
        Número da semana
    """
    if isinstance(date, str):
        date = parse_date_string(date)
    
    if date:
        return date.isocalendar()[1]
    return None

def get_month_name(date):
    """
    Retorna nome do mês em português
    
    Args:
        date: Objeto datetime ou string
        
    Returns:
        Nome do mês
    """
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    if isinstance(date, str):
        date = parse_date_string(date)
    
    if date:
        return meses[date.month - 1]
    return ""

def sanitize_filename(filename):
    """
    Remove caracteres inválidos de nome de arquivo
    
    Args:
        filename: Nome do arquivo
        
    Returns:
        Nome sanitizado
    """
    # Remove caracteres especiais
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove espaços múltiplos
    filename = re.sub(r'\s+', '_', filename)
    return filename

def create_backup_filename():
    """
    Cria nome de arquivo para backup
    
    Returns:
        Nome do arquivo
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"backup_pdv_control_{timestamp}.json"

def format_file_size(size_bytes):
    """
    Formata tamanho de arquivo para leitura humana
    
    Args:
        size_bytes: Tamanho em bytes
        
    Returns:
        String formatada
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def get_greeting():
    """
    Retorna saudação baseada no horário
    
    Returns:
        String de saudação
    """
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        return "Bom dia"
    elif 12 <= hour < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

def days_between(date1, date2):
    """
    Calcula dias entre duas datas
    
    Args:
        date1: Data inicial
        date2: Data final
        
    Returns:
        Número de dias
    """
    if isinstance(date1, str):
        date1 = parse_date_string(date1)
    if isinstance(date2, str):
        date2 = parse_date_string(date2)
    
    if date1 and date2:
        return abs((date2 - date1).days)
    return 0

def is_valid_email(email):
    """
    Valida endereço de email
    
    Args:
        email: String do email
        
    Returns:
        Boolean
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None