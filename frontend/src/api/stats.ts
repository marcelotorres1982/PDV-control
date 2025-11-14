import { http } from './client'
import type { StatsOverview } from './types'

export const fetchOverviewStats = async () => {
  const { data } = await http.get<StatsOverview>('/stats/overview')
  return data
}
