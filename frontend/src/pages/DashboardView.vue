<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { CheckBadgeIcon, ExclamationTriangleIcon } from '@heroicons/vue/24/outline'
import PageHeader from '@/components/base/PageHeader.vue'
import StatCard from '@/components/base/StatCard.vue'
import AppCard from '@/components/base/AppCard.vue'

const router = useRouter()

const statCards = [
  { label: 'Registros', value: '0', helper: 'Integraçao em andamento', trend: undefined },
  { label: 'Promotores ativos', value: '0', helper: 'Sincronize para atualizar' },
  { label: 'PDVs monitorados', value: '0', helper: 'Importe dados ou cadastre novos' },
  { label: 'Fotos no Drive', value: '0', helper: 'Upload via check-in' },
]

const recentCheckins = [
  { id: '1', promotor: 'Em breve', pdv: 'Integraçao pendente', hora: '—', status: 'Aguardando API' },
]

const integrationAlerts = computed(() => [
  {
    id: 'drive',
    label: 'Google Drive',
    status: 'Configuraçao pendente',
    description: 'Crie as credenciais OAuth e conecte o serviço que fará o upload.',
    icon: ExclamationTriangleIcon,
  },
  {
    id: 'sheets',
    label: 'Google Sheets',
    status: 'Configuraçao pendente',
    description: 'Defina a planilha alvo para sincronizar registros.',
    icon: ExclamationTriangleIcon,
  },
])
</script>

<template>
  <section>
    <PageHeader
      title="Visao geral"
      description="Configure suas APIs e conecte o Google Workspace. Os cards abaixo refletem o que sera exibido quando os endpoints de check-ins e estatisticas estiverem ativos."
      :meta="[
        { label: 'Status da API', value: 'Em implementaçao' },
        { label: 'Google Workspace', value: 'Nao conectado' },
      ]"
    >
      <template #actions>
        <button
          class="inline-flex items-center rounded-2xl bg-brand px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-brand-dark"
          @click="router.push('/checkins')"
        >
          Registrar agora
        </button>
      </template>
    </PageHeader>

    <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
      <StatCard v-for="card in statCards" :key="card.label" v-bind="card" />
    </div>

    <div class="mt-8 grid gap-6 lg:grid-cols-2">
      <AppCard title="Ultimos check-ins" subtitle="Fluxo pronto para consumir sua API">
        <ul class="divide-y divide-slate-100">
          <li v-for="checkin in recentCheckins" :key="checkin.id" class="flex items-center justify-between py-3">
            <div>
              <p class="font-medium text-slate-900">{{ checkin.promotor }}</p>
              <p class="text-sm text-slate-500">{{ checkin.pdv }}</p>
            </div>
            <span class="text-xs font-medium text-slate-500">{{ checkin.hora }}</span>
            <span class="rounded-full border border-amber-200 bg-amber-50 px-3 py-1 text-xs font-semibold text-amber-700">
              {{ checkin.status }}
            </span>
          </li>
        </ul>
      </AppCard>

      <AppCard title="Integraçao Google" subtitle="Checklist para finalizar integraçoes">
        <ul class="space-y-4">
          <li
            v-for="alert in integrationAlerts"
            :key="alert.id"
            class="flex gap-3 rounded-2xl border border-slate-100 p-3"
          >
            <component
              :is="alert.icon"
              class="h-6 w-6 flex-shrink-0 text-amber-500"
            />
            <div>
              <p class="font-medium text-slate-900">{{ alert.label }}</p>
              <p class="text-sm text-slate-500">{{ alert.description }}</p>
              <span class="mt-2 inline-flex rounded-full bg-amber-100 px-2.5 py-0.5 text-xs font-semibold text-amber-700">
                {{ alert.status }}
              </span>
            </div>
          </li>
          <li class="rounded-2xl border border-emerald-200 bg-emerald-50 p-4 text-sm text-emerald-800 flex items-start gap-3">
            <CheckBadgeIcon class="h-5 w-5 flex-shrink-0" />
            <span>Quando conectar sua API a este frontend, os alertas acima serao atualizados automaticamente.</span>
          </li>
        </ul>
      </AppCard>
    </div>
  </section>
</template>
