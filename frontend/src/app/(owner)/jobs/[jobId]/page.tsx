'use client'

import { useEffect, useState } from 'react'
import { useParams } from 'next/navigation'
import Link from 'next/link'
import api from '@/lib/api'
import { formatCurrency, formatDate } from '@/lib/formatters'

interface Job {
  id: string
  title: string
  description: string
  category: string
  budgetMin: number
  budgetMax: number
  location: string
  jobStatus: string
  requiredSkills?: string[]
  timelineDays?: number
  createdAt: string
}

export default function JobDetailPage() {
  const params = useParams()
  const jobId = params?.jobId as string
  const [job, setJob] = useState<Job | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const fetchJob = async () => {
      setIsLoading(true)
      setError('')
      try {
        const response = await api.get<Job>(`/jobs/${jobId}`)
        setJob(response.data)
      } catch (err: any) {
        setError(err.response?.data?.detail || 'Failed to load job')
      } finally {
        setIsLoading(false)
      }
    }

    if (jobId) {
      fetchJob()
    }
  }, [jobId])

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gray-50 py-12 px-4">
        <div className="text-center py-12">
          <p className="text-gray-600">Loading job...</p>
        </div>
      </div>
    )
  }

  if (error || !job) {
    return (
      <div className="min-h-screen bg-gray-50 py-12 px-4">
        <div className="max-w-2xl mx-auto">
          <div className="bg-red-50 border border-red-200 p-4 rounded-lg mb-6">
            <p className="text-red-800">{error || 'Job not found'}</p>
          </div>
          <Link href="/owner/jobs" className="text-blue-600 hover:text-blue-700">
            ← Back to Jobs
          </Link>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-2xl mx-auto">
        <Link href="/owner/jobs" className="text-blue-600 hover:text-blue-700 mb-4 inline-block">
          ← Back to Jobs
        </Link>

        <div className="bg-white rounded-lg shadow p-8">
          <div className="mb-6">
            <div className="flex justify-between items-start mb-4">
              <h1 className="text-4xl font-bold text-gray-900">{job.title}</h1>
              <span className="px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
                {job.jobStatus.replace('_', ' ')}
              </span>
            </div>
            <p className="text-gray-600">{job.category}</p>
          </div>

          <div className="grid grid-cols-2 gap-4 mb-8 pb-8 border-b border-gray-200">
            <div>
              <p className="text-gray-500 text-sm">Budget</p>
              <p className="text-2xl font-bold text-gray-900">
                {formatCurrency(job.budgetMin)} - {formatCurrency(job.budgetMax)}
              </p>
            </div>
            <div>
              <p className="text-gray-500 text-sm">Location</p>
              <p className="text-2xl font-bold text-gray-900">{job.location}</p>
            </div>
            {job.timelineDays && (
              <div>
                <p className="text-gray-500 text-sm">Timeline</p>
                <p className="text-2xl font-bold text-gray-900">{job.timelineDays} days</p>
              </div>
            )}
            <div>
              <p className="text-gray-500 text-sm">Posted</p>
              <p className="text-2xl font-bold text-gray-900">{formatDate(job.createdAt)}</p>
            </div>
          </div>

          <div className="mb-8">
            <h3 className="text-xl font-semibold text-gray-900 mb-4">Description</h3>
            <p className="text-gray-700 whitespace-pre-wrap">{job.description}</p>
          </div>

          {job.requiredSkills && job.requiredSkills.length > 0 && (
            <div className="mb-8">
              <h3 className="text-xl font-semibold text-gray-900 mb-4">Required Skills</h3>
              <div className="flex flex-wrap gap-2">
                {job.requiredSkills.map(skill => (
                  <span
                    key={skill}
                    className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          )}

          <div className="flex gap-4">
            <Link
              href={`/owner/jobs/${job.id}/edit`}
              className="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 font-medium text-center"
            >
              Edit Job
            </Link>
            <Link
              href="/owner/jobs"
              className="flex-1 border border-gray-300 text-gray-700 py-2 px-4 rounded-md hover:bg-gray-50 font-medium text-center"
            >
              Back to Jobs
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
