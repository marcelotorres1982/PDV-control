import { http } from './client'

export type LoginPayload = {
  email: string
  password: string
}

export type RegisterPayload = {
  name: string
  email: string
  password: string
}

export type AuthResponse = {
  access_token: string
  user: {
    id: string
    name: string
    email: string
  }
}

export type GoogleLoginResponse = Partial<AuthResponse> & {
  auth_url?: string
}

export const login = async (payload: LoginPayload) => {
  const { data } = await http.post<AuthResponse>('/auth/login', payload)
  return data
}

export const loginWithGoogle = async () => {
  const { data } = await http.post<GoogleLoginResponse>('/auth/google-login')
  return data
}

export const register = async (payload: RegisterPayload) => {
  const { data } = await http.post<AuthResponse>('/auth/register', payload)
  return data
}

export const fetchProfile = async () => {
  const { data } = await http.get<AuthResponse['user']>('/auth/me')
  return data
}
