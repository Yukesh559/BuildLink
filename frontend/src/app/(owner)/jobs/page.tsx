'use client'

import { useEffect, useState } from 'react'
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
  createdAt: string
}

interface JobListResponse {
  total: number
  page: number
  page_size: number
  jobs: Job[]
}

export default function JobsPage() {
  const [jobs, setJobs] = useState<Job[]>([])
  const [total, setTotal] = useState(0)
  const [page, setPage] = useState(1)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const fetchJobs = async () => {
      setIsLoading(true)
      setError('')
      try {
        const response = await api.get<JobListResponse>('/jobs/me/jobs', {
          params: {
            skip: (page - 1) * 10,
            limit: 10,
          },
        })
        setJobs(response.data.jobs)
        setTotal(response.data.total)
      } catch (err: any) {
        setError(err.response?.data?.detail || 'Failed to load jobs')
      } finally {
        setIsLoading(false)
      }
    }

    fetchJobs()
  }, [page])

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'open':
        return 'bg-green-100 text-green-800'
      case 'in_progress':
        return 'bg-blue-100 text-blue-800'
      case 'completed':
        return 'bg-gray-100 text-gray-800'
      case 'cancelled':
        return 'bg-red-100 text-red-800'
      default:
        return 'bg-gray-100 text-gray-800'
    }
  }

  const totalPages = Math.ceil(total / 10)

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-6xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900">My Jobs</h1>
          <Link
            href="/owner/jobs/create"
            className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 font-medium"
          >
            Post New Job
          </Link>
        </div>

        {error && (
          <div className="bg-red-50 border border-red-200 p-4 rounded-lg mb-6">
            <p className="text-red-800">{error}</p>
          </div>
        )}

        {isLoading ? (
          <div className="text-center py-12">
            <p className="text-gray-600">Loading jobs...</p>
          </div>
        ) : jobs.length === 0 ? (
          <div className="bg-white rounded-lg shadow p-12 text-center">
            <p className="text-gray-600 mb-4">You haven't posted any jobs yet.</p>
            <Link
              href="/owner/jobs/create"
              className="inline-block bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700"
            >
              Post Your First Job
            </Link>
          </div>
        ) : (
          <>
            <div className="space-y-4">
              {jobs.map(job => (
                <div key={job.id} className="bg-white rounded-lg shadow p-6">
                  <div className="flex justify-between items-start mb-4">
                    <div>
                      <h3 className="text-xl font-semibold text-gray-900">{job.title}</h3>
                      <p className="text-gray-600 text-sm mt-1">{job.category}</p>
                    </div>
                    <span className={`px-3 py-1 rounded-full text-sm font-medium ${getStatusColor(job.jobStatus)}`}>
                      {job.jobStatus.replace('_', ' ')}
                    </span>
                  </div>

                  <p className="text-gray-600 mb-4 line-clamp-2">{job.description}</p>

                  <div className="grid grid-cols-3 gap-4 mb-4 text-sm">
                    <div>
                      <p className="text-gray-500">Budget</p>
                      <p className="font-semibold text-gray-900">
                        {formatCurrency(job.budgetMin)} - {formatCurrency(job.budgetMax)}
                      </p>
                    </div>
                    <div>
                      <p className="text-gray-500">Location</p>
                      <p className="font-semibold text-gray-900">{job.location}</p>
                    </div>
                    <div>
                      <p className="text-gray-500">Posted</p>
                      <p className="font-semibold text-gray-900">{formatDate(job.createdAt)}</p>
                    </div>
                  </div>

                  <div className="flex gap-2">
                    <Link
                      href={`/owner/jobs/${job.id}`}
                      className="flex-1 bg-blue-50 text-blue-600 px-4 py-2 rounded hover:bg-blue-100 text-center font-medium"
                    >
                      View Details
                    </Link>
                    <Link
                      href={`/owner/jobs/${job.id}/edit`}
                      className="flex-1 bg-gray-100 text-gray-700 px-4 py-2 rounded hover:bg-gray-200 text-center font-medium"
                    >
                      Edit
                    </Link>
                  </div>
                </div>
              ))}
            </div>

            {totalPages > 1 && (
              <div className="flex justify-center gap-2 mt-8">
                <button
                  onClick={() => setPage(p => Math.max(1, p - 1))}
                  disabled={page === 1}
                  className="px-4 py-2 border border-gray-300 rounded-lg disabled:opacity-50"
                >
                  Previous
                </button>
                <div className="flex items-center gap-2">
                  {Array.from({ length: totalPages }, (_, i) => i + 1).map(p => (
                    <button
                      key={p}
                      onClick={() => setPage(p)}
                      className={`px-3 py-1 rounded-lg ${
                        p === page
                          ? 'bg-blue-600 text-white'
                          : 'border border-gray-300 text-gray-700 hover:bg-gray-100'
                      }`}
                    >
                      {p}
                    </button>
                  ))}
                </div>
                <button
                  onClick={() => setPage(p => Math.min(totalPages, p + 1))}
                  disabled={page === totalPages}
                  className="px-4 py-2 border border-gray-300 rounded-lg disabled:opacity-50"
                >
                  Next
                </button>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  )
}
