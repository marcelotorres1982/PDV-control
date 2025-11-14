<script setup lang="ts">
const emit = defineEmits<{
  action: []
}>()

defineProps<{
  title: string
  description?: string
  actionLabel?: string
}>()
</script>

<template>
  <div class="flex flex-col items-center justify-center rounded-3xl border-2 border-dashed border-slate-200 bg-white/60 px-6 py-10 text-center">
    <p class="text-lg font-semibold text-slate-900">{{ title }}</p>
    <p v-if="description" class="mt-2 max-w-xl text-sm text-slate-500">
      {{ description }}
    </p>
    <button
      v-if="actionLabel"
      class="mt-4 inline-flex items-center gap-2 rounded-2xl border border-brand/30 bg-brand px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-brand-dark"
      @click="emit('action')"
    >
      {{ actionLabel }}
    </button>
  </div>
</template>
