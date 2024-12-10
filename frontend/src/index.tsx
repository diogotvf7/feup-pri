import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import SearchPage from './pages/SearchPage'
import reportWebVitals from './reportWebVitals'
import ArticlePage from './pages/ArticlePage'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Test from './pages/Test'

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement)

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<SearchPage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/article/:article" element={<ArticlePage />} />
        <Route path="/test" element={<Test />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()
