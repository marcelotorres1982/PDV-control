<script setup lang="ts">
import PageHeader from '@/components/base/PageHeader.vue'
import AppCard from '@/components/base/AppCard.vue'
import EmptyState from '@/components/feedback/EmptyState.vue'

const galleryFilters = ['Todos', 'Hoje', 'Esta semana', 'Este mes']
</script>

<template>
  <section>
    <PageHeader
      title="Galeria"
      description="Fotos enviadas pelos promotores ficarao visiveis aqui. Cada card deve apontar para o arquivo no Google Drive retornado pela API."
    />

    <AppCard>
      <div class="flex flex-wrap gap-3">
        <button
          v-for="filter in galleryFilters"
          :key="filter"
          class="rounded-2xl border border-slate-200 px-4 py-2 text-sm font-medium text-slate-600 hover:border-brand hover:text-brand"
        >
          {{ filter }}
        </button>
      </div>

      <div class="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <EmptyState
          title="Nenhuma foto carregada"
          description="Assim que os check-ins forem integrados, exibiremos thumbnails com links diretos para o Google Drive."
        />
      </div>
    </AppCard>
  </section>
</template>
