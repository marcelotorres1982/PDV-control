# 📍 PDV Control - Sistema de Controle de Promotores em PDV

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)

🚀 Sistema completo para gerenciamento de visitas de promotores em Pontos de Venda (PDV) com integração ao Google Drive e Google Sheets 📋 Funcionalidades • 🛠️ Instalação • 🎯 Como Usar • 📸 Screenshots • 🔑 Configuração • 🤝 Contribuição

---

## 🌟 Visão Geral

O **PDV Control** é um sistema desenvolvido para facilitar o controle e gestão de visitas de promotores em pontos de venda. Com interface intuitiva construída em Streamlit, permite registro completo de check-ins, upload de fotos e sincronização automática com Google Drive e Google Sheets.

### ✨ Por que escolher o PDV Control?

- 🎨 **Interface Moderna**: Design limpo e profissional inspirado no BarbeVibe
- 📱 **Responsivo**: Funciona perfeitamente em qualquer dispositivo
- ⚡ **Sincronização Automática**: Integração total com Google Drive e Sheets
- 📸 **Upload de Fotos**: Armazenamento organizado por promotor e data
- 💰 **Controle Financeiro**: Gerenciamento de valores de deslocamento
- 📊 **Relatórios Automáticos**: Planilhas atualizadas em tempo real
- 🔒 **100% Gratuito**: Open source e sem custos

---

## 🚀 Funcionalidades

### 📋 Registro de Check-in

✅ Nome do promotor  
✅ Seleção de PDV  
✅ Registro automático de horário de check-in  
✅ Valor de deslocamento configurável  
✅ Múltiplas entradas por promotor  
✅ Validação de dados  

### 📸 Upload de Fotos

✅ Upload de múltiplas fotos do PDV  
✅ Organização automática por promotor  
✅ Separação por data de visita  
✅ Armazenamento seguro no Google Drive  
✅ Nomenclatura padronizada  

### 📊 Integração Google

✅ Salvamento automático no Google Sheets  
✅ Atualização em tempo real  
✅ Backup automático de fotos no Drive  
✅ Estrutura de pastas organizada  
✅ Histórico completo de visitas  

### 📈 Visualização de Dados

✅ Dashboard com estatísticas  
✅ Histórico de visitas por promotor  
✅ Relatórios por período  
✅ Exportação de dados  

---

## 🛠️ Instalação

### 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Conta Google (para Drive e Sheets)
- Credenciais da API do Google Cloud

### ⚡ Instalação Rápida

**1. Clone o repositório**

```bash
git clone https://github.com/marcelotorres1982/pdv-control.git
cd pdv-control
```

**2. Instale as dependências**

```bash
pip install -r requirements.txt
```

**3. Configure as credenciais do Google**

- Acesse [Google Cloud Console](https://console.cloud.google.com/)
- Crie um novo projeto
- Ative as APIs: Google Drive API e Google Sheets API
- Crie credenciais OAuth 2.0
- Baixe o arquivo `credentials.json` e coloque na pasta do projeto

**4. Execute o aplicativo**

```bash
streamlit run app.py
```

**5. Acesse no navegador**

```
http://localhost:8501
```

---

## 🎯 Como Usar

### 🆕 Primeiro Uso

1. Inicie o sistema com `streamlit run app.py`
2. Acesse `http://localhost:8501` no seu navegador
3. Faça login com sua conta Google (primeira vez)
4. Configure os PDVs e promotores
5. Comece a registrar visitas!

### 📱 Interface Principal

```
📍 PDV Control - Sistema de Controle de Promotores
│
├── 📝 Novo Check-in
│   ├── Nome do Promotor
│   ├── Selecionar PDV
│   ├── Valor do Deslocamento
│   ├── Upload de Fotos
│   └── Confirmar Check-in
│
├── 📊 Ver Registros
│   ├── Por data específica
│   ├── Por promotor
│   └── Todos os registros
│
├── 📸 Galeria de Fotos
│   ├── Por promotor
│   ├── Por PDV
│   └── Por data
│
└── ⚙️ Configurações
    ├── Gerenciar PDVs
    ├── Gerenciar Promotores
    └── Configurar Google Drive
```

---

## 📂 Estrutura do Projeto

```
pdv-control/
│
├── 📄 app.py                    # Interface principal Streamlit
├── 📄 database.py               # Gerenciamento de dados
├── 📄 google_integration.py     # Integração com Google Drive/Sheets
├── 📄 utils.py                  # Funções auxiliares
├── 📄 config.py                 # Configurações do sistema
├── 📄 requirements.txt          # Dependências do projeto
├── 📄 README.md                 # Documentação
├── 📄 .gitignore               # Arquivos ignorados pelo Git
│
├── 📁 credentials/
│   └── 📄 credentials.json      # Credenciais Google (não versionado)
│
├── 📁 data/
│   └── 📄 local_backup.json     # Backup local dos dados
│
└── 📁 assets/
    └── 📷 screenshots/          # Capturas de tela
```

---

## 🔑 Configuração

### 📊 Google Sheets

O sistema cria automaticamente uma planilha com a seguinte estrutura:

| Data | Hora | Promotor | PDV | Valor Deslocamento | Link Fotos | Observações |
|------|------|----------|-----|-------------------|------------|-------------|

### 📁 Estrutura no Google Drive

```
PDV Control/
│
├── 📁 Promotor 1/
│   ├── 📁 2025-01-15/
│   │   ├── 📷 PDV_A_001.jpg
│   │   ├── 📷 PDV_A_002.jpg
│   │   └── 📷 PDV_B_001.jpg
│   └── 📁 2025-01-16/
│
├── 📁 Promotor 2/
│   └── 📁 2025-01-15/
│       └── 📷 PDV_C_001.jpg
│
└── 📄 registros_pdv.xlsx        # Planilha consolidada
```

### ⚙️ Configurações Personalizadas

Edite o arquivo `config.py`:

```python
# PDVs cadastrados
PDVS = [
    "Supermercado ABC",
    "Farmácia XYZ",
    "Loja de Conveniência 123"
]

# Promotores
PROMOTORES = [
    "João Silva",
    "Maria Santos",
    "Pedro Oliveira"
]

# Valores padrão
VALOR_DESLOCAMENTO_PADRAO = 50.00
MOEDA = "R$"

# Configurações do Google Drive
DRIVE_FOLDER_NAME = "PDV Control"
SHEET_NAME = "Registros PDV"
```

---

## 📸 Screenshots

### 📝 Tela de Check-in
*Interface para registro de nova visita com todos os campos*

### 📊 Dashboard de Registros
*Visualização de todos os check-ins com filtros e busca*

### 📸 Galeria de Fotos
*Visualização organizada das fotos por promotor e data*

### ⚙️ Painel de Configurações
*Gerenciamento de PDVs, promotores e integrações*

---

## 🔮 Próximas Funcionalidades

- 🗺️ **Geolocalização**: Validação de check-in por GPS
- 📱 **App Mobile**: Versão nativa para Android/iOS
- 📊 **Analytics Avançado**: Dashboards interativos
- 🔔 **Notificações**: Alertas de check-in pendentes
- 💾 **Modo Offline**: Sincronização posterior
- 🎯 **Metas e KPIs**: Acompanhamento de performance
- 📈 **Relatórios PDF**: Exportação automática
- 🤖 **IA para Análise**: Insights automatizados

---

## 🤝 Contribuição

Contribuições são sempre bem-vindas! 🎉

### 📝 Como Contribuir

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### 🐛 Reportar Bugs

Encontrou um bug? Abra uma issue com:

- 📝 Descrição detalhada
- 🖥️ Sistema operacional
- 🐍 Versão do Python
- 📸 Screenshots (se aplicável)
- 🔄 Passos para reproduzir

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨💻 Autor

**Marcelo Torres**

- 🌐 Website: seusite.com
- 📧 Email: marcelotorres1982@gmail.com
- 💼 LinkedIn: [https://www.linkedin.com/in/marcelo-t-554b8045/](https://www.linkedin.com/in/marcelo-t-554b8045/)
- 🐙 GitHub: [https://github.com/marcelotorres1982](https://github.com/marcelotorres1982)

---

## 🙏 Agradecimentos

- 🎨 **Streamlit** pela framework incrível
- 💡 **Comunidade Python** pelo suporte
- 🚀 **Google Cloud** pelas APIs robustas
- 📍 **Promotores** que inspiraram este projeto
- ✨ **Você** por usar o PDV Control!

---

## 📞 Suporte

Precisa de ajuda? Entre em contato:

- 💬 **Issues**: [GitHub Issues](https://github.com/marcelotorres1982/pdv-control/issues)
- 📧 **Email**: marcelotorres1982@gmail.com
- 💭 **Discussões**: [GitHub Discussions](https://github.com/marcelotorres1982/pdv-control/discussions)

---

## 📊 Status do Projeto

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Last Commit](https://img.shields.io/badge/last%20commit-outubro%202025-green)

---

© 2025 PDV Control. Todos os direitos reservados.