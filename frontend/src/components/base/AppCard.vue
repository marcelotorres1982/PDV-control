<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    title?: string
    subtitle?: string
    padding?: 'sm' | 'md' | 'lg'
  }>(),
  {
    padding: 'md',
  },
)

const paddingMap = {
  sm: 'p-4',
  md: 'p-6',
  lg: 'p-8',
} as const
</script>

<template>
  <section
    class="rounded-3xl border border-surface-border/80 bg-white shadow-card transition hover:shadow-lg"
    :class="paddingMap[props.padding]"
  >
    <header v-if="title" class="mb-4">
      <p class="text-base font-semibold text-slate-900">{{ title }}</p>
      <p v-if="subtitle" class="text-sm text-slate-500">{{ subtitle }}</p>
    </header>
    <slot />
  </section>
</template>
