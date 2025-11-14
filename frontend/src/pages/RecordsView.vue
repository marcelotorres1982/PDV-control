<script setup lang="ts">
import { computed, onMounted, reactive } from 'vue'
import { useQuery } from '@tanstack/vue-query'
import PageHeader from '@/components/base/PageHeader.vue'
import AppCard from '@/components/base/AppCard.vue'
import { listCheckins } from '@/api/checkins'
import { listPromoters } from '@/api/promoters'
import { listPdvs } from '@/api/pdvs'

const filters = reactive({
  startDate: '',
  endDate: '',
  promotorId: '',
  pdvId: '',
})

const { data: promoters } = useQuery({
  queryKey: ['promoters'],
  queryFn: listPromoters,
})
const { data: pdvs } = useQuery({
  queryKey: ['pdvs'],
  queryFn: listPdvs,
})

const fetchCheckins = () =>
  listCheckins({
    startDate: filters.startDate || undefined,
    endDate: filters.endDate || undefined,
    promotorId: filters.promotorId || undefined,
    pdvId: filters.pdvId || undefined,
  })

const {
  data: checkinsData,
  refetch,
  isFetching,
  isError,
} = useQuery({
  queryKey: ['checkins'],
  queryFn: fetchCheckins,
  enabled: false,
})

const checkins = computed(() => checkinsData.value ?? [])
const promoterOptions = computed(() => promoters.value ?? [])
const pdvOptions = computed(() => pdvs.value ?? [])
const currency = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' })

const applyFilters = () => refetch()
const clearFilters = () => {
  Object.assign(filters, { startDate: '', endDate: '', promotorId: '', pdvId: '' })
  refetch()
}

onMounted(() => {
  refetch()
})
</script>

<template>
  <section>
    <PageHeader
      title="Registros"
      description="Filtre check-ins por período, promotor e PDV. As fotos exibem a quantidade sincronizada no Google Drive."
    />

    <AppCard padding="lg">
      <form class="grid gap-4 md:grid-cols-4" @submit.prevent="applyFilters">
        <label class="text-sm text-slate-600">
          Início
          <input
            v-model="filters.startDate"
            type="date"
            class="mt-1 w-full rounded-2xl border border-slate-200 px-4 py-2 text-sm focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
          />
        </label>
        <label class="text-sm text-slate-600">
          Fim
          <input
            v-model="filters.endDate"
            type="date"
            class="mt-1 w-full rounded-2xl border border-slate-200 px-4 py-2 text-sm focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
          />
        </label>
        <label class="text-sm text-slate-600">
          Promotor
          <select
            v-model="filters.promotorId"
            class="mt-1 w-full rounded-2xl border border-slate-200 px-4 py-2 text-sm focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
          >
            <option value="">Todos</option>
            <option v-for="option in promoterOptions" :key="option.id" :value="option.id">
              {{ option.nome }}
            </option>
          </select>
        </label>
        <label class="text-sm text-slate-600">
          PDV
          <select
            v-model="filters.pdvId"
            class="mt-1 w-full rounded-2xl border border-slate-200 px-4 py-2 text-sm focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
          >
            <option value="">Todos</option>
            <option v-for="option in pdvOptions" :key="option.id" :value="option.id">
              {{ option.nome }}
            </option>
          </select>
        </label>
        <div class="flex flex-wrap gap-3 md:col-span-4">
          <button
            type="submit"
            class="rounded-2xl bg-brand px-4 py-2 text-sm font-semibold text-white hover:bg-brand-dark disabled:opacity-60"
            :disabled="isFetching"
          >
            {{ isFetching ? 'Filtrando...' : 'Aplicar filtros' }}
          </button>
          <button
            type="button"
            class="rounded-2xl border border-slate-200 px-4 py-2 text-sm font-semibold text-slate-600 hover:text-slate-900"
            @click="clearFilters"
          >
            Limpar
          </button>
        </div>
      </form>

      <div class="mt-6 overflow-hidden rounded-3xl border border-slate-100">
        <div
          class="hidden bg-slate-50 px-4 py-3 text-xs font-semibold uppercase tracking-wider text-slate-500 md:grid md:grid-cols-[120px,120px,1fr,1fr,120px,90px,90px]"
        >
          <span>Data</span>
          <span>Hora</span>
          <span>Promotor</span>
          <span>PDV</span>
          <span>Deslocamento</span>
          <span>Entradas</span>
          <span>Fotos</span>
        </div>
        <ul v-if="checkins.length">
          <li
            v-for="row in checkins"
            :key="row.id"
            class="grid gap-3 border-t border-slate-100 px-4 py-4 text-sm md:grid-cols-[120px,120px,1fr,1fr,120px,90px,90px]"
          >
            <span>{{ new Date(row.data).toLocaleDateString() }}</span>
            <span>{{ row.hora }}</span>
            <span class="font-medium text-slate-900">{{ row.promotorNome }}</span>
            <span>{{ row.pdvNome }}</span>
            <span>{{ currency.format(row.valorDeslocamento ?? 0) }}</span>
            <span>{{ row.numEntradas ?? 1 }}</span>
            <span>{{ row.fotos?.length ?? 0 }}</span>
          </li>
        </ul>
        <div
          v-else
          class="p-6 text-center text-sm text-slate-500"
        >
          {{ isError ? 'Não foi possível carregar os registros.' : isFetching ? 'Carregando...' : 'Nenhum check-in encontrado.' }}
        </div>
      </div>
    </AppCard>
  </section>
</template>
