'use client'

import { useState } from 'react'
import Link from 'next/link'
import api from '@/lib/api'

interface JobFormData {
  title: string
  description: string
  category: string
  budgetMin: number
  budgetMax: number
  location: string
  timeline?: number
  skills?: string
}

export default function CreateJobPage() {
  const [formData, setFormData] = useState<JobFormData>({
    title: '',
    description: '',
    category: '',
    budgetMin: 0,
    budgetMax: 0,
    location: '',
    timeline: undefined,
    skills: '',
  })
  const [error, setError] = useState('')
  const [success, setSuccess] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: ['budgetMin', 'budgetMax', 'timeline'].includes(name) ? parseFloat(value) || 0 : value,
    }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    setIsLoading(true)

    try {
      // Validate budget
      if (formData.budgetMin <= 0 || formData.budgetMax <= 0) {
        setError('Budget must be greater than 0')
        setIsLoading(false)
        return
      }

      if (formData.budgetMin > formData.budgetMax) {
        setError('Minimum budget cannot be greater than maximum budget')
        setIsLoading(false)
        return
      }

      const payload = {
        ...formData,
        required_skills: formData.skills ? formData.skills.split(',').map(s => s.trim()) : undefined,
        timeline_days: formData.timeline,
      }

      const response = await api.post('/jobs', payload)
      setSuccess(true)
      setFormData({
        title: '',
        description: '',
        category: '',
        budgetMin: 0,
        budgetMax: 0,
        location: '',
        timeline: undefined,
        skills: '',
      })
      // Redirect to job details or jobs list
      setTimeout(() => {
        window.location.href = '/owner/jobs'
      }, 1500)
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to create job')
    } finally {
      setIsLoading(false)
    }
  }

  const categories = [
    'Carpentry',
    'Plumbing',
    'Electrical',
    'Painting',
    'Masonry',
    'Roofing',
    'Landscaping',
    'General Repairs',
    'Other',
  ]

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-2xl mx-auto">
        <div className="mb-8">
          <Link href="/owner/jobs" className="text-blue-600 hover:text-blue-700">
            ← Back to Jobs
          </Link>
          <h1 className="text-4xl font-bold text-gray-900 mt-4">Post a New Job</h1>
          <p className="text-gray-600 mt-2">
            Describe your project and get bids from construction professionals
          </p>
        </div>

        <div className="bg-white rounded-lg shadow p-8">
          <form onSubmit={handleSubmit} className="space-y-6">
            {error && (
              <div className="bg-red-50 border border-red-200 p-4 rounded-lg">
                <p className="text-red-800">{error}</p>
              </div>
            )}

            {success && (
              <div className="bg-green-50 border border-green-200 p-4 rounded-lg">
                <p className="text-green-800">Job posted successfully! Redirecting...</p>
              </div>
            )}

            <div>
              <label htmlFor="title" className="block text-sm font-medium text-gray-700">
                Job Title
              </label>
              <input
                id="title"
                name="title"
                type="text"
                required
                placeholder="e.g., Kitchen Renovation"
                className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                value={formData.title}
                onChange={handleChange}
              />
            </div>

            <div>
              <label htmlFor="category" className="block text-sm font-medium text-gray-700">
                Category
              </label>
              <select
                id="category"
                name="category"
                required
                className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                value={formData.category}
                onChange={handleChange}
              >
                <option value="">Select a category</option>
                {categories.map(cat => (
                  <option key={cat} value={cat}>
                    {cat}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label htmlFor="description" className="block text-sm font-medium text-gray-700">
                Description
              </label>
              <textarea
                id="description"
                name="description"
                required
                rows={6}
                placeholder="Describe your project in detail..."
                className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                value={formData.description}
                onChange={handleChange}
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label htmlFor="budgetMin" className="block text-sm font-medium text-gray-700">
                  Minimum Budget ($)
                </label>
                <input
                  id="budgetMin"
                  name="budgetMin"
                  type="number"
                  required
                  min="1"
                  step="100"
                  className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                  value={formData.budgetMin || ''}
                  onChange={handleChange}
                />
              </div>
              <div>
                <label htmlFor="budgetMax" className="block text-sm font-medium text-gray-700">
                  Maximum Budget ($)
                </label>
                <input
                  id="budgetMax"
                  name="budgetMax"
                  type="number"
                  required
                  min="1"
                  step="100"
                  className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                  value={formData.budgetMax || ''}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div>
              <label htmlFor="location" className="block text-sm font-medium text-gray-700">
                Location
              </label>
              <input
                id="location"
                name="location"
                type="text"
                required
                placeholder="e.g., New York, NY"
                className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                value={formData.location}
                onChange={handleChange}
              />
            </div>

            <div>
              <label htmlFor="timeline" className="block text-sm font-medium text-gray-700">
                Timeline (days)
              </label>
              <input
                id="timeline"
                name="timeline"
                type="number"
                min="1"
                placeholder="Expected number of days"
                className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                value={formData.timeline || ''}
                onChange={handleChange}
              />
            </div>

            <div>
              <label htmlFor="skills" className="block text-sm font-medium text-gray-700">
                Required Skills (comma-separated)
              </label>
              <input
                id="skills"
                name="skills"
                type="text"
                placeholder="e.g., carpentry, plumbing"
                className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                value={formData.skills}
                onChange={handleChange}
              />
            </div>

            <div className="flex gap-4">
              <button
                type="submit"
                disabled={isLoading}
                className="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:opacity-50 font-medium"
              >
                {isLoading ? 'Creating...' : 'Post Job'}
              </button>
              <Link
                href="/owner/jobs"
                className="flex-1 border border-gray-300 text-gray-700 py-2 px-4 rounded-md hover:bg-gray-50 font-medium text-center"
              >
                Cancel
              </Link>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}
