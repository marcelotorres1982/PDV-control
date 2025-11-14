<script setup lang="ts">
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { register as registerRequest } from '@/api/auth'

const form = ref({
  email: '',
  password: '',
})
const registerForm = ref({
  name: '',
  email: '',
  password: '',
})
const loading = ref(false)
const registering = ref(false)
const errorMessage = ref<string | null>(null)
const registerMessage = ref<string | null>(null)
const router = useRouter()
const route = useRoute()
const auth = useAuthStore()

const handleSubmit = async () => {
  loading.value = true
  errorMessage.value = null
  try {
    await auth.login(form.value.email, form.value.password)
    const redirect = (route.query.redirect as string) || '/'
    router.replace(redirect)
  } catch (error) {
    errorMessage.value = 'Credenciais inválidas'
    console.warn(error)
  } finally {
    loading.value = false
  }
}

const handleRegister = async () => {
  registerMessage.value = null
  registering.value = true
  try {
    await registerRequest(registerForm.value)
    registerMessage.value = 'Usuário criado! Use o formulário acima para entrar.'
    form.value.email = registerForm.value.email
    registerForm.value = { name: '', email: '', password: '' }
  } catch (error) {
    registerMessage.value = 'Não foi possível criar o usuário (talvez já exista).'
    console.warn(error)
  } finally {
    registering.value = false
  }
}
const handleGoogleLogin = async () => {
  loading.value = true
  errorMessage.value = null
  try {
    await auth.loginWithGoogle()
    router.replace((route.query.redirect as string) || '/')
  } catch (error) {
    errorMessage.value = 'Falha ao entrar com a conta Google.'
    console.warn(error)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="mx-auto flex min-h-[60vh] max-w-md flex-col justify-center">
    <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-card">
      <h1 class="text-2xl font-semibold text-slate-900">Entrar no PDV Control</h1>
      <p class="mt-1 text-sm text-slate-500">Somente usuários autorizados podem acessar o painel.</p>
      <form class="mt-6 space-y-4" @submit.prevent="handleSubmit">
        <label class="block text-sm font-medium text-slate-700">
          E-mail
          <input
            v-model="form.email"
            type="email"
            required
            class="mt-1 w-full rounded-2xl border border-slate-200 px-4 py-2 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
          />
        </label>
        <label class="block text-sm font-medium text-slate-700">
          Senha
          <input
            v-model="form.password"
            type="password"
            required
            class="mt-1 w-full rounded-2xl border border-slate-200 px-4 py-2 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/10"
          />
        </label>
        <p v-if="errorMessage" class="text-sm text-rose-600">
          {{ errorMessage }}
        </p>
        <button
          type="submit"
          class="w-full rounded-2xl bg-brand px-4 py-2 text-sm font-semibold text-white hover:bg-brand-dark disabled:opacity-60"
          :disabled="loading"
        >
          {{ loading ? 'Entrando...' : 'Entrar' }}
        </button>
      </form>
      <button
        class="mt-4 w-full rounded-2xl border border-slate-200 px-4 py-2 text-sm font-semibold text-slate-700 hover:text-slate-900"
        @click="handleGoogleLogin"
        :disabled="loading"
      >
        Entrar com conta Google
      </button>
    </div>
    <div class="mt-6 rounded-3xl border border-slate-200 bg-white p-6 shadow-card">
      <p class="text-sm font-semibold text-slate-900">Primeiro acesso?</p>
      <p class="text-sm text-slate-500">
        Caso ainda não exista nenhum usuário, cadastre o administrador inicial:
      </p>
      <form class="mt-4 grid gap-3 md:grid-cols-2" @submit.prevent="handleRegister">
        <label class="text-sm font-medium text-slate-700">
          Nome
          <input
            v-model="registerForm.name"
            required
            class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2"
          />
        </label>
        <label class="text-sm font-medium text-slate-700">
          E-mail
          <input
            v-model="registerForm.email"
            type="email"
            required
            class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2"
          />
        </label>
        <label class="text-sm font-medium text-slate-700 md:col-span-2">
          Senha
          <input
            v-model="registerForm.password"
            type="password"
            required
            class="mt-1 w-full rounded-2xl border border-slate-200 px-3 py-2"
          />
        </label>
        <button
          type="submit"
          class="rounded-2xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white hover:bg-slate-800 md:col-span-2 disabled:opacity-60"
          :disabled="registering"
        >
          {{ registering ? 'Registrando...' : 'Criar usuário administrador' }}
        </button>
      </form>
      <p v-if="registerMessage" class="mt-2 text-sm" :class="registerMessage.includes('não') ? 'text-rose-600' : 'text-emerald-600'">
        {{ registerMessage }}
      </p>
    </div>
  </div>
</template>
