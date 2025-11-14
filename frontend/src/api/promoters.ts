import { http } from './client'

export type Promoter = {
  id: string
  nome: string
  documento?: string | null
  telefone?: string | null
  ativo: boolean
}

export type PromoterPayload = Omit<Promoter, 'id'>

export const listPromoters = async () => {
  const { data } = await http.get<Promoter[]>('/promotores')
  return data
}

export const createPromoter = async (payload: PromoterPayload) => {
  const { data } = await http.post<Promoter>('/promotores', payload)
  return data
}

export const updatePromoter = async (id: string, payload: PromoterPayload) => {
  const { data } = await http.put<Promoter>(`/promotores/${id}`, payload)
  return data
}

export const deletePromoter = async (id: string) => {
  await http.delete(`/promotores/${id}`)
}
