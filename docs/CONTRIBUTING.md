# 🤝 Guia de Contribuição – PDV Control (Vue + Tailwind)

Obrigado por ajudar a construir a nova fase do PDV Control! Este documento descreve o fluxo para contribuir com a versão em **Vue 3 + Vite + Tailwind**, totalmente independente de backend.

---

## 📋 Índice

1. [Princípios e Código de Conduta](#princípios-e-código-de-conduta)
2. [Visão geral do fluxo](#visão-geral-do-fluxo)
3. [Configurando o ambiente](#configurando-o-ambiente)
4. [Padrões de código](#padrões-de-código)
5. [Checklist de pull requests](#checklist-de-pull-requests)
6. [Reportando bugs e sugerindo melhorias](#reportando-bugs-e-sugerindo-melhorias)

---

## 🌱 Princípios e Código de Conduta

Mantemos um ambiente colaborativo com foco em:

- Respeito e comunicação clara.
- Feedback construtivo.
- Transparência em decisões técnicas.
- Documentação atualizada para cada mudança relevante.

Ao contribuir, siga o [Contributor Covenant](https://www.contributor-covenant.org/) como referência.

---

## 🔁 Visão geral do fluxo

1. **Abra uma issue** descrevendo o problema/feature (caso ainda não exista).
2. **Crie uma branch** a partir de `main` com o formato `tipo/descritivo-curto` (ex.: `feat/checkin-form`).
3. **Implemente** seguindo os padrões descritos abaixo.
4. **Rode lint e testes** antes de abrir o PR.
5. **Abra o PR** referenciando a issue e descrevendo mudanças + screenshots/gifs quando pertinente.

Tipos de branch sugeridos: `feat/`, `fix/`, `chore/`, `docs/`, `refactor/`, `test/`.

---

## 💻 Configurando o ambiente

```bash
git clone https://github.com/marcelotorres1982/pdv-control.git
cd pdv-control/frontend
cp .env.example .env       # ajuste VITE_API_BASE_URL se necessário
npm install

# Servidor de desenvolvimento
npm run dev
```

Outros scripts úteis:

- `npm run lint` – ESLint (com auto-fix).
- `npm run test:unit` – Vitest.
- `npm run test:e2e` – Cypress (requer build/preview).
- `npm run build` – gera `dist/`.

---

## 🧑‍💻 Padrões de código

### Estilo

- Utilize **TypeScript** sempre que possível.
- Componentes em `<script setup>` com `lang="ts"`.
- CSS via **Tailwind**. Caso precise de estilos adicionais, use `@layer` nos arquivos em `src/assets/`.
- Nomeie componentes com o sufixo `*View.vue` (páginas) e `*Card.vue`/`*Section.vue` (componentes).

### Estrutura

- `src/api/` – clients Axios + tipagens.
- `src/stores/` – Pinia stores (um arquivo por domínio).
- `src/pages/` – views conectadas ao router.
- `src/components/base/` – componentes genéricos reutilizáveis.

### Lint e formatação

- ESLint já está configurado para Vue + TypeScript.
- Prettier roda automaticamente no VS Code (veja `.vscode/settings.json`).
- Antes de comitar, execute `npm run lint` e `npm run test:unit`.

### Commits (Conventional Commits)

Use prefixos como `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `test:`. Exemplos:

```
feat: adiciona grid responsivo na página de registros
fix: corrige fallback do PageHeader sem meta
```

---

## ✅ Checklist de Pull Requests

- [ ] Issue relacionada mencionada no PR.
- [ ] `npm run lint` executado sem erros.
- [ ] `npm run test:unit` (e2e quando aplicável) executado.
- [ ] Screenshots/GIFs anexados quando houver mudanças visuais.
- [ ] Documentação atualizada (`docs/*.md` ou comentários no código) quando necessário.
- [ ] Descreveu pontos de atenção/impactos em outras áreas.

---

## 🐞 Reportando bugs e sugerindo melhorias

1. **Bugs**
   - Descreva os passos para reproduzir.
   - Informe o ambiente (SO, navegador, versão do Node).
   - Anexe logs/prints quando possível.

2. **Melhorias / Features**
   - Contextualize o problema que deseja resolver.
   - Proponha uma solução inicial (wireframes, fluxos ou comportamento esperado).
   - Indique dependências com APIs externas/Google, se houver.

Use o template de issues no GitHub e marque com as labels `bug`, `enhancement`, `documentation`, etc.

---

## 🙌 Obrigado!

Cada PR/issue aproxima o PDV Control da melhor experiência possível com HTML, Tailwind e Vue. Acompanhe o plano em `docs/architecture-vue-migration.md` e fique à vontade para sugerir ajustes. Vamos construir juntos! 💙
