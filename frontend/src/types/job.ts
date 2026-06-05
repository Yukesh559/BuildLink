export interface Job {
  id: string
  ownerId: string
  title: string
  description: string
  category: string
  budgetMin: number
  budgetMax: number
  location: string
  latitude?: string
  longitude?: string
  jobStatus: 'open' | 'in_progress' | 'completed' | 'cancelled'
  imagesUrls?: string[]
  requiredSkills?: string[]
  timelineDays?: number
  winnerBidId?: string
  createdAt: string
  updatedAt: string
}

export interface JobCreate {
  title: string
  description: string
  category: string
  budgetMin: number
  budgetMax: number
  location: string
  latitude?: string
  longitude?: string
  imagesUrls?: string[]
  requiredSkills?: string[]
  timelineDays?: number
}
