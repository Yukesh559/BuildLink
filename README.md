# BuildLink - Direct Construction Hiring Platform

BuildLink is a web application that connects house owners and construction workers directly, eliminating middlemen. The platform features job posting, bidding, real-time chat, payments, and reviews.

## 🚀 Project Structure

```
BuildLink/
├── backend/          # FastAPI backend
├── frontend/         # Next.js frontend (Coming in Phase 2)
└── README.md         # This file
```

## 📋 Tech Stack

- **Frontend:** Next.js 14, TypeScript, Tailwind CSS
- **Backend:** FastAPI, Python 3.10+
- **Database:** PostgreSQL
- **Authentication:** JWT
- **Real-time:** WebSockets
- **File Upload:** Cloudinary
- **Payments:** Stripe (mock for now)

## 🏗️ Development Phases

- ✅ **Phase 1:** Backend Foundation (Auth, User Management)
- ⏳ **Phase 2:** Frontend Foundation (Pages, Components)
- ⏳ **Phase 3:** Job Management
- ⏳ **Phase 4:** Bidding System
- ⏳ **Phase 5:** Worker Discovery
- ⏳ **Phase 6:** Real-time Chat
- ⏳ **Phase 7:** Notifications
- ⏳ **Phase 8:** Payment Integration
- ⏳ **Phase 9:** Reviews & Ratings
- ⏳ **Phase 10:** Dashboards
- ⏳ **Phase 11:** Admin Panel
- ⏳ **Phase 12:** Testing & Deployment

## 🚀 Quick Start

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env.local
# Edit .env.local with your credentials
uvicorn app.main:app --reload
```

Backend will run at: http://localhost:8000

### Frontend (Coming Soon)

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at: http://localhost:3000

## 📚 API Documentation

Once backend is running, visit: http://localhost:8000/api/docs

## 🤝 Contributing

This is an active development project. Check the current phase for what's being worked on.

## 📝 License

MIT License
