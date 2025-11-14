# PDV Control 2.0 – Arquitetura da SPA Vue + Tailwind

Este documento descreve a arquitetura de referência da interface do PDV Control. Todo o código reside no frontend; qualquer serviço de dados pode ser conectado via HTTP, desde que respeite os contratos de `src/api/`.

---

## Objetivos da migração
- Oferecer uma experiência moderna, responsiva e acessível para promotores e gestores.
- Padronizar o design system usando Tailwind + tokens de cor.
- Organizar o código em camadas claras (UI, estado, dados) usando Vue 3 com TypeScript.
- Permitir que diferentes APIs/serviços possam ser plugados sem alterações profundas.

---

## Visão geral
```
Vue 3 SPA (Vite + Tailwind + Pinia + Vue Router + Vue Query)
        ↕ HTTP/JSON (Axios)
Serviço(s) de dados externos (stack livre)
        ↔ Integrações Google Drive/Sheets ou qualquer outro provider
```

- O repositório mantém apenas a camada Vue.
- `src/api` concentra os clients Axios e tipagens.
- Vue Query orquestra cache, estados de carregamento e invalidation.
- Pinia guarda estados globais (UI, filtros, usuário autenticado).

---

## Camadas do frontend

| Camada / Pasta             | Responsabilidade                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| `src/pages`               | Views conectadas ao router (Dashboard, Check-ins, Registros, Galeria, Admin).    |
| `src/components/layout`   | `AppShell`, `AppSidebar`, `AppHeader`, grid responsivo.                          |
| `src/components/base`     | Cartões, cabeçalhos, estados vazios, componentes reutilizáveis.                  |
| `src/api`                 | Clients Axios + tipagens (`checkins`, `stats`, `promoters`, `pdvs`, `google`).    |
| `src/stores`              | Pinia stores para UI e fluxos compartilhados.                                     |
| `src/constants`           | Navegação, cores, breakpoints e tokens.                                           |
| `src/assets`              | Estilos base Tailwind (layers, fontes, resets).                                  |
| `src/router`              | Definição das rotas + lazy loading.                                               |

---

## Fluxo de Check-in (exemplo)
1. Usuário acessa `/checkins`.
2. Vue Query dispara `listPromoters` e `listPdvs`.
3. O formulário multi-etapas usa `reactive` + `computed` para manter estado local.
4. Ao enviar, `createCheckin` monta `FormData` (dados + fotos) e envia para o endpoint configurado.
5. Em caso de sucesso, o cache `['checkins']` é invalidado para atualizar o Dashboard/Registros.

> Enquanto não houver API, o botão exibe feedback visual e os dados permanecem no estado local.

---

## Estrutura das APIs esperadas

| Método | Rota                   | Descrição / payload esperado                                  |
|--------|-----------------------|----------------------------------------------------------------|
| `POST` | `/checkins`           | Dados do formulário + fotos (`multipart/form-data`).          |
| `GET`  | `/checkins`           | Lista paginada com filtros (`promotorId`, `pdvId`, datas).    |
| `GET`  | `/stats/overview`     | Totais e indicadores usados nos `StatCard`.                   |
| `GET`  | `/stats/promoters`    | Métricas por promotor/PDV.                                    |
| `GET`  | `/promoters`          | Listagem de promotores ativos.                                |
| `GET`  | `/pdvs`               | Listagem de pontos de venda.                                  |
| `POST` | `/google/sync`        | Aciona sincronização com Drive/Sheets (opcional).             |
| `GET`  | `/google/status`      | Status das integrações, últimos uploads, links úteis.         |

- A tecnologia usada para expor essas rotas é livre (Node, FastAPI, Firebase, Supabase, etc.).
- Em ambientes sem API, utilize mocks, interceptores Axios ou serviços como [Mock Service Worker](https://mswjs.io/).

---

## Styling & UX

- Tailwind configurado com tokens (`brand`, `brand-dark`, tons de cinza, sombras e espaçamentos).
- Componentes base encapsulam padrões visuais — evite duplicar classes.
- O layout responde bem de mobile a desktop, com colunas configuradas em CSS Grid.
- Recomenda-se adicionar dark mode usando `data-theme` e variantes `dark:` do Tailwind.

---

## Estado e dados

- **Pinia**: mantém estados globais (ex.: `uiStore` para controlar sidebar, dimensões, preferências).
- **Vue Query**: cuida de `loading`, `error`, invalidação e revalidação automática.
- **Local Storage**: pode ser utilizado para persistir filtros e preferências (não implementado por padrão).

---

## Estratégia de migração
1. Recriar cada fluxo antigo (Dashboard, Check-in, Registros, Admin) como páginas Vue.
2. Implementar componentes base e tokens antes de telas específicas.
3. Conectar gradualmente às APIs verdadeiras conforme ficarem disponíveis.
4. Adicionar testes unitários (Vitest) para componentes críticos.
5. Automatizar testes E2E (Cypress) para fluxos como “registrar check-in” e “filtrar registros”.

---

## Pendências / decisões abertas
- Definir proveedor oficial dos dados (API proprietária, BaaS, planilhas + middleware).
- Escolher estratégia de autenticação no frontend.
- Implementar upload com barra de progresso e feedback em tempo real.
- Documentar contratos de API com OpenAPI ou JSON Schemas para facilitar integrações.

Este blueprint serve como referência para manter a SPA organizada, independente de qual serviço de dados seja utilizado.***
