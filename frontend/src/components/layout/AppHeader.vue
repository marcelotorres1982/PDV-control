<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { Bars3Icon, BellIcon, PlusIcon, ArrowRightOnRectangleIcon } from '@heroicons/vue/24/outline'
import { quickActions } from '@/constants/navigation'
import { useUiStore } from '@/stores/ui'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const router = useRouter()
const ui = useUiStore()
const auth = useAuthStore()

const pageTitle = computed(() => (route.meta?.title as string) || 'PDV Control')
const isAuthenticated = computed(() => auth.isAuthenticated)
const initials = computed(() => auth.user?.name?.split(' ').map((word) => word[0]).join('').slice(0, 2) ?? '??')
const userName = computed(() => auth.user?.name ?? 'Visitante')

const goToCheckin = () => {
  router.push('/checkins')
}

const handleAuthAction = () => {
  if (isAuthenticated.value) {
    auth.logout()
    router.push('/login')
  } else {
    router.push('/login')
  }
}
</script>

<template>
  <header class="sticky top-0 z-10 border-b border-surface-border/60 bg-surface/90 backdrop-blur-lg">
    <div class="flex flex-col gap-4 px-4 py-4 lg:flex-row lg:items-center lg:justify-between lg:px-10">
      <div class="flex items-center gap-3">
        <button
          class="rounded-2xl border border-slate-200 bg-white p-2 shadow-sm lg:hidden"
          @click="ui.toggleSidebar()"
          aria-label="Menu"
        >
          <Bars3Icon class="h-6 w-6 text-slate-700" />
        </button>
        <div>
          <p class="text-xs font-medium uppercase tracking-widest text-slate-500">Visao Atual</p>
          <p class="text-2xl font-semibold text-slate-900">{{ pageTitle }}</p>
        </div>
      </div>

      <div class="flex flex-1 flex-col gap-3 lg:flex-row lg:items-center lg:justify-end">
        <div class="relative w-full max-w-md">
          <input
            type="search"
            placeholder="Pesquisar promotor, PDV ou registro..."
            class="w-full rounded-2xl border border-slate-200 bg-white px-4 py-2.5 pl-11 text-sm text-slate-700 placeholder:text-slate-400 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
          />
          <span class="pointer-events-none absolute left-3 top-2.5 text-slate-400">⌘K</span>
        </div>

        <div class="flex items-center gap-3">
          <button
            class="hidden rounded-2xl border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-600 shadow-sm hover:text-slate-900 lg:inline-flex"
            @click="goToCheckin"
          >
            <PlusIcon class="mr-2 h-5 w-5" />
            Novo check-in
          </button>
          <button class="rounded-2xl border border-slate-200 bg-white p-2 text-slate-600 shadow-sm">
            <BellIcon class="h-5 w-5" />
          </button>
          <div class="hidden items-center gap-3 rounded-2xl border border-slate-200 bg-white px-3 py-2 shadow-sm md:flex">
            <div class="flex h-8 w-8 items-center justify-center rounded-full bg-brand text-sm font-semibold text-white">
              {{ initials }}
            </div>
            <div class="leading-tight">
              <p class="text-sm font-semibold text-slate-900">{{ userName }}</p>
              <p class="text-xs text-slate-500">
                {{ isAuthenticated ? 'Administrador' : 'Visitante' }}
              </p>
            </div>
          </div>
          <button
            class="inline-flex items-center gap-2 rounded-2xl border border-slate-200 bg-white px-3 py-2 text-sm font-semibold text-slate-700 shadow-sm hover:text-slate-900"
            @click="handleAuthAction"
          >
            <ArrowRightOnRectangleIcon class="h-5 w-5" />
            {{ isAuthenticated ? 'Sair' : 'Entrar' }}
          </button>
        </div>
      </div>
    </div>

    <div class="flex flex-wrap gap-3 border-t border-surface-border/60 px-4 py-3 lg:px-10">
      <button
        v-for="action in quickActions"
        :key="action.label"
        class="inline-flex items-center gap-2 rounded-2xl border border-brand/30 bg-white px-4 py-2 text-sm font-medium text-brand shadow-sm transition hover:bg-brand hover:text-white"
        @click="router.push(action.to)"
      >
        <component :is="action.icon" class="h-4 w-4" />
        {{ action.label }}
      </button>
    </div>
  </header>
</template>
