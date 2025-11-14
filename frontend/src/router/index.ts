import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: () => import('@/pages/DashboardView.vue'),
      meta: { title: 'Dashboard', requiresAuth: false },
    },
    {
      path: '/checkins',
      name: 'checkins',
      component: () => import('@/pages/CheckinView.vue'),
      meta: { title: 'Novo Check-in' },
    },
    {
      path: '/registros',
      name: 'records',
      component: () => import('@/pages/RecordsView.vue'),
      meta: { title: 'Registros' },
    },
    {
      path: '/galeria',
      name: 'gallery',
      component: () => import('@/pages/GalleryView.vue'),
      meta: { title: 'Galeria' },
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('@/pages/AdminView.vue'),
      meta: { title: 'Painel Administrativo', requiresAuth: true },
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/pages/LoginView.vue'),
      meta: { title: 'Entrar', public: true },
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('@/pages/NotFoundView.vue'),
      meta: { title: 'Não encontrado' },
    },
  ],
  scrollBehavior() {
    return { top: 0, behavior: 'smooth' }
  },
})

router.afterEach((to) => {
  const baseTitle = 'PDV Control'
  document.title = to.meta?.title ? `${to.meta.title} · ${baseTitle}` : baseTitle
})

router.beforeEach((to) => {
  const auth = useAuthStore()
  if (to.meta?.requiresAuth && !auth.isAuthenticated) {
    return { name: 'login', query: { redirect: to.fullPath } }
  }
  if (to.name === 'login' && auth.isAuthenticated) {
    return { name: 'dashboard' }
  }
  return true
})

export default router
