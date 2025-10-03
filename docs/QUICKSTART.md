# ⚡ Guia Rápido - PDV Control

Comece a usar o PDV Control em menos de 10 minutos!

---

## 🚀 Início Rápido

### 1️⃣ Instalar (2 minutos)

```bash
# Clone o repositório
git clone https://github.com/marcelotorres1982/pdv-control.git
cd pdv-control

# Instale as dependências
pip install -r requirements.txt
```

### 2️⃣ Configurar Google (5 minutos)

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um projeto novo
3. Ative **Google Drive API** e **Google Sheets API**
4. Crie credenciais OAuth 2.0 (Aplicativo Desktop)
5. Baixe `credentials.json` e coloque em `credentials/`

### 3️⃣ Executar (1 minuto)

```bash
streamlit run app.py
```

### 4️⃣ Usar (2 minutos)

1. Clique em **"Conectar Google"** na sidebar
2. Autorize o acesso
3. Faça seu primeiro check-in! 🎉

---

## 📱 Uso Diário

### Fazer Check-in

```
1. Abrir app → Novo Check-in
2. Selecionar Promotor e PDV
3. Upload de fotos
4. Confirmar ✅
```

### Ver Registros

```
1. Ir em → Ver Registros
2. Aplicar filtros
3. Visualizar estatísticas 📊
```

### Acessar Fotos

```
Todas as fotos ficam no seu Google Drive em:
📁 PDV Control/[Promotor]/[Data]/
```

---

## 🔧 Comandos Essenciais

```bash
# Executar aplicação
streamlit run app.py

# Porta customizada
streamlit run app.py --server.port 8502

# Acesso remoto
streamlit run app.py --server.address 0.0.0.0
```

---

## 💡 Dicas Rápidas

✅ **Faça**: Upload imediato das fotos  
✅ **Faça**: Use nomes descritivos nos PDVs  
✅ **Faça**: Adicione observações importantes  

❌ **Evite**: Fotos muito grandes (>10MB)  
❌ **Evite**: Deixar para sincronizar depois  
❌ **Evite**: Pular o campo de observações  

---

## 🆘 Problemas Comuns

### Erro: Credenciais não encontradas
```bash
# Certifique-se de ter o arquivo credentials.json em:
credentials/credentials.json
```

### Erro: Porta em uso
```bash
# Use outra porta
streamlit run app.py --server.port 8502
```

### Erro: Módulo não encontrado
```bash
# Reinstale dependências
pip install -r requirements.txt --upgrade
```

---

## 📚 Documentação Completa

- 📖 [README.md](README.md) - Visão geral completa
- 🛠️ [INSTALL.md](INSTALL.md) - Guia de instalação detalhado
- 💡 [EXAMPLES.md](EXAMPLES.md) - Exemplos práticos
- 🤝 [CONTRIBUTING.md](CONTRIBUTING.md) - Como contribuir

---

## 📞 Precisa de Ajuda?

- 💬 [GitHub Issues](https://github.com/marcelotorres1982/pdv-control/issues)
- 📧 Email: marcelotorres1982@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/marcelo-t-554b8045/)

---

## ✨ Próximos Passos

Depois de começar:

1. ⚙️ Personalize promotores e PDVs em `config.py`
2. 📊 Explore os relatórios e filtros
3. 📸 Configure backup automático
4. 👥 Treine sua equipe
5. 🚀 Maximize o uso do sistema!

---

**Pronto! Você está operacional! 🎉**

Agora é só usar e aproveitar o PDV Control para gerenciar suas visitas aos pontos de venda!

---

**Desenvolvido com ❤️ por Marcelo Torres**