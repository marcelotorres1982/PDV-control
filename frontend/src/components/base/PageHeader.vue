<script setup lang="ts">
defineProps<{
  title: string
  description?: string
  meta?: Array<{ label: string; value: string }>
}>()
</script>

<template>
  <div class="mb-6 flex flex-col gap-4 rounded-3xl border border-transparent bg-gradient-to-r from-white to-brand/5 p-6 lg:flex-row lg:items-center lg:justify-between">
    <div>
      <h1 class="text-3xl font-semibold text-slate-900">{{ title }}</h1>
      <p v-if="description" class="mt-2 max-w-2xl text-sm text-slate-600">
        {{ description }}
      </p>
    </div>
    <div class="flex flex-wrap gap-4">
      <div
        v-for="item in meta"
        :key="item.label"
        class="rounded-2xl border border-brand/20 bg-white px-4 py-2 text-left"
      >
        <p class="text-xs uppercase tracking-wider text-slate-500">{{ item.label }}</p>
        <p class="text-lg font-semibold text-slate-900">{{ item.value }}</p>
      </div>
    </div>
    <div v-if="$slots.actions" class="flex items-center gap-3">
      <slot name="actions" />
    </div>
  </div>
</template>
