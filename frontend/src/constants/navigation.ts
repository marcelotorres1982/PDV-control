import type { Component } from 'vue'
import {
  Squares2X2Icon,
  PencilSquareIcon,
  TableCellsIcon,
  PhotoIcon,
  Cog6ToothIcon,
  ArrowPathIcon,
  ArrowUpTrayIcon,
} from '@heroicons/vue/24/outline'

export type NavItem = {
  label: string
  to: string
  icon: Component
  badge?: string
  description?: string
}

export const primaryNav: NavItem[] = [
  {
    label: 'Dashboard',
    to: '/',
    icon: Squares2X2Icon,
    description: 'Visao geral em tempo real',
  },
  {
    label: 'Novo Check-in',
    to: '/checkins',
    icon: PencilSquareIcon,
    description: 'Registrar visita e fotos',
  },
  {
    label: 'Registros',
    to: '/registros',
    icon: TableCellsIcon,
    description: 'Tabela detalhada',
  },
  {
    label: 'Galeria',
    to: '/galeria',
    icon: PhotoIcon,
    description: 'Fotos organizadas',
  },
  {
    label: 'Admin',
    to: '/admin',
    icon: Cog6ToothIcon,
    description: 'Configuraçoes e integraçoes',
  },
]

export const quickActions: NavItem[] = [
  {
    label: 'Sincronizar Google',
    to: '/admin',
    icon: ArrowPathIcon,
  },
  {
    label: 'Exportar CSV',
    to: '/admin',
    icon: ArrowUpTrayIcon,
  },
]
