# BuildLink Frontend

Next.js 14 frontend for BuildLink - a direct construction hiring platform.

## Setup

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Setup environment:
```bash
cp .env.example .env.local
# Edit .env.local with your API URL
```

### Running the Development Server

```bash
npm run dev
```

Frontend will be available at: http://localhost:3000

### Building for Production

```bash
npm run build
npm start
```

## Project Structure

```
src/
├── app/              # Next.js App Router pages
├── components/       # Reusable React components
├── features/         # Feature-based modules
├── hooks/            # Custom React hooks
├── lib/              # Utilities and services
├── types/            # TypeScript types
├── styles/           # CSS and Tailwind
└── constants/        # App constants
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint

## Technologies

- Next.js 14
- TypeScript
- Tailwind CSS
- Socket.io (for real-time features)
- Axios (for API calls)
