import { http } from './client'

export type GoogleStatus = {
  drive_connected: boolean
  sheets_connected: boolean
  last_sync?: string
  folder_url?: string
  sheet_url?: string
  message: string
}

export const fetchGoogleStatus = async () => {
  const { data } = await http.get<GoogleStatus>('/google/status')
  return data
}

export const triggerSync = async () => {
  const { data } = await http.post<GoogleStatus>('/google/sync')
  return data
}
