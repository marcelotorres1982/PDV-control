# 📚 Exemplos de Uso – Nova Interface PDV Control

Mesmo antes de uma API real estar pronta, o frontend já espelha os fluxos reais que serão atendidos. Use estes cenários como referência para conectar dados e validar UX.

---

## 🎯 Cenário 1 – Check-in guiado

**Objetivo:** permitir que o promotor selecione promotor/PDV, informe deslocamento, observações e envie fotos.

1. Navegue para `/checkins`.
2. A etapa **“Dados do promotor”** consumirá `GET /api/promotores` e `GET /api/pdvs` para preencher os selects.
3. A etapa **“Detalhes da visita”** armazena data, hora, valor e entradas.
4. A etapa **“Comprovantes”** enviará arquivos via `POST /api/checkins` (multipart), que encaminhará os uploads ao Google Drive.

**Integração necessária:** `src/api/checkins.ts` (funções `listCheckins` e `createCheckin`) + o serviço HTTP responsável por processar uploads.

---

## 📊 Cenário 2 – Controle diário do gestor

**Objetivo:** dar visibilidade das visitas realizadas e estatísticas globais.

1. Na rota `/` (Dashboard) os cards `StatCard` devem consumir `GET /api/stats/overview`.
2. A tabela “Últimos check-ins” consumirá `GET /api/checkins?limit=5`.
3. O painel “Integração Google” consome `GET /api/google/status` exibindo links para Drive/Sheets e o horário da última sincronização.

**Integrações sugeridas:** endpoints `stats` e `google` documentados em `architecture-vue-migration.md`.

---

## 🗂️ Cenário 3 – Consulta avançada de registros

**Objetivo:** permitir filtros combinados e exportação.

1. Em `/registros`, cada filtro controla parâmetros (`promotorId`, `pdvId`, `startDate`, `endDate`).
2. O serviço deve suportar paginação (`page`, `pageSize`), ordenação e exportação (`POST /api/export/csv`), retornando uma URL temporária.
3. A UI mostra uma tabela responsiva; considere usar uma lib de virtualização quando o volume de dados crescer.

---

## 🖼️ Cenário 4 – Galeria de fotos

**Objetivo:** navegar rapidamente pelas evidências de execução.

1. `/galeria` apresenta filtros rápidos (Hoje, Semana, Mês).
2. Ao integrar, alimente o grid com `GET /api/checkins?hasPhotos=true` ou um endpoint dedicado a mídias.
3. Cada card precisa das miniaturas (geradas pelo serviço escolhido) e do link direto para o arquivo no Drive.
4. Um modal/lightbox pode ser aberto com metadados adicionais.

---

## ⚙️ Cenário 5 – Administração

**Objetivo:** manter promotores, PDVs e integrações em dia.

1. `/admin` consome `GET/POST/PUT/DELETE /api/promotores` e `/api/pdvs`.
2. Botões “Configurar OAuth” e “Sincronizar agora” acionam `POST /api/google/sync`.
3. Mostre alertas usando o componente `EmptyState` sempre que não houver dados.

---

## 💡 Boas práticas para integrar os cenários

- Centralize chamadas HTTP em `src/api/` e exponha hooks/composables reutilizáveis.
- Prefira **Pinia** para estados compartilhados (ex.: listas de promotores) e **Vue Query** para dados cacheáveis.
- Trate erros de rede exibindo banners/toasts no layout principal.
- Use Skeletons/Loading states para manter a experiência fluida enquanto os dados carregam.

Esses cenários representam a transição planejada do Streamlit para uma SPA moderna. Ao conectar cada etapa aos endpoints HTTP da sua preferência, o PDV Control terá a mesma cobertura funcional, porém com UX superior.***
