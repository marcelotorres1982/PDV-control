<template>
  <div class="flex min-h-[60vh] flex-col items-center justify-center text-center">
    <p class="text-7xl font-semibold text-brand">404</p>
    <p class="mt-4 text-2xl font-semibold text-slate-900">Pagina nao encontrada</p>
    <p class="mt-2 max-w-md text-sm text-slate-500">
      Verifique a URL ou utilize o menu lateral para navegar entre Dashboard, Check-ins, Registros, Galeria e Admin.
    </p>
    <RouterLink
      to="/"
      class="mt-6 rounded-2xl bg-brand px-6 py-2 text-sm font-semibold text-white hover:bg-brand-dark"
    >
      Voltar para o Dashboard
    </RouterLink>
  </div>
</template>
