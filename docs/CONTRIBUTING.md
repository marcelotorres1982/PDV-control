# 🤝 Guia de Contribuição - PDV Control

Obrigado por considerar contribuir com o PDV Control! Este documento fornece diretrizes para contribuir com o projeto.

---

## 📋 Índice

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
- [Processo de Desenvolvimento](#processo-de-desenvolvimento)
- [Padrões de Código](#padrões-de-código)
- [Processo de Pull Request](#processo-de-pull-request)
- [Reportando Bugs](#reportando-bugs)
- [Sugerindo Melhorias](#sugerindo-melhorias)

---

## 📜 Código de Conduta

Este projeto e todos os participantes seguem um código de conduta. Ao participar, espera-se que você mantenha este código.

### Nossos Valores

- ✨ Respeito e cortesia com todos os colaboradores
- 🤝 Ambiente acolhedor e inclusivo
- 💡 Feedback construtivo e profissional
- 🎯 Foco na qualidade e melhoria contínua

---

## 🚀 Como Posso Contribuir?

### Tipos de Contribuição

Você pode contribuir de várias formas:

#### 1. 🐛 Reportar Bugs
- Encontrou um erro? Abra uma issue detalhada
- Inclua passos para reproduzir o problema
- Adicione screenshots se possível

#### 2. 💡 Sugerir Funcionalidades
- Tem uma ideia para melhorar o sistema?
- Abra uma issue com a tag `enhancement`
- Descreva o caso de uso e benefícios

#### 3. 📝 Melhorar Documentação
- Corrigir erros de digitação
- Adicionar exemplos
- Traduzir documentação
- Melhorar clareza das explicações

#### 4. 💻 Contribuir com Código
- Implementar novas funcionalidades
- Corrigir bugs existentes
- Melhorar performance
- Adicionar testes

#### 5. 🎨 Design e UX
- Melhorar interface do usuário
- Sugerir melhorias de usabilidade
- Criar mockups e protótipos

---

## 🛠️ Processo de Desenvolvimento

### 1. Fork e Clone

```bash
# Fork o repositório no GitHub
# Depois clone seu fork

git clone https://github.com/SEU-USUARIO/pdv-control.git
cd pdv-control
```

### 2. Configurar Ambiente

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Instalar dependências de desenvolvimento
pip install pytest black flake8
```

### 3. Criar Branch

```bash
# Sempre crie uma branch para suas mudanças
git checkout -b feature/nome-da-funcionalidade
# ou
git checkout -b fix/nome-do-bug
```

**Padrões de nomenclatura de branches:**
- `feature/` - Nova funcionalidade
- `fix/` - Correção de bug
- `docs/` - Mudanças na documentação
- `refactor/` - Refatoração de código
- `test/` - Adição de testes

### 4. Fazer Mudanças

- Escreva código claro e bem documentado
- Siga os padrões de código do projeto
- Adicione testes para novas funcionalidades
- Atualize a documentação se necessário

### 5. Testar

```bash
# Execute os testes
pytest

# Verifique a formatação
black --check .

# Verifique o linting
flake8 .
```

### 6. Commit

```bash
# Adicione suas mudanças
git add .

# Commit com mensagem descritiva
git commit -m "feat: adiciona validação de email"
```

**Padrões de mensagens de commit (Conventional Commits):**
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `style:` - Formatação, falta de ponto e vírgula, etc
- `refactor:` - Refatoração de código
- `test:` - Adição de testes
- `chore:` - Atualizações de build, configs, etc

### 7. Push

```bash
# Push para seu fork
git push origin feature/nome-da-funcionalidade
```

### 8. Pull Request

- Abra um Pull Request no GitHub
- Descreva suas mudanças detalhadamente
- Referencie issues relacionadas
- Aguarde revisão

---

## 💻 Padrões de Código

### Python

**Estilo**: Seguimos PEP 8

```python
# ✅ Bom
def calcular_total_deslocamento(registros):
    """Calcula o total de valores de deslocamento."""
    return sum(r.get('valor_deslocamento', 0) for r in registros)

# ❌ Evitar
def CalcTotal(regs):
    total=0
    for r in regs:
        total+=r['valor_deslocamento']
    return total
```

### Formatação

Use **Black** para formatação automática:

```bash
black .
```

### Docstrings

```python
def funcao_exemplo(parametro1, parametro2):
    """
    Breve descrição da função.
    
    Args:
        parametro1: Descrição do parâmetro 1
        parametro2: Descrição do parâmetro 2
        
    Returns:
        Descrição do retorno
        
    Raises:
        ValueError: Quando ocorre erro específico
    """
    pass
```

### Naming Conventions

- **Variáveis e funções**: `snake_case`
- **Classes**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE`
- **Módulos**: `lowercase`

### Imports

```python
# Ordem dos imports:
# 1. Biblioteca padrão
import os
from datetime import datetime

# 2. Bibliotecas de terceiros
import streamlit as st
import pandas as pd

# 3. Imports locais
from config import PROMOTORES
from database import Database
```

---

## 🔍 Processo de Pull Request

### Checklist antes de enviar PR

- [ ] Código segue os padrões do projeto
- [ ] Testes passando
- [ ] Documentação atualizada
- [ ] Sem conflitos com branch main
- [ ] Commit messages seguem convenções
- [ ] PR tem descrição clara

### Template de Pull Request

```markdown
## Descrição
Breve descrição das mudanças.

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## Como Testar
Passos para testar as mudanças.

## Screenshots (se aplicável)
Adicione screenshots se relevante.

## Checklist
- [ ] Código testado localmente
- [ ] Testes passando
- [ ] Documentação atualizada
```

### Processo de Revisão

1. **Revisão Automática**: CI/CD verifica testes e linting
2. **Revisão de Código**: Mantenedor revisa o código
3. **Feedback**: Discussão e ajustes se necessário
4. **Aprovação**: Merge quando aprovado
5. **Release**: Incluído na próxima versão

---

## 🐛 Reportando Bugs

### Antes de Reportar

- Verifique se o bug já foi reportado nas [Issues](https://github.com/marcelotorres1982/pdv-control/issues)
- Teste na versão mais recente
- Colete informações sobre o ambiente

### Como Reportar

Use o template de issue para bugs:

```markdown
## Descrição do Bug
Descrição clara e concisa do problema.

## Passos para Reproduzir
1. Vá para '...'
2. Clique em '...'
3. Role até '...'
4. Veja o erro

## Comportamento Esperado
O que deveria acontecer.

## Comportamento Atual
O que está acontecendo.

## Screenshots
Se aplicável, adicione screenshots.

## Ambiente
- OS: [ex: Windows 10]
- Python: [ex: 3.11]
- Versão do PDV Control: [ex: 1.0.0]
- Navegador: [ex: Chrome 120]

## Informações Adicionais
Qualquer outra informação relevante.
```

---

## 💡 Sugerindo Melhorias

### Template para Sugestões

```markdown
## Descrição da Funcionalidade
Descrição clara da funcionalidade sugerida.

## Motivação
Por que esta funcionalidade seria útil?

## Solução Proposta
Como você imagina que isso funcionaria?

## Alternativas Consideradas
Outras formas de resolver o problema.

## Informações Adicionais
Mockups, exemplos, referências, etc.
```

---

## 🧪 Testes

### Escrevendo Testes

```python
# tests/test_database.py
import pytest
from database import Database

def test_add_record():
    """Testa adição de registro."""
    db = Database('test_db.json')
    
    registro = {
        'data': '2025-10-01',
        'promotor': 'Teste',
        'pdv': 'PDV Teste',
        'valor_deslocamento': 50.0
    }
    
    record_id = db.add_record(registro)
    assert record_id is not None
    
    # Cleanup
    db.delete_record(record_id)
```

### Executando Testes

```bash
# Todos os testes
pytest

# Teste específico
pytest tests/test_database.py

# Com cobertura
pytest --cov=. tests/
```

---

## 📚 Recursos Úteis

### Documentação

- [Streamlit Docs](https://docs.streamlit.io/)
- [Google APIs Python](https://github.com/googleapis/google-api-python-client)
- [PEP 8 Style Guide](https://pep8.org/)

### Ferramentas

- [Black](https://black.readthedocs.io/) - Formatação de código
- [Flake8](https://flake8.pycqa.org/) - Linting
- [Pytest](https://docs.pytest.org/) - Testes
- [Git](https://git-scm.com/doc) - Controle de versão

---

## 🎯 Áreas que Precisam de Ajuda

Estamos especialmente interessados em contribuições nas seguintes áreas:

### Alta Prioridade
- 🔴 Testes automatizados
- 🔴 Documentação em inglês
- 🔴 Melhorias de performance

### Média Prioridade
- 🟡 Interface mobile responsiva
- 🟡 Modo offline robusto
- 🟡 Exportação de relatórios em PDF

### Baixa Prioridade
- 🟢 Temas customizáveis
- 🟢 Notificações por email
- 🟢 Integração com outras APIs

---

## 💬 Comunicação

### Canais de Contato

- **Issues**: Para bugs e sugestões
- **Discussions**: Para perguntas e ideias gerais
- **Email**: marcelotorres1982@gmail.com

### Tempo de Resposta

- **Issues**: 1-3 dias úteis
- **Pull Requests**: 3-7 dias úteis
- **Email**: 1-5 dias úteis

---

## 🏆 Reconhecimento

Todos os contribuidores serão reconhecidos:
- Nome no arquivo CONTRIBUTORS.md
- Menção nos release notes
- Badge de contribuidor no perfil GitHub

---

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto (MIT License).

---

## 🙏 Agradecimentos

Obrigado por dedicar seu tempo para contribuir com o PDV Control! Cada contribuição, não importa o tamanho, é valiosa e apreciada.

### Contribuidores Especiais

Agradecimentos especiais a todos que contribuíram para tornar este projeto melhor! 🎉

---

## 📞 Dúvidas?

Se tiver qualquer dúvida sobre como contribuir:

1. 📖 Leia esta documentação completamente
2. 🔍 Procure em issues e discussions existentes
3. 💬 Abra uma discussion para esclarecer dúvidas
4. 📧 Entre em contato: marcelotorres1982@gmail.com

---

**Juntos construímos um projeto melhor!** 🚀

---

**Desenvolvido com ❤️ pela comunidade**

Mantido por: [Marcelo Torres](https://github.com/marcelotorres1982)  
📧 marcelotorres1982@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/marcelo-t-554b8045/)