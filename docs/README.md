# 📍 PDV Control - Sistema de Gestão de Check-ins

Sistema completo de gestão de check-ins para promotores de vendas, com integração ao Google Drive e Google Sheets.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://pdv-control.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com)

## 🚀 Demo

**Aplicação em produção:** [https://pdv-control.streamlit.app/](https://pdv-control.streamlit.app/)

## 📋 Sobre o Projeto

O PDV Control foi desenvolvido para resolver o problema de registro e acompanhamento de visitas de promotores em pontos de venda. O sistema oferece:

- ✅ **Check-in com geolocalização** - Registro automático da localização
- 📸 **Upload múltiplo de fotos** - Armazenamento seguro no Google Drive
- 📊 **Sincronização automática** - Dados salvos no Google Sheets em tempo real
- 👥 **Gestão de promotores e PDVs** - Interface administrativa completa
- 🔍 **Detecção de duplicados** - Identifica e remove check-ins duplicados
- 💰 **Controle financeiro** - Rastreamento de valores de deslocamento

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**
- **Streamlit** - Framework para interface web
- **Google Drive API** - Armazenamento de fotos
- **Google Sheets API** - Banco de dados em nuvem
- **OAuth2** - Autenticação segura
- **SQLite** - Banco de dados local para cache

## 📦 Instalação

### Pré-requisitos

- Python 3.9 ou superior
- Conta Google (para Google Drive e Sheets)
- Projeto no Google Cloud Console

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/marcelotorres1982/pdv-control.git
cd pdv-control
```

### Passo 2: Criar ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Passo 3: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar Google Cloud

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative as APIs:
   - Google Drive API
   - Google Sheets API
4. Crie credenciais OAuth 2.0:
   - Tipo: Desktop app
   - Baixe o arquivo JSON
5. Renomeie para `credentials.json` e coloque em `credentials/`

### Passo 5: Executar localmente

```bash
streamlit run app.py
```

## 🔐 Configuração para Streamlit Cloud

### 1. Autenticar localmente primeiro

Execute a aplicação localmente e complete a autenticação OAuth2:

```bash
streamlit run app.py
```

### 2. Gerar token base64

```bash
# Linux/Mac
base64 -w 0 credentials/token.pickle > token_base64.txt

# Windows PowerShell
[Convert]::ToBase64String([IO.File]::ReadAllBytes("credentials/token.pickle")) | Out-File -FilePath token_base64.txt -NoNewline
```

### 3. Configurar Secrets no Streamlit Cloud

No painel do Streamlit Cloud, adicione em **Settings → Secrets**:

```toml
google_token_base64 = "COLE_O_TOKEN_AQUI"
```

## 📁 Estrutura do Projeto

```
pdv-control/
├── app.py                      # Aplicação principal
├── google_integration.py       # Integração com Google APIs
├── database.py                 # Banco de dados local
├── config.py                   # Configurações
├── requirements.txt            # Dependências
├── credentials/
│   ├── credentials.json        # Credenciais OAuth2 (não commitar)
│   └── token.pickle           # Token de acesso (não commitar)
├── .streamlit/
│   ├── config.toml            # Configurações do Streamlit
│   └── secrets.toml           # Secrets locais (não commitar)
└── README.md
```

## 🎯 Funcionalidades

### Check-in
- Seleção de promotor e PDV
- Valor de deslocamento configurável
- Número de entradas
- Upload de múltiplas fotos
- Observações opcionais

### Visualização de Registros
- Filtros por data, promotor e PDV
- Estatísticas consolidadas
- Detalhes completos de cada visita
- Links para fotos no Drive

### Galeria de Fotos
- Visualização organizada por promotor e data
- Links diretos para Google Drive
- Preview de todas as fotos

### Painel Administrativo
- **Links:** Acesso rápido à planilha e pasta do Drive
- **Promotores:** Adicionar e remover promotores
- **PDVs:** Adicionar e remover pontos de venda
- **Duplicados:** Detectar e remover check-ins duplicados

## 🔒 Segurança

- Autenticação OAuth2 com Google
- Tokens criptografados
- Acesso controlado via Google Account
- Dados armazenados no Google Drive pessoal

## 📊 Google Sheets

O sistema cria automaticamente uma planilha com as seguintes colunas:

| Coluna | Descrição |
|--------|-----------|
| Data | Data do check-in (YYYY-MM-DD) |
| Hora | Hora do check-in (HH:MM:SS) |
| Promotor | Nome do promotor |
| PDV | Nome do ponto de venda |
| Valor Deslocamento | Valor em R$ |
| Nº Entradas | Quantidade de entradas |
| Observações | Notas adicionais |
| Fotos | Links das fotos no Drive |

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Marcelo Torres**

- Portfolio: [marcelotorres1982.github.io](https://marcelotorres1982.github.io/)
- LinkedIn: [marcelo-t-554b8045](https://www.linkedin.com/in/marcelo-t-554b8045/)
- GitHub: [@marcelotorres1982](https://github.com/marcelotorres1982)
- Email: marcelotorres1982@gmail.com

## 🙏 Agradecimentos

- [Streamlit](https://streamlit.io/) - Framework incrível para Python
- [Google APIs](https://developers.google.com/) - Drive e Sheets APIs
- Comunidade Python

## 📈 Roadmap

- [ ] Dashboard com gráficos e métricas
- [ ] Exportação de relatórios em PDF
- [ ] Notificações por email
- [ ] App mobile (PWA)
- [ ] Backup automático
- [ ] Integração com WhatsApp

## 🐛 Problemas Conhecidos

Se encontrar problemas, por favor:
1. Verifique se as APIs estão habilitadas no Google Cloud
2. Confirme que o token não expirou
3. Abra uma [issue](https://github.com/marcelotorres1982/pdv-control/issues) detalhando o problema

## 📞 Suporte

Para suporte, abra uma issue no GitHub ou entre em contato via email.

---

**Desenvolvido com ❤️ por Marcelo Torres**