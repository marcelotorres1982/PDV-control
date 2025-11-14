<script setup lang="ts">
import { computed, reactive, ref } from 'vue'
import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query'
import PageHeader from '@/components/base/PageHeader.vue'
import AppCard from '@/components/base/AppCard.vue'
import EmptyState from '@/components/feedback/EmptyState.vue'
import { listPromoters } from '@/api/promoters'
import { listPdvs } from '@/api/pdvs'
import { createCheckin } from '@/api/checkins'

const steps = [
  { id: 1, label: 'Dados do promotor', description: 'Selecionar equipe e PDV' },
  { id: 2, label: 'Detalhes da visita', description: 'Entradas, valores e observacoes' },
  { id: 3, label: 'Comprovantes', description: 'Upload das fotos e revisao' },
]

const queryClient = useQueryClient()
const { data: promoters } = useQuery({ queryKey: ['promoters'], queryFn: listPromoters })
const { data: pdvs } = useQuery({ queryKey: ['pdvs'], queryFn: listPdvs })
const promoterOptions = computed(() => promoters.value ?? [])
const pdvOptions = computed(() => pdvs.value ?? [])

const today = new Date()
const form = reactive({
  promotorId: '',
  pdvId: '',
  data: today.toISOString().slice(0, 10),
  hora: today.toTimeString().slice(0, 5),
  valorDeslocamento: 0,
  numEntradas: 1,
  observacoes: '',
  fotos: [] as File[],
})

const filesPreview = ref<File[]>([])

const selectedPromoter = computed(() => promoterOptions.value.find((p) => p.id === form.promotorId))
const selectedPdv = computed(() => pdvOptions.value.find((p) => p.id === form.pdvId))

const mutation = useMutation({
  mutationFn: () =>
    createCheckin({
      promotorId: form.promotorId,
      promotorNome: selectedPromoter.value?.nome || '',
      pdvId: form.pdvId,
      pdvNome: selectedPdv.value?.nome || '',
      data: form.data,
      hora: form.hora,
      valorDeslocamento: form.valorDeslocamento,
      numEntradas: form.numEntradas,
      observacoes: form.observacoes,
      fotos: form.fotos,
    }),
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['checkins'] })
    filesPreview.value = []
    form.observacoes = ''
    form.numEntradas = 1
    form.fotos = []
  },
})
const isSubmitting = computed(() => mutation.isPending.value)

const handleFiles = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files) {
    form.fotos = Array.from(target.files)
    filesPreview.value = form.fotos
  }
}
</script>

<template>
  <section>
    <PageHeader
      title="Fluxo de check-in"
      description="Registre a visita e envie os comprovantes. Sua API é responsável por salvar e sincronizar com o Google Drive/Sheets."
    />

    <div class="grid gap-6 lg:grid-cols-[2fr,1fr]">
      <AppCard title="Registrar visita" subtitle="Campos chave do endpoint">
        <form class="space-y-6" @submit.prevent="mutation.mutate()">
          <div class="grid gap-4 md:grid-cols-2">
            <label class="space-y-2 text-sm font-medium text-slate-700">
              Promotor
              <select
                v-model="form.promotorId"
                class="w-full rounded-2xl border border-slate-200 px-4 py-2 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
                required
              >
                <option value="">Selecione um promotor</option>
                <option v-for="promoter in promoterOptions" :key="promoter.id" :value="promoter.id">
                  {{ promoter.nome }}
                </option>
              </select>
            </label>
            <label class="space-y-2 text-sm font-medium text-slate-700">
              PDV
              <select
                v-model="form.pdvId"
                class="w-full rounded-2xl border border-slate-200 px-4 py-2 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
                required
              >
                <option value="">Selecione um PDV</option>
                <option v-for="pdv in pdvOptions" :key="pdv.id" :value="pdv.id">
                  {{ pdv.nome }}
                </option>
              </select>
            </label>
          </div>

          <div class="grid gap-4 md:grid-cols-3">
            <label class="space-y-2 text-sm text-slate-700">
              Data
              <input
                type="date"
                v-model="form.data"
                class="w-full rounded-2xl border border-slate-200 px-4 py-2 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
              />
            </label>
            <label class="space-y-2 text-sm text-slate-700">
              Hora
              <input
                type="time"
                v-model="form.hora"
                class="w-full rounded-2xl border border-slate-200 px-4 py-2 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
              />
            </label>
            <label class="space-y-2 text-sm text-slate-700">
              Valor deslocamento
              <input
                type="number"
                v-model.number="form.valorDeslocamento"
                placeholder="0,00"
                class="w-full rounded-2xl border border-slate-200 px-4 py-2 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
              />
            </label>
          </div>
          <label class="space-y-2 text-sm text-slate-700">
            Número de entradas
            <input
              type="number"
              min="1"
              v-model.number="form.numEntradas"
              class="w-full rounded-2xl border border-slate-200 px-4 py-2 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
            />
          </label>

          <label class="space-y-2 text-sm text-slate-700">
            Observacoes
            <textarea
              rows="4"
              v-model="form.observacoes"
              placeholder="Detalhe a visita, rupturas, campanhas..."
              class="w-full rounded-2xl border border-slate-200 px-4 py-2 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
            ></textarea>
          </label>

          <label class="space-y-2 text-sm text-slate-700">
            Fotos
            <input
              type="file"
              accept="image/*"
              multiple
              class="w-full rounded-2xl border border-dashed border-slate-300 px-4 py-6 text-sm"
              @change="handleFiles"
            />
            <p class="text-xs text-slate-500">Suporta até 20 arquivos. Tamanho máximo por arquivo: 10 MB.</p>
          </label>

          <div class="flex flex-wrap gap-3">
            <button type="button" class="rounded-2xl border border-slate-200 px-4 py-2 text-sm font-medium text-slate-600">
              Salvar rascunho
            </button>
            <button
              type="submit"
              class="rounded-2xl bg-brand px-6 py-2 text-sm font-semibold text-white shadow-sm hover:bg-brand-dark disabled:opacity-50"
              :disabled="isSubmitting"
            >
              {{ isSubmitting ? 'Enviando...' : 'Enviar para API' }}
            </button>
          </div>
        </form>
      </AppCard>

      <div class="space-y-6">
        <AppCard title="Etapas" subtitle="Mantenha o estado do formulario por etapa">
          <ol class="space-y-4">
            <li
              v-for="step in steps"
              :key="step.id"
              class="rounded-2xl border border-slate-100 bg-slate-50 px-4 py-3"
            >
              <p class="text-xs font-semibold uppercase tracking-widest text-slate-500">
                Etapa {{ step.id }}
              </p>
              <p class="text-base font-medium text-slate-900">{{ step.label }}</p>
              <p class="text-sm text-slate-500">{{ step.description }}</p>
            </li>
          </ol>
        </AppCard>

        <AppCard title="Uploads de fotos">
          <template v-if="filesPreview.length">
            <ul class="space-y-2 text-sm text-slate-600">
              <li v-for="file in filesPreview" :key="file.name" class="rounded-2xl border border-slate-100 px-3 py-2">
                {{ file.name }} - {{ (file.size / (1024 * 1024)).toFixed(2) }} MB
              </li>
            </ul>
          </template>
          <EmptyState
            v-else
            title="Nenhum arquivo selecionado"
            description="Selecione as fotos no formulário ao lado para pré-visualizar aqui."
          />
        </AppCard>
      </div>
    </div>
  </section>
</template>
