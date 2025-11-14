# 📍 PDV Control – SPA Vue + Tailwind

O PDV Control foi totalmente reescrito como uma **Single Page Application** construída com **Vue 3**, **Vite**, **Tailwind CSS**, **Pinia**, **Vue Router** e **@tanstack/vue-query**. Todo o legado em Python/Streamlit foi descartado e nenhuma implementação de backend acompanha este repositório – você é livre para conectar qualquer serviço HTTP compatível com os clients Axios já disponíveis em `src/api/`.

[![Vue](https://img.shields.io/badge/Vue_3-42B883?style=for-the-badge&logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![Tailwind](https://img.shields.io/badge/Tailwind-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)

> ✅ Repositório 100% frontend. Defina suas próprias APIs ou serviços (REST, GraphQL, BaaS, etc.) e configure o endpoint via `VITE_API_BASE_URL`.

---

## 🎯 Visão Geral

Mantendo o objetivo original — facilitar o controle de execuções em PDV com check-ins, uploads e dashboards — a nova versão concentra todo o trabalho na interface:

- **Frontend (este repositório)**: SPA em Vue 3 + Tailwind, com Pinia, Vue Router e Vue Query.
- **Serviço de dados externo (opcional)**: qualquer API acessível via HTTP/JSON que implemente os contratos de `src/api/`.

Principais áreas já modeladas:

- **Dashboard**: cards com indicadores, status das integrações com Google e últimos check-ins.
- **Check-ins**: formulário multi-etapas, upload em lote e pré-visualização de fotos.
- **Registros**: tabela responsiva com filtros persistidos.
- **Galeria**: placeholders e layout para exibir imagens sincronizadas.
- **Administração**: gestão de promotores/PDVs e integrações.

---

## 🛠️ Tecnologias

- **Vue 3 (script setup + TypeScript)**
- **Vite 7** para bundling/dev server
- **Tailwind CSS 3.4** com design tokens customizados
- **Pinia** para estado global
- **Vue Router** para navegação declarativa
- **@tanstack/vue-query** para chamadas HTTP com cache e revalidação
- **Axios** como HTTP client
- **Vitest + Vue Test Utils** (unit)
- **Cypress 15** (E2E)

---

## 🚀 Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/marcelotorres1982/pdv-control.git
cd pdv-control/frontend

# 2. Variáveis de ambiente (apenas o frontend usa)
cp .env.example .env
# VITE_API_BASE_URL aponta para o seu serviço HTTP
# VITE_GOOGLE_OAUTH_URL (opcional) abre diretamente a tela de login do Google quando não houver backend

# 3. Dependências
npm install

# 4. Modo desenvolvimento
npm run dev
```

Scripts disponíveis:

| Script            | Descrição                                   |
|-------------------|---------------------------------------------|
| `npm run dev`     | Vite Dev Server (porta 5173 por padrão)     |
| `npm run build`   | Build de produção (`dist/`)                 |
| `npm run preview` | Servir o build local                        |
| `npm run test:unit` | Vitest                                    |
| `npm run test:e2e`   | Cypress com build                         |
| `npm run lint`    | ESLint + Prettier                           |

> Recomendado Node.js 20+. Se preferir pnpm ou yarn, adapte os comandos.
> Dica: defina `VITE_GOOGLE_OAUTH_URL` quando quiser testar o botão “Entrar com conta Google” sem uma API própria.

---

## 📁 Estrutura Essencial

```
pdv-control/
├── frontend/
│   ├── src/
│   │   ├── api/              # Clients Axios + tipagens
│   │   ├── components/
│   │   │   ├── base/         # Cartões, headers, feedback
│   │   │   └── layout/       # Shell, sidebar, header
│   │   ├── pages/            # Views do router
│   │   ├── stores/           # Pinia stores
│   │   ├── constants/        # Navegação, tokens, etc.
│   │   └── main.ts           # Bootstrap do app
│   ├── public/
│   ├── .env.example
│   ├── package.json
│   └── tailwind.config.js
└── docs/
    ├── architecture-vue-migration.md
    ├── INSTALL.md
    ├── QUICKSTART.md
    ├── CONTRIBUTING.md
    └── ...
```

---

## 🔌 Integrações e APIs

- `src/api/` define o contrato das rotas necessárias (`/checkins`, `/stats`, `/promoters`, `/google/status`, etc.).
- A SPA utiliza Axios + Vue Query; basta ajustar `VITE_API_BASE_URL` para apontar para o serviço escolhido (FastAPI, Node, Firebase, Supabase, Airtable, etc.).
- Componentes exibem mensagens amigáveis quando o endpoint não está disponível, mantendo a UI útil mesmo com dados mockados.

---

## 🤝 Contribuindo

1. Leia `docs/CONTRIBUTING.md` para entender o fluxo baseado em Node/Vite.
2. Crie uma branch seguindo `tipo/descricao-curta`.
3. Rode `npm run lint` e os testes relevantes antes do PR.
4. Atualize a documentação sempre que alterar comportamento visível ou contratos de API.

---

## 🗺️ Roadmap Próximo

- [ ] Integrar dados reais aos cards do Dashboard.
- [ ] Implementar busca/ordenação avançada nos Registros.
- [ ] Adicionar upload com arrastar-e-soltar e progresso visual.
- [ ] Finalizar a galeria com lightbox e filtros.
- [ ] Habilitar modo escuro usando Tailwind.
- [ ] Evoluir o shell para suportar notificações e atalhos.

---

## 📄 Licença & Contato

- Licença: MIT (`docs/MIT LICENSE.md`)
- Autor original: [Marcelo Torres](https://github.com/marcelotorres1982)
- Dúvidas ou sugestões: abra uma issue ou PR neste repositório.

Vamos evoluir juntos a nova experiência do PDV Control – agora 100% HTML, Tailwind e Vue. 💙
