# 📁 Estrutura do Projeto - PDV Control

Documentação completa da estrutura de arquivos e organização do projeto.

---

## 🗂️ Visão Geral

```
pdv-control/
├── 📄 app.py                      # Aplicação principal Streamlit
├── 📄 database.py                 # Gerenciamento de banco de dados local
├── 📄 google_integration.py       # Integração com Google Drive/Sheets
├── 📄 config.py                   # Configurações do sistema
├── 📄 utils.py                    # Funções utilitárias
├── 📄 requirements.txt            # Dependências do projeto
├── 📄 .gitignore                  # Arquivos ignorados pelo Git
│
├── 📁 credentials/                # Credenciais Google (não versionado)
│   ├── 📄 credentials.json        # Credenciais OAuth 2.0
│   └── 📄 token.pickle            # Token de acesso (gerado automaticamente)
│
├── 📁 data/                       # Dados locais (não versionado)
│   ├── 📄 local_backup.json       # Backup local dos registros
│   └── 📁 backups/                # Backups automáticos
│
├── 📁 assets/                     # Recursos estáticos
│   └── 📁 screenshots/            # Capturas de tela
│
├── 📁 tests/                      # Testes automatizados
│   ├── 📄 test_database.py
│   ├── 📄 test_utils.py
│   └── 📄 test_integration.py
│
└── 📁 docs/                       # Documentação
    ├── 📄 README.md               # Documentação principal
    ├── 📄 INSTALL.md              # Guia de instalação
    ├── 📄 QUICKSTART.md           # Guia rápido
    ├── 📄 EXAMPLES.md             # Exemplos de uso
    ├── 📄 CONTRIBUTING.md         # Guia de contribuição
    ├── 📄 STRUCTURE.md            # Este arquivo
    └── 📄 LICENSE                 # Licença MIT
```

---

## 📄 Descrição dos Arquivos

### Arquivos Principais

#### `app.py`
**Propósito**: Interface principal do usuário com Streamlit

**Responsabilidades**:
- Renderização da interface
- Gerenciamento de formulários
- Interação com usuário
- Orquestração de funcionalidades

**Principais Funções**:
```python
main()                    # Função principal
novo_checkin()           # Tela de novo check-in
ver_registros()          # Visualização de registros
galeria_fotos()          # Galeria de fotos
configuracoes()          # Painel de configurações
```

**Fluxo de Execução**:
```
app.py inicializa
    ↓
Carrega sessão (Database, GoogleIntegration)
    ↓
Renderiza sidebar com menu
    ↓
Executa função correspondente ao menu selecionado
    ↓
Processa ações do usuário
    ↓
Atualiza estado e interface
```

---

#### `database.py`
**Propósito**: Gerenciamento de dados local em JSON

**Responsabilidades**:
- CRUD de registros
- Persistência local
- Queries e filtros
- Estatísticas

**Principais Métodos**:
```python
add_record()             # Adiciona novo registro
get_all_records()        # Retorna todos os registros
get_records_by_date()    # Filtra por data
get_records_by_promotor() # Filtra por promotor
update_record()          # Atualiza registro
delete_record()          # Remove registro
get_statistics()         # Calcula estatísticas
export_to_csv()          # Exporta para CSV
backup_database()        # Cria backup
```

**Estrutura de Dados**:
```json
{
  "id": "2025-10-01_14-30-00_João_Silva",
  "data": "2025-10-01",
  "hora": "14:30:00",
  "promotor": "João Silva",
  "pdv": "Supermercado Central",
  "valor_deslocamento": 50.00,
  "num_entradas": 1,
  "observacoes": "Estoque completo",
  "fotos": ["url1", "url2"],
  "created_at": "2025-10-01T14:30:00",
  "updated_at": "2025-10-01T14:30:00"
}
```

---

#### `google_integration.py`
**Propósito**: Integração com Google Drive e Sheets

**Responsabilidades**:
- Autenticação OAuth
- Upload de fotos para Drive
- Sincronização com Sheets
- Gerenciamento de pastas

**Principais Métodos**:
```python
authenticate()           # Autentica com Google
upload_photo()          # Upload de foto para Drive
add_to_sheet()          # Adiciona linha na planilha
get_spreadsheet_url()   # URL da planilha
get_all_records_from_sheet() # Lê dados da planilha
_setup_drive_structure() # Configura estrutura de pastas
_get_or_create_folder()  # Cria/obtém pasta
```

**Estrutura no Google Drive**:
```
📁 PDV Control/
├── 📁 João Silva/
│   ├── 📁 2025-10-01/
│   │   ├── 📷 Supermercado_Central_001.jpg
│   │   ├── 📷 Supermercado_Central_002.jpg
│   │   └── 📷 Supermercado_Central_003.jpg
│   └── 📁 2025-10-02/
│       └── ...
├── 📁 Maria Santos/
│   └── ...
└── 📊 Registros PDV.xlsx
```

**Estrutura da Planilha**:
| Data | Hora | Promotor | PDV | Valor | Entradas | Obs | Links Fotos |
|------|------|----------|-----|-------|----------|-----|-------------|
| ... | ... | ... | ... | ... | ... | ... | ... |

---

#### `config.py`
**Propósito**: Configurações centralizadas do sistema

**Seções**:
- Configurações gerais
- Listas de promotores e PDVs
- Valores e moeda
- Configurações do Google
- Configurações de upload
- Formatos de data/hora
- Mensagens do sistema
- Validações
- Temas e ícones

**Como Personalizar**:
```python
# Adicionar promotores
PROMOTORES = [
    "Seu Promotor 1",
    "Seu Promotor 2",
]

# Adicionar PDVs
PDVS = [
    "Seu PDV 1",
    "Seu PDV 2",
]

# Alterar valor padrão
VALOR_DESLOCAMENTO_PADRAO = 75.00

# Alterar limites
MAX_PHOTOS_PER_CHECKIN = 30
MAX_FILE_SIZE_MB = 20
```

---

#### `utils.py`
**Propósito**: Funções auxiliares e utilitárias

**Categorias de Funções**:

**Formatação**:
```python
format_currency()        # Formata moeda
format_date()           # Formata data
format_time()           # Formata hora
format_datetime()       # Formata data/hora completo
```

**Validação**:
```python
validate_promotor_name() # Valida nome do promotor
validate_pdv_name()     # Valida nome do PDV
validate_valor_deslocamento() # Valida valor
validate_num_entradas() # Valida número de entradas
validate_image_file()   # Valida arquivo de imagem
```

**Cálculos**:
```python
calculate_statistics()  # Calcula estatísticas
get_date_range()       # Retorna intervalo de datas
days_between()         # Dias entre datas
```

**Utilidades**:
```python
generate_photo_filename() # Gera nome de arquivo
generate_folder_path()   # Gera caminho de pasta
sanitize_filename()     # Limpa nome de arquivo
parse_date_string()     # Converte string em data
get_greeting()          # Retorna saudação
```

---

## 🔄 Fluxo de Dados

### Check-in Completo

```
1. Usuário preenche formulário
        ↓
2. app.py valida dados (utils.py)
        ↓
3. app.py cria registro
        ↓
4. Fotos → google_integration.py → Google Drive
        ↓
5. Registro → database.py → local_backup.json
        ↓
6. Registro → google_integration.py → Google Sheets
        ↓
7. Feedback visual para usuário
```

### Consulta de Registros

```
1. Usuário aplica filtros
        ↓
2. app.py solicita dados
        ↓
3. database.py retorna registros filtrados
        ↓
4. app.py processa e formata (utils.py)
        ↓
5. Exibição na interface
```

### Sincronização com Google

```
Modo Online:
    Registro local → Imediato → Google

Modo Offline:
    Registro local → Queue → Sincronização posterior
```

---

## 🗃️ Banco de Dados Local

### Estrutura do JSON

```json
[
  {
    "id": "unique_id_1",
    "data": "2025-10-01",
    "hora": "09:00:00",
    "promotor": "João Silva",
    "pdv": "PDV 1",
    "valor_deslocamento": 50.0,
    "num_entradas": 1,
    "observacoes": "",
    "fotos": ["url1", "url2"],
    "created_at": "2025-10-01T09:00:00",
    "updated_at": null
  },
  {
    "id": "unique_id_2",
    ...
  }
]
```

### Operações CRUD

**Create**:
```python
db = Database()
registro = {...}
record_id = db.add_record(registro)
```

**Read**:
```python
# Todos os registros
registros = db.get_all_records()

# Por filtro
registros = db.get_records_by_promotor("João Silva")
registros = db.get_records_by_date("2025-10-01")
```

**Update**:
```python
db.update_record(record_id, {'observacoes': 'Nova obs'})
```

**Delete**:
```python
db.delete_record(record_id)
```

---

## 🔐 Segurança

### Credenciais

**Arquivos Sensíveis** (não versionados):
- `credentials/credentials.json` - Credenciais OAuth
- `credentials/token.pickle` - Token de acesso
- `data/` - Dados locais

**Proteção**:
- `.gitignore` configurado
- OAuth 2.0 para autenticação
- Tokens armazenados localmente
- Acesso limitado aos escopos necessários

### Boas Práticas

✅ **Faça**:
- Mantenha `credentials.json` seguro
- Não compartilhe tokens
- Revise permissões regularmente

❌ **Não Faça**:
- Commitar credenciais no Git
- Compartilhar arquivos de configuração
- Usar credenciais em produção sem cuidado

---

## 🧪 Testes

### Estrutura de Testes

```
tests/
├── test_database.py       # Testes do banco de dados
├── test_utils.py          # Testes de utilidades
├── test_integration.py    # Testes de integração
└── conftest.py           # Fixtures pytest
```

### Executar Testes

```bash
# Todos os testes
pytest

# Teste específico
pytest tests/test_database.py

# Com cobertura
pytest --cov=. tests/

# Verbose
pytest -v
```

---

## 📦 Dependências

### Principais

- **streamlit**: Interface web
- **google-auth**: Autenticação Google
- **google-api-python-client**: APIs do Google
- **pandas**: Manipulação de dados
- **Pillow**: Processamento de imagens

### Opcionais

- **plotly**: Gráficos interativos
- **openpyxl**: Exportação Excel
- **reportlab**: Geração de PDF
- **pytest**: Testes

---

## 🚀 Deploy

### Streamlit Cloud (Recomendado)

```bash
# 1. Push para GitHub
git push origin main

# 2. Acesse https://share.streamlit.io
# 3. Conecte repositório
# 4. Configure secrets (credentials)
# 5. Deploy automático
```

### Docker

```bash
# Build
docker build -t pdv-control .

# Run
docker run -p 8501:8501 pdv-control
```

### Servidor Local

```bash
# Com nohup (Linux)
nohup streamlit run app.py &

# Com screen (Linux)
screen -S pdv
streamlit run app.py
# Ctrl+A+D para detach
```

---

## 🔧 Manutenção

### Backup

```bash
# Backup manual
python -c "from database import Database; db = Database(); db.backup_database()"

# Backup Google Drive
# Automático a cada check-in
```

### Logs

```bash
# Logs do Streamlit
~/.streamlit/logs/

# Logs personalizados (se configurado)
logs/app.log
```

### Limpeza

```bash
# Limpar cache
rm -rf __pycache__
rm -rf .pytest_cache

# Limpar backups antigos
find data/backups -mtime +30 -delete
```

---

## 📈 Monitoramento

### Métricas Importantes

- Total de check-ins por dia
- Tempo médio de resposta
- Taxa de sucesso de uploads
- Uso de armazenamento no Drive

### Logs de Auditoria

Todos os check-ins são registrados com:
- Timestamp
- Usuário (promotor)
- Ação realizada
- Status (sucesso/falha)

---

## 🎯 Roadmap

### Versão Atual (1.0.0)
- ✅ Check-in básico
- ✅ Upload de fotos
- ✅ Integração Google
- ✅ Relatórios simples

### Próximas Versões
- 🔄 v1.1: Modo offline robusto
- 🔄 v1.2: Relatórios avançados
- 🔄 v1.3: App mobile
- 🔄 v2.0: Analytics e IA

---

**Documentação mantida por: Marcelo Torres**  
📧 marcelotorres1982@gmail.com  
📅 Última atualização: Outubro 2025