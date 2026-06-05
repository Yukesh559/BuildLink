// API endpoints
export const API_ENDPOINTS = {
  // Auth
  AUTH_REGISTER: '/auth/register',
  AUTH_LOGIN: '/auth/login',
  AUTH_REFRESH: '/auth/refresh',

  // Users
  USERS_ME: '/users/me',
  USERS_GET: (id: string) => `/users/${id}`,
  USERS_UPDATE_ME: '/users/me',

  // Jobs (Phase 3)
  JOBS_CREATE: '/jobs',
  JOBS_LIST: '/jobs',
  JOBS_GET: (id: string) => `/jobs/${id}`,
  JOBS_UPDATE: (id: string) => `/jobs/${id}`,
  JOBS_DELETE: (id: string) => `/jobs/${id}`,
  JOBS_SEARCH: '/jobs/search',

  // Bids (Phase 4)
  BIDS_CREATE: '/bids',
  BIDS_GET: (id: string) => `/bids/${id}`,
  BIDS_ACCEPT: (id: string) => `/bids/${id}/accept`,
  BIDS_REJECT: (id: string) => `/bids/${id}/reject`,

  // Chat (Phase 6)
  CHAT_SEND: '/chat/message',
  CHAT_HISTORY: (userId: string) => `/chat/history/${userId}`,

  // Payments (Phase 8)
  PAYMENTS_CREATE: '/payments',
  PAYMENTS_GET: (id: string) => `/payments/${id}`,

  // Reviews (Phase 9)
  REVIEWS_CREATE: '/reviews',
  REVIEWS_GET: (userId: string) => `/reviews/${userId}`,
}

// Routes
export const ROUTES = {
  HOME: '/',
  LOGIN: '/login',
  REGISTER_OWNER: '/register/owner',
  REGISTER_WORKER: '/register/worker',
  OWNER_DASHBOARD: '/owner',
  WORKER_DASHBOARD: '/worker',
  ADMIN_DASHBOARD: '/admin',
  MESSAGES: '/messages',
  PROFILE: '/profile',
  NOTIFICATIONS: '/notifications',
}
