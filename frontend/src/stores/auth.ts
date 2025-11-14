import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import {
  fetchProfile,
  login as loginRequest,
  loginWithGoogle as loginWithGoogleRequest,
  type AuthResponse,
} from '@/api/auth'
import { setAuthToken } from '@/api/client'

type User = {
  id: string
  name: string
  email: string
}

const TOKEN_KEY = 'pdvcontrol_token'

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null)
  const token = ref<string | null>(localStorage.getItem(TOKEN_KEY))
  const persistSession = (session: AuthResponse) => {
    token.value = session.access_token
    user.value = session.user
    if (session.access_token) {
      setAuthToken(session.access_token)
      localStorage.setItem(TOKEN_KEY, session.access_token)
    }
  }
  const redirectTo = (url: string) => {
    if (typeof window === 'undefined') return
    window.location.href = url
  }
  if (token.value) {
    setAuthToken(token.value)
    fetchProfile()
      .then((profile) => {
        user.value = profile
      })
      .catch(() => {
        logout()
      })
  }

  const login = async (email: string, password: string) => {
    const data = await loginRequest({ email, password })
    persistSession(data)
  }

  const logout = () => {
    token.value = null
    user.value = null
    setAuthToken(null)
    localStorage.removeItem(TOKEN_KEY)
  }

  const loginWithGoogle = async () => {
    try {
      const data = await loginWithGoogleRequest()
      if (data?.auth_url && !data.access_token) {
        redirectTo(data.auth_url)
        return
      }
      if (data?.access_token && data.user) {
        persistSession({ access_token: data.access_token, user: data.user })
        return
      }
      throw new Error('Resposta inválida ao iniciar login com Google')
    } catch (error) {
      const fallbackUrl = import.meta.env.VITE_GOOGLE_OAUTH_URL
      if (fallbackUrl) {
        console.warn('[Auth] Falha ao acessar /auth/google-login, redirecionando para VITE_GOOGLE_OAUTH_URL.')
        redirectTo(fallbackUrl)
        return
      }
      console.error('[Auth] Não foi possível iniciar o fluxo de OAuth com Google.', error)
      throw error
    }
  }

  return {
    user,
    token,
    isAuthenticated: computed(() => Boolean(token.value)),
    login,
    logout,
    loginWithGoogle,
  }
})
