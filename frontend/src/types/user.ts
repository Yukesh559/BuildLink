export type UserType = 'owner' | 'worker' | 'admin'

export interface User {
  id: string
  email: string
  firstName: string
  lastName: string
  userType: UserType
  phone?: string
  profileImageUrl?: string
  bio?: string
  location?: string
  isVerified: boolean
  isBlocked: boolean
  createdAt: string
}

export interface TokenResponse {
  accessToken: string
  refreshToken: string
  tokenType: string
  user: User
}
