export interface Bid {
  id: string
  jobId: string
  workerId: string
  bidAmount: number
  bidMessage?: string
  proposedTimelineDays?: number
  bidStatus: 'pending' | 'accepted' | 'rejected' | 'completed'
  createdAt: string
  updatedAt: string
}

export interface BidCreate {
  jobId: string
  bidAmount: number
  bidMessage?: string
  proposedTimelineDays?: number
}
