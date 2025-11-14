# ⚡ Guia Rápido – PDV Control (Frontend Vue)

Suba o novo frontend em menos de 5 minutos.

---

## 1️⃣ Clonar e instalar

```bash
git clone https://github.com/marcelotorres1982/pdv-control.git
cd pdv-control/frontend
cp .env.example .env     # configure VITE_API_BASE_URL e, se quiser testar OAuth, VITE_GOOGLE_OAUTH_URL
npm install
```

---

## 2️⃣ Rodar em desenvolvimento

```bash
npm run dev
# Acesse http://localhost:5173
```

### Principais telas já disponíveis

- `/` – Dashboard (cards, status das integrações).
- `/checkins` – Formulário multi-etapas.
- `/registros` – Grid de registros com filtros.
- `/galeria` – Placeholder da galeria.
- `/admin` – Painel administrativo.

Cada tela está pronta para consumir as rotas mencionadas em `docs/architecture-vue-migration.md`.

---

## 3️⃣ Scripts úteis

```bash
npm run build      # gera dist/
npm run preview    # testa build localmente
npm run lint       # ESLint com auto-fix
npm run test:unit  # Vitest
npm run test:e2e   # Cypress
```

---

## 4️⃣ Conectar suas APIs

1. Garanta que seu serviço HTTP exponha os caminhos esperados (`/checkins`, `/stats/*`, `/promoters`, etc.).
2. Ajuste `VITE_API_BASE_URL` no `.env`.
3. Reinicie `npm run dev` e valide as chamadas via Vue Query Devtools.
4. Substitua dados mockados/comentados por respostas reais conforme integrar cada rota.

---

## 5️⃣ Fluxo recomendado para desenvolvimento

1. **Planejar**: abra/assine uma issue descrevendo a tarefa.
2. **Implementar**: componentize a UI e mantenha estados no Pinia/Vue Query.
3. **Validar**: rode `lint`, testes unitários e snapshot (quando aplicável).
4. **Documentar**: atualize `docs/` quando uma nova funcionalidade ficar pronta.

---

## 🙋 Ajuda

- Documentação detalhada: `docs/README.md` e `docs/INSTALL.md`
- Plano de migração: `docs/architecture-vue-migration.md`
- Fluxo de contribuição: `docs/CONTRIBUTING.md`

Bom hacking! 🚀
