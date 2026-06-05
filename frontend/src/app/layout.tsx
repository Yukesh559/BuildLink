import type { Metadata } from 'next'
import './styles/globals.css'

export const metadata: Metadata = {
  title: 'BuildLink - Direct Construction Hiring',
  description: 'Connect house owners and construction workers directly',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-white text-gray-900">
        {children}
      </body>
    </html>
  )
}
