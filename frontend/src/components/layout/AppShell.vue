<script setup lang="ts">
import { storeToRefs } from 'pinia'
import AppSidebar from './AppSidebar.vue'
import AppHeader from './AppHeader.vue'
import { useUiStore } from '@/stores/ui'

const ui = useUiStore()
const { sidebarOpen } = storeToRefs(ui)
const closeSidebar = () => ui.toggleSidebar(false)
</script>

<template>
  <div class="min-h-screen bg-surface text-slate-900 flex">
    <AppSidebar />
    <div class="flex-1 flex flex-col min-h-screen">
      <AppHeader />
      <main class="flex-1 px-4 py-6 lg:px-10 lg:py-10 bg-surface">
        <slot />
      </main>
    </div>

    <transition name="fade">
      <div
        v-if="sidebarOpen"
        class="fixed inset-0 z-20 bg-slate-900/70 backdrop-blur-sm lg:hidden"
        @click="closeSidebar"
      />
    </transition>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
