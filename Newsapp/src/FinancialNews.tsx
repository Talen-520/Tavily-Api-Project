import React, { useState } from 'react'
import axios from 'axios'

const FinancialNews: React.FC = () => {
  const [news, setNews] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(false)
  const [company, setCompany] = useState<string>('')
  const [quarter, setQuarter] = useState<string>('')
  const [year, setYear] = useState<string>('')

  const fetchNews = async () => {
    if (!company || !quarter || !year) {
      alert('Please fill in all fields')
      return
    }

    setLoading(true)
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/chat/', {
        company,
        quarter,
        year
      })
      setNews(response.data)
    } catch (error) {
      console.error('Error fetching news:', error)
      setNews('Error fetching news. Please try again.')
    }
    setLoading(false)
  }

  return (
    <div className="financial-news">
      <h1>AI Financial Quarter Earning Analyst</h1>
      <h3 >(Note: please enter valid quarter and year to obtain more accurate result)</h3>
      <div className="input-container">
        <input 
          type="text" 
          placeholder="Company Name" 
          value={company} 
          onChange={(e) => setCompany(e.target.value)}
        />
        <input 
          type="number" 
          placeholder="Quarter (1-4)" 
          value={quarter} 
          onChange={(e) => setQuarter(e.target.value)}
          min="1"
          max="4"
        />
        <input 
          type="number" 
          placeholder="Year" 
          value={year} 
          onChange={(e) => setYear(e.target.value)}
        />
      </div>
      <button onClick={fetchNews} disabled={loading}>
        {loading ? 'Loading...' : 'Get Earning Report'}
      </button>
      {news && (
        <div className="news-content">
          <h2>Analysis:</h2>
          <pre className="formatted-news">{news}</pre>
        </div>
      )}
    </div>
  )
}

export default FinancialNews