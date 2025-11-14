import { defineStore } from 'pinia'

export const useUiStore = defineStore('ui', {
  state: () => ({
    sidebarOpen: false,
  }),
  actions: {
    toggleSidebar(force?: boolean) {
      if (typeof force === 'boolean') {
        this.sidebarOpen = force
        return
      }
      this.sidebarOpen = !this.sidebarOpen
    },
  },
})
