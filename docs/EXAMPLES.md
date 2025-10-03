# 📚 Exemplos de Uso - PDV Control

Este documento contém exemplos práticos de como usar o sistema PDV Control.

---

## 🎯 Cenários de Uso

### Cenário 1: Check-in Simples

**Situação**: Promotor João faz visita ao Supermercado Central

**Passos**:
1. Abrir o aplicativo
2. Selecionar "📝 Novo Check-in"
3. Preencher:
   - **Promotor**: João Silva
   - **PDV**: Supermercado Central
   - **Valor Deslocamento**: R$ 50,00
   - **Número de Entradas**: 1
4. Fazer upload de 3 fotos do PDV
5. Clicar em "✅ Confirmar Check-in"

**Resultado**: Check-in registrado com sucesso, fotos enviadas para o Drive

---

### Cenário 2: Múltiplas Entradas no Mesmo PDV

**Situação**: Promotora Maria faz 3 visitas no mesmo dia ao mesmo PDV

**Passos**:
1. No campo **Número de Entradas**, selecionar: **3**
2. O valor do deslocamento será contabilizado apenas uma vez
3. Upload de fotos de todas as visitas

**Dica**: Use este recurso quando fizer múltiplas visitas ao mesmo local no mesmo dia

---

### Cenário 3: Consultar Histórico por Promotor

**Situação**: Gerente quer ver todas as visitas do promotor Carlos

**Passos**:
1. Ir em "📊 Ver Registros"
2. No filtro **Promotor**, selecionar: Carlos Mendes
3. Visualizar todos os check-ins, valores e fotos

**Recursos disponíveis**:
- Total de visitas
- Valor total de deslocamento
- Número total de entradas
- Links para todas as fotos

---

### Cenário 4: Relatório Mensal

**Situação**: Precisa gerar relatório do mês para prestação de contas

**Passos**:
1. Ir em "📊 Ver Registros"
2. Aplicar filtros:
   - **Data**: Selecionar intervalo do mês
   - **Promotor**: Todos
3. Visualizar estatísticas:
   - Total gasto com deslocamento
   - Número de visitas
   - PDVs visitados

---

## 💡 Dicas e Truques

### Organização de Fotos

As fotos são automaticamente organizadas no Google Drive seguindo esta estrutura:

```
PDV Control/
└── João Silva/
    └── 2025-10-01/
        ├── Supermercado_Central_001.jpg
        ├── Supermercado_Central_002.jpg
        └── Supermercado_Central_003.jpg
```

### Nomenclatura Padronizada

O sistema cria nomes automáticos para as fotos:
- **Formato**: `{NOME_DO_PDV}_{NÚMERO}.jpg`
- **Exemplo**: `Farmacia_Popular_001.jpg`

### Sincronização com Google Sheets

Cada check-in é automaticamente adicionado à planilha com:
- Data e hora do check-in
- Nome do promotor
- PDV visitado
- Valor do deslocamento
- Número de entradas
- Links diretos para as fotos no Drive

---

## 📊 Casos de Uso Avançados

### Uso 1: Múltiplos Promotores

**Cenário**: Equipe de 5 promotores usando o mesmo sistema

**Configuração**:
1. Editar `config.py`
2. Adicionar todos os promotores na lista `PROMOTORES`
3. Cada promotor terá sua própria pasta no Drive
4. Relatórios podem filtrar por promotor específico

### Uso 2: Grande Volume de PDVs

**Cenário**: 50+ PDVs cadastrados

**Dicas**:
- Use a busca no seletor de PDV
- Digite as primeiras letras para filtrar
- Organize os PDVs por região no arquivo `config.py`

**Exemplo de organização**:

```python
PDVS = [
    # Zona Norte
    "Supermercado Norte 1",
    "Supermercado Norte 2",
    
    # Zona Sul
    "Supermercado Sul 1",
    "Supermercado Sul 2",
    
    # Centro
    "Farmácia Centro",
    # ...
]
```

### Uso 3: Controle de Custo

**Cenário**: Monitorar gastos mensais com deslocamento

**Processo**:
1. Acessar "📊 Ver Registros"
2. Filtrar por mês desejado
3. Visualizar **Total Deslocamento** no card estatístico
4. Exportar dados para análise externa (se necessário)

---

## 🔄 Fluxo de Trabalho Recomendado

### Rotina Diária do Promotor

**Manhã**:
1. ✅ Abrir o PDV Control
2. ✅ Verificar PDVs agendados para o dia
3. ✅ Confirmar conexão com Google Drive

**Durante Visitas**:
1. ✅ Ao chegar no PDV, fazer check-in
2. ✅ Tirar fotos necessárias (prateleiras, produtos, etc.)
3. ✅ Fazer upload imediato das fotos
4. ✅ Adicionar observações relevantes

**Fim do Dia**:
1. ✅ Revisar todos os check-ins do dia
2. ✅ Verificar se todas as fotos foram enviadas
3. ✅ Confirmar sincronização com Google Sheets

### Rotina Semanal do Gestor

**Segunda-feira**:
1. ✅ Revisar check-ins da semana anterior
2. ✅ Validar gastos com deslocamento
3. ✅ Verificar cobertura de PDVs

**Sexta-feira**:
1. ✅ Gerar relatório semanal
2. ✅ Planejar visitas da próxima semana
3. ✅ Backup dos dados importantes

---

## 📸 Boas Práticas para Fotos

### O Que Fotografar

✅ **Recomendado**:
- Fachada do PDV (para identificação)
- Prateleiras com produtos
- Displays e materiais promocionais
- Áreas de exposição
- Problemas identificados (estoque, organização)

❌ **Evitar**:
- Fotos desfocadas
- Imagens muito escuras
- Fotos sem contexto
- Informações confidenciais

### Qualidade das Fotos

- **Resolução**: Média a alta (para upload rápido)
- **Iluminação**: Natural quando possível
- **Ângulo**: Frontal e nítido
- **Quantidade**: 3-5 fotos por visita (ideal)

---

## 🎓 Exemplos de Dados

### Exemplo de Registro Completo

```json
{
  "data": "2025-10-01",
  "hora": "14:30:00",
  "promotor": "João Silva",
  "pdv": "Supermercado Central",
  "valor_deslocamento": 50.00,
  "num_entradas": 1,
  "observacoes": "Estoque completo, boa organização",
  "fotos": [
    "https://drive.google.com/file/d/.../view",
    "https://drive.google.com/file/d/.../view",
    "https://drive.google.com/file/d/.../view"
  ]
}
```

### Exemplo de Estatísticas Mensais

```
📊 Estatísticas de Setembro/2025

👤 João Silva:
   • Total de Visitas: 22
   • Total Deslocamento: R$ 1.100,00
   • PDVs Visitados: 15
   • Fotos Enviadas: 66

👤 Maria Santos:
   • Total de Visitas: 18
   • Total Deslocamento: R$ 900,00
   • PDVs Visitados: 12
   • Fotos Enviadas: 54

💰 Total Geral: R$ 2.000,00
📍 Total de Visitas: 40
```

---

## 🚨 Situações Especiais

### Problema: Sem Conexão com Internet

**Solução**: 
- Os dados são salvos localmente em `data/local_backup.json`
- Quando a conexão retornar, use "🔄 Sincronizar Dados" nas configurações

### Problema: PDV Não Cadastrado

**Solução**:
- Na tela de check-in, há campo para digitar novo PDV
- Ou adicione permanentemente em `config.py`

### Problema: Erro ao Enviar Fotos

**Solução**:
1. Verificar tamanho das fotos (max 10MB cada)
2. Verificar conexão com Google Drive
3. Tentar novamente
4. Se persistir, salvar fotos localmente e enviar depois

---

## 📈 Métricas de Sucesso

### KPIs Sugeridos

- **Cobertura**: % de PDVs visitados no período
- **Frequência**: Média de visitas por PDV
- **Custo**: Custo médio por visita
- **Documentação**: % de visitas com fotos

### Metas Exemplo

```
✅ Meta Mensal:
   • Visitar 100% dos PDVs prioritários
   • Manter custo médio abaixo de R$ 60/visita
   • 100% das visitas com mínimo 3 fotos
   • Upload imediato em 95% dos casos
```

---

## 💬 Perguntas Frequentes

**P: Posso usar offline?**  
R: Sim! Os dados são salvos localmente e sincronizados quando houver conexão.

**P: Quantas fotos posso enviar?**  
R: Até 20 fotos por check-in, máximo 10MB cada.

**P: Como compartilhar relatórios?**  
R: Os dados estão no Google Sheets, basta compartilhar a planilha.

**P: Posso deletar check-ins?**  
R: Atualmente não há função de deletar pela interface, mas você pode remover diretamente da planilha.

**P: Os dados são seguros?**  
R: Sim! Usa autenticação OAuth do Google e os dados ficam na sua conta.

---

## 🎯 Próximos Passos

Depois de dominar o básico:

1. 📊 Explore filtros avançados nos relatórios
2. 🔄 Configure sincronização automática
3. 📱 Teste em diferentes dispositivos
4. 👥 Treine outros usuários da equipe
5. 📈 Analise tendências nos dados coletados

---

**💡 Dica Final**: Mantenha uma rotina consistente de check-ins e documentação fotográfica para maximizar o valor do sistema!

---

**Desenvolvido com ❤️ por Marcelo Torres**

📧 marcelotorres1982@gmail.com  
🐙 [GitHub](https://github.com/marcelotorres1982)