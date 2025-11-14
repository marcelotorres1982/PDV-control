<script setup lang="ts">
import { computed, reactive } from 'vue'
import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query'
import PageHeader from '@/components/base/PageHeader.vue'
import AppCard from '@/components/base/AppCard.vue'
import EmptyState from '@/components/feedback/EmptyState.vue'
import { listPromoters, createPromoter, deletePromoter } from '@/api/promoters'
import { listPdvs, createPdv, deletePdv } from '@/api/pdvs'
import { fetchGoogleStatus, triggerSync } from '@/api/google'
import { useAuthStore } from '@/stores/auth'

const queryClient = useQueryClient()
const auth = useAuthStore()
const isAuthenticated = computed(() => auth.isAuthenticated)

const promoterForm = reactive({
  nome: '',
  documento: '',
  telefone: '',
  ativo: true,
})

const pdvForm = reactive({
  nome: '',
  cidade: '',
  estado: '',
  codigo: '',
  ativo: true,
})

const { data: promoters } = useQuery({
  queryKey: ['promoters'],
  queryFn: listPromoters,
})

const { data: pdvs } = useQuery({
  queryKey: ['pdvs'],
  queryFn: listPdvs,
})

const { data: googleStatus, refetch: refetchGoogle, isFetching: googleLoading } = useQuery({
  queryKey: ['google-status'],
  queryFn: fetchGoogleStatus,
  retry: false,
})
const isGoogleLoading = computed(() => googleLoading.value)

const promoterMutation = useMutation({
  mutationFn: () => createPromoter({ ...promoterForm }),
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['promoters'] })
    Object.assign(promoterForm, { nome: '', documento: '', telefone: '', ativo: true })
  },
})
const isPromoterPending = computed(() => promoterMutation.isPending.value)

const deletePromoterMutation = useMutation({
  mutationFn: (id: string) => deletePromoter(id),
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ['promoters'] }),
})
const isDeletingPromoter = computed(() => deletePromoterMutation.isPending.value)

const pdvMutation = useMutation({
  mutationFn: () => createPdv({ ...pdvForm }),
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['pdvs'] })
    Object.assign(pdvForm, { nome: '', cidade: '', estado: '', codigo: '', ativo: true })
  },
})
const isPdvPending = computed(() => pdvMutation.isPending.value)

const deletePdvMutation = useMutation({
  mutationFn: (id: string) => deletePdv(id),
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ['pdvs'] }),
})
const isDeletingPdv = computed(() => deletePdvMutation.isPending.value)

const syncMutation = useMutation({
  mutationFn: triggerSync,
  onSuccess: () => refetchGoogle(),
})
const isSyncing = computed(() => syncMutation.isPending.value)
const promoterList = computed(() => promoters.value ?? [])
const pdvList = computed(() => pdvs.value ?? [])
const connectGoogleAccount = async () => {
  await auth.loginWithGoogle()
}
</script>

<template>
  <section>
    <PageHeader
      title="Painel administrativo"
      description="Gerencie promotores, PDVs e integraçoes com Google. Esta tela conversa com as rotas /api/promotores, /api/pdvs e /api/google."
    />

    <AppCard v-if="!isAuthenticated" class="mt-4" title="Autenticação necessária">
      <p class="text-sm text-slate-600">
        Para acessar o painel completo, entre com a conta Google configurada. Isso usará suas credenciais locais e
        habilitará as rotas protegidas.
      </p>
      <button
        class="mt-4 rounded-2xl bg-brand px-4 py-2 text-sm font-semibold text-white hover:bg-brand-dark"
        @click="connectGoogleAccount"
      >
        Entrar com conta Google
      </button>
    </AppCard>

    <div v-if="!isAuthenticated" class="mt-6 rounded-3xl border border-dashed border-slate-300 p-6 text-sm text-slate-500">
      Após autenticar, este painel exibirá os formulários de promotores, PDVs e status do Google.
    </div>

    <template v-else>
    <div class="grid gap-6 xl:grid-cols-2">
      <AppCard title="Promotores" subtitle="Gerencie quem pode registrar visitas">
        <form class="grid gap-3 md:grid-cols-2" @submit.prevent="promoterMutation.mutate()">
          <label class="text-sm font-medium text-slate-700">
            Nome
            <input v-model="promoterForm.nome" required class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2" />
          </label>
          <label class="text-sm font-medium text-slate-700">
            Documento
            <input v-model="promoterForm.documento" class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2" />
          </label>
          <label class="text-sm font-medium text-slate-700">
            Telefone
            <input v-model="promoterForm.telefone" class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2" />
          </label>
          <label class="flex items-center gap-2 text-sm font-medium text-slate-700">
            <input v-model="promoterForm.ativo" type="checkbox" class="rounded border-slate-300" />
            Ativo
          </label>
          <button
            type="submit"
            class="rounded-2xl bg-brand px-4 py-2 text-sm font-semibold text-white hover:bg-brand-dark md:col-span-2 disabled:opacity-50"
            :disabled="isPromoterPending"
          >
            Adicionar
          </button>
        </form>
        <div v-if="promoterList.length" class="mt-6 divide-y divide-slate-100">
          <div v-for="promoter in promoterList" :key="promoter.id" class="flex items-center justify-between py-3">
            <div>
              <p class="font-semibold text-slate-900">{{ promoter.nome }}</p>
              <p class="text-xs text-slate-500">{{ promoter.documento || 'Sem documento' }}</p>
            </div>
            <button
              class="text-sm text-rose-600"
              @click="deletePromoterMutation.mutate(promoter.id)"
              :disabled="isDeletingPromoter"
            >
              Remover
            </button>
          </div>
        </div>
        <EmptyState
          v-else
          title="Nenhum promotor cadastrado"
          description="Use o formulário acima para convidar colaboradores."
        />
      </AppCard>

      <AppCard title="PDVs" subtitle="Manutenção dos pontos de venda">
        <form class="grid gap-3 md:grid-cols-2" @submit.prevent="pdvMutation.mutate()">
          <label class="text-sm font-medium text-slate-700">
            Nome
            <input v-model="pdvForm.nome" required class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2" />
          </label>
          <label class="text-sm font-medium text-slate-700">
            Código
            <input v-model="pdvForm.codigo" class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2" />
          </label>
          <label class="text-sm font-medium text-slate-700">
            Cidade
            <input v-model="pdvForm.cidade" class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2" />
          </label>
          <label class="text-sm font-medium text-slate-700">
            Estado
            <input v-model="pdvForm.estado" class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2" />
          </label>
          <label class="flex items-center gap-2 text-sm font-medium text-slate-700">
            <input v-model="pdvForm.ativo" type="checkbox" class="rounded border-slate-300" />
            Ativo
          </label>
          <button
            type="submit"
            class="rounded-2xl bg-brand px-4 py-2 text-sm font-semibold text-white hover:bg-brand-dark md:col-span-2 disabled:opacity-50"
            :disabled="isPdvPending"
          >
            Adicionar
          </button>
        </form>
        <div v-if="pdvList.length" class="mt-6 divide-y divide-slate-100">
          <div v-for="pdv in pdvList" :key="pdv.id" class="flex items-center justify-between py-3">
            <div>
              <p class="font-semibold text-slate-900">{{ pdv.nome }}</p>
              <p class="text-xs text-slate-500">
                {{ [pdv.cidade, pdv.estado].filter(Boolean).join(' / ') || 'Local não informado' }}
              </p>
            </div>
            <button class="text-sm text-rose-600" @click="deletePdvMutation.mutate(pdv.id)" :disabled="isDeletingPdv">
              Remover
            </button>
          </div>
        </div>
        <EmptyState
          v-else
          title="Nenhum PDV cadastrado"
          description="Use o formulário acima para cadastrar os pontos de venda."
        />
      </AppCard>
    </div>

    <AppCard class="mt-6" title="Integraçao Google" subtitle="Status e açoes rapidas">
      <div v-if="googleStatus" class="grid gap-4 md:grid-cols-3">
        <div class="rounded-2xl border border-slate-100 bg-slate-50 p-4">
          <p class="text-xs font-semibold uppercase tracking-widest text-slate-500">Drive</p>
          <p class="mt-1 text-lg font-semibold" :class="googleStatus.drive_connected ? 'text-emerald-600' : 'text-rose-600'">
            {{ googleStatus.drive_connected ? 'Conectado' : 'Não conectado' }}
          </p>
          <p class="text-sm text-slate-500">
            <a v-if="googleStatus.folder_url" :href="googleStatus.folder_url" target="_blank" class="text-brand underline">Abrir pasta</a>
            <span v-else>Configure o OAuth2 no serviço conectado.</span>
          </p>
        </div>
        <div class="rounded-2xl border border-slate-100 bg-slate-50 p-4">
          <p class="text-xs font-semibold uppercase tracking-widest text-slate-500">Sheets</p>
          <p class="mt-1 text-lg font-semibold" :class="googleStatus.sheets_connected ? 'text-emerald-600' : 'text-rose-600'">
            {{ googleStatus.sheets_connected ? 'Conectado' : 'Não conectado' }}
          </p>
          <p class="text-sm text-slate-500">
            <a v-if="googleStatus.sheet_url" :href="googleStatus.sheet_url" target="_blank" class="text-brand underline">Abrir planilha</a>
            <span v-else>Defina a planilha utilizada.</span>
          </p>
        </div>
        <div class="rounded-2xl border border-slate-100 bg-slate-50 p-4">
          <p class="text-xs font-semibold uppercase tracking-widest text-slate-500">Última sincronização</p>
          <p class="mt-1 text-lg font-semibold text-slate-900">
            {{ googleStatus.last_sync ? new Date(googleStatus.last_sync).toLocaleString() : 'Ainda não sincronizado' }}
          </p>
          <p class="text-sm text-slate-500">{{ googleStatus.message }}</p>
        </div>
      </div>
      <EmptyState v-else title="Sem status" description="Faça login para visualizar a integração." />
      <div class="mt-6 flex flex-wrap gap-3">
        <button
          class="rounded-2xl border border-slate-200 px-4 py-2 text-sm font-semibold text-slate-700 disabled:opacity-50"
          @click="() => refetchGoogle()"
          :disabled="isGoogleLoading"
        >
          Atualizar status
        </button>
        <button
          class="rounded-2xl bg-brand px-4 py-2 text-sm font-semibold text-white hover:bg-brand-dark disabled:opacity-50"
          @click="syncMutation.mutate()"
          :disabled="isSyncing"
        >
          {{ isSyncing ? 'Sincronizando...' : 'Sincronizar agora' }}
        </button>
        <button
          class="rounded-2xl border border-slate-200 px-4 py-2 text-sm font-semibold text-slate-700"
          @click="connectGoogleAccount"
        >
          Reautenticar com conta Google
        </button>
      </div>
    </AppCard>
    </template>
  </section>
</template>
