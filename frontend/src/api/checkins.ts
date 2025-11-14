import { http } from './client'
import type { Checkin, CheckinPayload } from './types'

export type CheckinFilters = Partial<{
  promotorId: string
  pdvId: string
  startDate: string
  endDate: string
}>

export const listCheckins = async (filters: CheckinFilters = {}) => {
  const { data } = await http.get<Checkin[]>('/checkins', { params: filters })
  return data
}

export const createCheckin = async (payload: CheckinPayload) => {
  const formData = new FormData()
  Object.entries(payload).forEach(([key, value]) => {
    if (key === 'fotos' && Array.isArray(value)) {
      value.forEach((file) => formData.append('fotos', file))
      return
    }
    const map: Record<string, string> = {
      promotorId: 'promotor_id',
      promotorNome: 'promotor_nome',
      pdvId: 'pdv_id',
      pdvNome: 'pdv_nome',
      valorDeslocamento: 'valor_deslocamento',
      numEntradas: 'num_entradas',
    }
    const normalizedKey = map[key] ?? key
    formData.append(normalizedKey, value as string)
  })

  const { data } = await http.post<Checkin>('/checkins', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return data
}
