# 🚀 Guia de Instalação - PDV Control

Este guia detalha o processo completo de instalação e configuração do sistema PDV Control.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)
- **Conta Google** (para integração com Drive e Sheets)

### Verificando Instalações

```bash
# Verificar Python
python --version
# ou
python3 --version

# Verificar pip
pip --version
# ou
pip3 --version

# Verificar Git
git --version
```

---

## 📥 Passo 1: Clonar o Repositório

```bash
# Clone o repositório
git clone https://github.com/marcelotorres1982/pdv-control.git

# Entre no diretório
cd pdv-control
```

---

## 🔧 Passo 2: Criar Ambiente Virtual (Recomendado)

É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

### No Windows:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate
```

### No Linux/Mac:

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

---

## 📦 Passo 3: Instalar Dependências

Com o ambiente virtual ativado, instale as dependências:

```bash
pip install -r requirements.txt
```

### Instalação Individual (caso necessário)

Se preferir instalar as bibliotecas individualmente:

```bash
pip install streamlit
pip install google-auth google-auth-oauthlib google-auth-httplib2
pip install google-api-python-client
pip install pandas numpy pillow
pip install python-dateutil pytz
```

---

## 🔑 Passo 4: Configurar Google Cloud

### 4.1 Criar Projeto no Google Cloud

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Clique em "Criar Projeto"
3. Digite um nome para o projeto (ex: "PDV Control")
4. Clique em "Criar"

### 4.2 Ativar APIs Necessárias

1. No menu lateral, vá em **APIs e Serviços** → **Biblioteca**
2. Procure e ative as seguintes APIs:
   - **Google Drive API**
   - **Google Sheets API**

### 4.3 Criar Credenciais OAuth 2.0

1. Vá em **APIs e Serviços** → **Credenciais**
2. Clique em **+ CRIAR CREDENCIAIS**
3. Selecione **ID do cliente OAuth**
4. Configure a tela de consentimento OAuth (se solicitado):
   - Tipo de usuário: **Externo**
   - Nome do aplicativo: **PDV Control**
   - Email de suporte: seu email
   - Salve e continue
5. Tipo de aplicativo: **Aplicativo para computador**
6. Nome: **PDV Control Desktop**
7. Clique em **CRIAR**
8. Baixe o arquivo JSON das credenciais

### 4.4 Configurar Credenciais no Projeto

```bash
# Criar pasta de credenciais
mkdir credentials

# Mover o arquivo baixado para a pasta e renomear
mv ~/Downloads/client_secret_*.json credentials/credentials.json
```

---

## 📁 Passo 5: Estrutura de Diretórios

Crie as pastas necessárias:

```bash
# Windows
mkdir data
mkdir data\backups

# Linux/Mac
mkdir -p data/backups
```

A estrutura final deve ficar assim:

```
pdv-control/
├── app.py
├── database.py
├── google_integration.py
├── config.py
├── utils.py
├── requirements.txt
├── README.md
├── INSTALL.md
├── .gitignore
├── credentials/
│   └── credentials.json
└── data/
    └── backups/
```

---

## ⚙️ Passo 6: Configuração Inicial

### 6.1 Editar Configurações (Opcional)

Abra o arquivo `config.py` e ajuste conforme necessário:

```python
# Exemplos de configurações que você pode alterar

# Adicionar/remover promotores
PROMOTORES = [
    "Seu Promotor 1",
    "Seu Promotor 2",
    # ...
]

# Adicionar/remover PDVs
PDVS = [
    "Seu PDV 1",
    "Seu PDV 2",
    # ...
]

# Valor padrão de deslocamento
VALOR_DESLOCAMENTO_PADRAO = 50.00
```

---

## 🚀 Passo 7: Executar o Aplicativo

```bash
streamlit run app.py
```

O aplicativo abrirá automaticamente no seu navegador em `http://localhost:8501`

### Primeira Execução

1. Na primeira execução, clique em **"Conectar Google"** na sidebar
2. Você será redirecionado para fazer login na sua conta Google
3. Autorize o aplicativo a acessar o Google Drive e Sheets
4. Após autorização, você será redirecionado de volta ao aplicativo

---

## ✅ Verificação de Instalação

Para verificar se tudo está funcionando:

1. **Teste de Conexão**: Verifique se aparece "✅ Google Drive conectado" na sidebar
2. **Teste de Check-in**: Faça um check-in de teste
3. **Verificar Google Drive**: Acesse seu Drive e verifique se a pasta "PDV Control" foi criada
4. **Verificar Google Sheets**: Verifique se a planilha "Registros PDV" foi criada

---

## 🔧 Solução de Problemas

### Erro: "credentials.json não encontrado"

**Solução**: Certifique-se de que o arquivo está em `credentials/credentials.json`

```bash
# Verificar se o arquivo existe
ls credentials/credentials.json
# ou no Windows
dir credentials\credentials.json
```

### Erro: "ModuleNotFoundError"

**Solução**: Reinstale as dependências

```bash
pip install -r requirements.txt --upgrade
```

### Erro ao conectar com Google

**Solução**: 
1. Verifique se as APIs estão ativadas no Google Cloud Console
2. Verifique se o arquivo `credentials.json` é válido
3. Delete o arquivo `credentials/token.pickle` e tente novamente

```bash
rm credentials/token.pickle
```

### Porta 8501 já em uso

**Solução**: Use uma porta diferente

```bash
streamlit run app.py --server.port 8502
```

### Erro de permissão no Google Drive

**Solução**: 
1. Vá em [Google Account Permissions](https://myaccount.google.com/permissions)
2. Remova o acesso do "PDV Control"
3. Conecte novamente no aplicativo

---

## 🔄 Atualizações

Para atualizar o projeto para a versão mais recente:

```bash
# Puxar últimas alterações
git pull origin main

# Atualizar dependências
pip install -r requirements.txt --upgrade
```

---

## 🐳 Instalação com Docker (Avançado)

Se você preferir usar Docker, aqui está um exemplo de `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Comandos Docker:**

```bash
# Build da imagem
docker build -t pdv-control .

# Executar container
docker run -p 8501:8501 -v $(pwd)/credentials:/app/credentials -v $(pwd)/data:/app/data pdv-control
```

---

## 📱 Acesso Remoto (Opcional)

Para acessar o aplicativo de outros dispositivos na mesma rede:

```bash
streamlit run app.py --server.address 0.0.0.0
```

Então acesse de outro dispositivo usando: `http://IP_DO_SEU_COMPUTADOR:8501`

---

## 🔒 Segurança

### Proteção de Credenciais

**⚠️ IMPORTANTE**: 

- **NUNCA** commite o arquivo `credentials.json` no Git
- **NUNCA** compartilhe suas credenciais
- O arquivo `.gitignore` já está configurado para ignorar credenciais

### Backup de Segurança

Faça backup regular do arquivo `credentials.json` em local seguro.

---

## 🆘 Suporte

Se encontrar problemas durante a instalação:

1. **Verifique os Issues**: [GitHub Issues](https://github.com/marcelotorres1982/pdv-control/issues)
2. **Crie um novo Issue**: Descreva o problema detalhadamente
3. **Email**: marcelotorres1982@gmail.com

---

## ✨ Próximos Passos

Após a instalação bem-sucedida:

1. 📖 Leia o [README.md](README.md) para conhecer todas as funcionalidades
2. ⚙️ Configure promotores e PDVs no arquivo `config.py`
3. 📝 Faça seu primeiro check-in de teste
4. 📊 Explore os relatórios e visualizações

---

## 🎓 Recursos Adicionais

### Documentação Oficial

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Drive API](https://developers.google.com/drive)
- [Google Sheets API](https://developers.google.com/sheets)

### Tutoriais Recomendados

- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2)
- [Streamlit Tutorial](https://docs.streamlit.io/library/get-started)

---

## 🎉 Conclusão

Parabéns! Você concluiu a instalação do PDV Control. 

O sistema está pronto para uso! 🚀

---

**Desenvolvido com ❤️ por Marcelo Torres**

📧 marcelotorres1982@gmail.com  
🐙 [GitHub](https://github.com/marcelotorres1982)  
💼 [LinkedIn](https://www.linkedin.com/in/marcelo-t-554b8045/)