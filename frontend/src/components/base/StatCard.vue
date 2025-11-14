<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  label: string
  value: string | number
  helper?: string
  trend?: number
}>()

const trendLabel = computed(() => {
  if (typeof props.trend !== 'number') return null
  const signal = props.trend > 0 ? '+' : ''
  return `${signal}${props.trend}% vs ultimo período`
})

const trendColor = computed(() => {
  if (typeof props.trend !== 'number') return 'text-slate-500'
  return props.trend >= 0 ? 'text-emerald-600' : 'text-rose-500'
})
</script>

<template>
  <div class="rounded-3xl border border-surface-border/80 bg-white px-5 py-6 shadow-card">
    <p class="text-xs font-semibold uppercase tracking-widest text-slate-500">{{ label }}</p>
    <p class="mt-3 text-3xl font-semibold text-slate-900">{{ value }}</p>
    <p v-if="helper" class="mt-1 text-sm text-slate-500">
      {{ helper }}
    </p>
    <p v-if="trendLabel" class="mt-2 text-xs font-medium" :class="trendColor">
      {{ trendLabel }}
    </p>
  </div>
</template>
