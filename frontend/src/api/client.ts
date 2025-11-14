import axios from 'axios'

const baseURL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api'
let authToken: string | null = null

export const setAuthToken = (token: string | null) => {
  authToken = token
}

export const http = axios.create({
  baseURL,
  timeout: 15000,
})

http.interceptors.request.use((config) => {
  if (authToken) {
    config.headers.Authorization = `Bearer ${authToken}`
  }
  return config
})

http.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error?.response?.status === 401) {
      setAuthToken(null)
    }
    console.warn('[API]', error?.response?.data || error.message)
    return Promise.reject(error)
  },
)
