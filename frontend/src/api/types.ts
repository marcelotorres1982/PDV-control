export type Promotor = {
  id: string
  nome: string
  documento?: string | null
  telefone?: string | null
  ativo: boolean
}

export type Pdv = {
  id: string
  nome: string
  cidade?: string | null
  estado?: string | null
  codigo?: string | null
  ativo: boolean
}

export type PhotoMetadata = {
  original_name: string
  stored_name: string
  path: string
  size?: number
  content_type?: string
  drive_file_id?: string
  drive_url?: string
}

export type CheckinPayload = {
  promotorId: string
  promotorNome: string
  pdvId: string
  pdvNome: string
  data: string
  hora: string
  valorDeslocamento: number
  numEntradas: number
  observacoes?: string
  fotos?: File[]
}

export type Checkin = {
  id: string
  promotorId: string
  promotorNome: string
  pdvId: string
  pdvNome: string
  data: string
  hora: string
  valorDeslocamento: number
  numEntradas: number
  observacoes?: string
  fotos?: PhotoMetadata[]
  createdAt: string
  updatedAt?: string
}

export type StatsOverview = {
  totalRegistros: number
  totalPromotores: number
  totalPdvs: number
  totalDeslocamento: number
  totalEntradas: number
  totalFotos: number
}

export type GoogleStatus = {
  driveConnected: boolean
  sheetsConnected: boolean
  lastSync?: string
  folderUrl?: string
  sheetUrl?: string
}
