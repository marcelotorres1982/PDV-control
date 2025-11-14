<script setup lang="ts">
import { RouterLink, useRoute } from 'vue-router'
import { XMarkIcon } from '@heroicons/vue/24/outline'
import { primaryNav } from '@/constants/navigation'
import { useUiStore } from '@/stores/ui'

const ui = useUiStore()
const route = useRoute()

const isActive = (path: string) => route.path === path
</script>

<template>
  <aside
    class="fixed inset-y-0 left-0 z-30 w-72 border-r border-slate-800/40 bg-slate-950 text-white shadow-2xl transition-transform duration-300 lg:static lg:translate-x-0"
    :class="[ui.sidebarOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0']"
  >
    <div class="flex items-center justify-between px-6 pt-6 lg:hidden">
      <div>
        <p class="text-sm uppercase tracking-widest text-slate-400">PDV Control</p>
        <p class="text-lg font-semibold text-white">Console</p>
      </div>
      <button
        class="rounded-full border border-white/20 p-1 text-white hover:bg-white/10"
        @click="ui.toggleSidebar(false)"
      >
        <XMarkIcon class="h-5 w-5" />
      </button>
    </div>
    <div class="hidden items-center gap-2 px-6 pt-8 lg:flex">
      <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-brand text-white font-semibold">
        PC
      </div>
      <div>
        <p class="text-xs uppercase tracking-widest text-slate-400">PDV Control</p>
        <p class="text-lg font-semibold">Console</p>
      </div>
    </div>

    <nav class="mt-8 px-4">
      <p class="px-2 text-xs uppercase tracking-wider text-slate-400">Navegaçao</p>
      <ul class="mt-4 space-y-1">
        <li v-for="item in primaryNav" :key="item.to">
          <RouterLink
            :to="item.to"
            class="group flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium transition"
            :class="isActive(item.to) ? 'bg-white/10 text-white' : 'text-slate-300 hover:bg-white/5 hover:text-white'"
            @click="ui.toggleSidebar(false)"
          >
            <component
              :is="item.icon"
              class="h-5 w-5"
              :class="isActive(item.to) ? 'text-brand' : 'text-slate-400 group-hover:text-brand'"
            />
            <div class="flex-1">
              <p>{{ item.label }}</p>
              <p class="text-xs font-normal text-slate-400" v-if="item.description">{{ item.description }}</p>
            </div>
          </RouterLink>
        </li>
      </ul>
    </nav>

    <div class="mt-10 border-t border-white/5 px-6 pt-6 text-xs text-slate-400">
      <p>Integraçao Google</p>
      <p class="mt-1 text-white">Status: Em configuraçao</p>
    </div>
  </aside>
</template>
