# 📁 Estrutura do Projeto – PDV Control (Vue Edition)

Com a remoção definitiva do app Streamlit/Python, o repositório passou a concentrar apenas o frontend moderno em Vue + Tailwind e a documentação associada. Este documento descreve cada pasta/arquivo relevante.

---

## 🗂️ Visão geral

```
pdv-control/
├── frontend/                 # Aplicação Vue 3 + Tailwind + Vite
│   ├── src/
│   │   ├── api/              # Clients Axios + tipagens
│   │   ├── assets/           # Tailwind + estilos base
│   │   ├── components/
│   │   │   ├── base/         # Cartões, headers, empty states
│   │   │   └── layout/       # Shell, sidebar, header
│   │   ├── pages/            # Views conectadas ao router
│   │   ├── stores/           # Pinia stores (ex.: UI store)
│   │   ├── constants/        # Navegação, tokens, etc.
│   │   └── main.ts           # Bootstrap do app
│   ├── public/
│   ├── .env.example
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.ts
├── docs/                     # Documentação atualizada
│   ├── README.md             # Visão geral da SPA
│   ├── INSTALL.md            # Guia de instalação (Node/Vite)
│   ├── QUICKSTART.md         # Onboarding em 5 passos
│   ├── EXAMPLES.md           # Cenários de uso (frontend)
│   ├── CONTRIBUTING.md       # Fluxo de contribuição
│   ├── STRUCTURE.md          # Este documento
│   ├── architecture-vue-migration.md # Plano completo da migração
│   └── MIT LICENSE.md
├── .devcontainer/            # Configuração Codespaces/Dev Containers (Node)
├── .gitignore                # Regras focadas em Node/Vite
└── PROJECT RESUME.md         # Resumo executivo atualizado
```

> Qualquer implementação de API fica fora deste repositório. Basta apontar `VITE_API_BASE_URL` para o serviço da sua preferência.

---

## 🧱 Detalhes do frontend

### `src/api/`
- `client.ts`: instancia Axios configurado com `VITE_API_BASE_URL`.
- `checkins.ts`, `stats.ts`, etc.: wrappers das rotas REST.
- `types.ts`: tipagens compartilhadas entre módulos.

### `src/components/`
- `layout/`: `AppShell`, `AppSidebar`, `AppHeader`.
- `base/`: `AppCard`, `PageHeader`, `StatCard`.
- `feedback/`: componentes como `EmptyState`.

### `src/pages/`
- `DashboardView.vue`, `CheckinView.vue`, `RecordsView.vue`, `GalleryView.vue`, `AdminView.vue`, `NotFoundView.vue`.
- Cada view já contém placeholders explicando quais endpoints alimentarão os dados.

### `src/stores/`
- `ui.ts`: controla elementos globais (sidebar, etc.).
- Novos stores devem seguir o padrão `defineStore` com TypeScript.

### Configuração
- `tailwind.config.js`: tokens de cor, fontes e sombras padrão.
- `postcss.config.js`: pipeline Tailwind + Autoprefixer.
- `vite.config.ts`: alias `@` → `src` e plugin Vue.

---

## 🧾 Documentação suplementar

- `docs/architecture-vue-migration.md` traz a visão completa da arquitetura Vue, módulos e expectativas de integração.
- `PROJECT RESUME.md` resume o estado atual do projeto para stakeholders.

---

## 🔜 Próximos diretórios planejados

| Pasta      | Descrição                                                                 |
|------------|----------------------------------------------------------------------------|
| `infra/`   | Scripts de deploy, automações de build ou pipelines para a SPA.            |
| `integrations/` | Arquivos auxiliares (mock servers, contratos, SDKs) caso sejam versionados. |

Quando novos módulos forem adicionados, este documento será atualizado para refletir a organização estendida. Enquanto isso, todo o foco está na SPA Vue e na documentação de referência.***
