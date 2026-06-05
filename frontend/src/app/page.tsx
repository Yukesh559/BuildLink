'use client'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Navigation */}
      <nav className="border-b border-gray-200 bg-white">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="flex h-16 justify-between items-center">
            <div className="flex items-center">
              <h1 className="text-2xl font-bold text-blue-600">BuildLink</h1>
            </div>
            <div className="flex gap-4">
              <a href="/login" className="text-gray-600 hover:text-gray-900">
                Login
              </a>
              <a href="/register/owner" className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
                Get Started
              </a>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center">
          <h2 className="text-5xl font-bold text-gray-900 mb-6">
            Connect Directly with Construction Professionals
          </h2>
          <p className="text-xl text-gray-600 mb-12 max-w-2xl mx-auto">
            BuildLink eliminates middlemen and connects house owners directly with skilled construction workers for faster, more affordable projects.
          </p>
          <div className="flex gap-4 justify-center">
            <a href="/register/owner" className="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 text-lg font-semibold">
              I'm a House Owner
            </a>
            <a href="/register/worker" className="bg-gray-200 text-gray-900 px-8 py-3 rounded-lg hover:bg-gray-300 text-lg font-semibold">
              I'm a Construction Worker
            </a>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="bg-gray-50 py-20">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <h3 className="text-3xl font-bold text-center text-gray-900 mb-12">
            How BuildLink Works
          </h3>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-lg shadow-sm">
              <div className="text-4xl font-bold text-blue-600 mb-4">1</div>
              <h4 className="text-xl font-semibold text-gray-900 mb-3">
                Post Your Job
              </h4>
              <p className="text-gray-600">
                Post your construction job with details, budget, and timeline.
              </p>
            </div>
            <div className="bg-white p-8 rounded-lg shadow-sm">
              <div className="text-4xl font-bold text-blue-600 mb-4">2</div>
              <h4 className="text-xl font-semibold text-gray-900 mb-3">
                Receive Bids
              </h4>
              <p className="text-gray-600">
                Get bids from qualified workers in your area. Compare and chat directly.
              </p>
            </div>
            <div className="bg-white p-8 rounded-lg shadow-sm">
              <div className="text-4xl font-bold text-blue-600 mb-4">3</div>
              <h4 className="text-xl font-semibold text-gray-900 mb-3">
                Pay & Review
              </h4>
              <p className="text-gray-600">
                Pay securely through the platform and leave reviews to build trust.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-center">
          <p>&copy; 2024 BuildLink. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}
