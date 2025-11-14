# 🚀 Guia de Instalação – SPA PDV Control

Este guia cobre tudo o que você precisa para subir o frontend baseado em **Vue 3 + Vite + Tailwind**. Nenhum backend acompanha o projeto, então você pode apontar `VITE_API_BASE_URL` para qualquer serviço próprio (REST, GraphQL, BaaS, etc.).

---

## 📋 Pré-requisitos

| Ferramenta | Versão recomendada | Observações |
|------------|--------------------|-------------|
| Node.js    | 20.10+             | Testado com a imagem oficial dos Dev Containers |
| npm        | 10+                | Use `pnpm` ou `yarn` se preferir, adaptando os comandos |
| Git        | 2.40+              | Necessário para clonar o repo |

> Dica: `.nvmrc` não é necessário, mas é recomendável alinhar a versão de Node com o Dev Container (`node:22`).

---

## 📥 1. Clonar o repositório

```bash
git clone https://github.com/marcelotorres1982/pdv-control.git
cd pdv-control
```

---

## ⚙️ 2. Configurar variáveis do frontend

```bash
cd frontend
cp .env.example .env
```

- Defina `VITE_API_BASE_URL` para o host das suas APIs.
- Se não houver um serviço disponível ainda, mantenha um placeholder (`http://localhost:8000/api`, por exemplo) e use dados mockados.
- (Opcional) Use `VITE_GOOGLE_OAUTH_URL` para apontar diretamente para o endpoint OAuth do Google quando seu backend ainda não expõe `/auth/google-login`.

---

## 📦 3. Instalar dependências

```bash
npm install
# ou
pnpm install
# ou
yarn install
```

---

## 🧪 4. Scripts essenciais

```bash
npm run dev        # Vite Dev Server
npm run build      # Build de produção (gera dist/)
npm run preview    # Serve o build localmente
npm run lint       # ESLint + Prettier
npm run test:unit  # Vitest
npm run test:e2e   # Cypress (usa o build + preview)
```

> Execute `npm run lint` e `npm run test:unit` antes de abrir um PR.

---

## 🔌 5. Conectando a sua API

1. Exponha endpoints compatíveis com os clients existentes (`src/api/*.ts`). O contrato é simples e baseado em JSON.
2. Ajuste `VITE_API_BASE_URL` no `.env`.
3. Reinicie `npm run dev` para aplicar a nova configuração.
4. Utilize o Vue Query Devtools para inspecionar o cache e validar as chamadas.

Não há restrições sobre a tecnologia usada no servidor. Pode ser FastAPI, Express, Firebase Functions, Supabase, Airtable, etc. O importante é manter os mesmos caminhos/estruturas esperados pelo frontend.

---

## 🧱 Estrutura pós-instalação

```
pdv-control/
├── frontend/
│   ├── node_modules/
│   ├── src/
│   ├── vite.config.ts
│   └── package-lock.json
├── docs/
└── ...
```

---

## ✅ Checklist final

- [ ] Node e npm instalados nas versões recomendadas.
- [ ] Dependências do `frontend/` instaladas.
- [ ] `.env` configurado com `VITE_API_BASE_URL`.
- [ ] `npm run dev` servindo o frontend em `http://localhost:5173`.
- [ ] `npm run lint` e `npm run test:unit` executados sem erros.
- [ ] APIs externas mapeadas (mock ou serviço real) para alimentar os componentes.

Pronto! Seu ambiente está preparado para evoluir o PDV Control apenas com HTML, Tailwind e Vue. Consulte `docs/QUICKSTART.md` para um resumo operacional e `docs/CONTRIBUTING.md` para o fluxo de contribuição.***
