import { http } from './client'

export type Pdv = {
  id: string
  nome: string
  cidade?: string | null
  estado?: string | null
  codigo?: string | null
  ativo: boolean
}

export type PdvPayload = Omit<Pdv, 'id'>

export const listPdvs = async () => {
  const { data } = await http.get<Pdv[]>('/pdvs')
  return data
}

export const createPdv = async (payload: PdvPayload) => {
  const { data } = await http.post<Pdv>('/pdvs', payload)
  return data
}

export const updatePdv = async (id: string, payload: PdvPayload) => {
  const { data } = await http.put<Pdv>(`/pdvs/${id}`, payload)
  return data
}

export const deletePdv = async (id: string) => {
  await http.delete(`/pdvs/${id}`)
}
