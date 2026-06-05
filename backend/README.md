# BuildLink Backend API

FastAPI backend for BuildLink - a direct construction hiring platform.

## Setup

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- pip

### Installation

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Setup environment:
```bash
cp .env.example .env.local
# Edit .env.local with your credentials
```

4. Create database:
```bash
createdb buildlink_db
```

### Running the Server

```bash
uvicorn app.main:app --reload --port 8000
```

API will be available at: http://localhost:8000
API Documentation: http://localhost:8000/api/docs

## Project Structure

```
app/
├── core/           # Configuration, security, constants
├── database/       # Database connection setup
├── schemas/        # SQLAlchemy ORM models
├── models/         # Pydantic validation models
├── middleware/     # Authentication and middleware
├── api/            # API routes and endpoints
├── services/       # Business logic (to be implemented)
├── utils/          # Utility functions
└── main.py         # FastAPI app initialization
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh access token

### Users
- `GET /api/v1/users/me` - Get current user profile
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PUT /api/v1/users/me` - Update user profile

## Testing

### Test Registration
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "first_name": "John",
    "last_name": "Doe",
    "user_type": "owner"
  }'
```

### Test Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```
