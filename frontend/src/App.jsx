import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import Home from './pages/Home'
import Blog from './pages/Blog'
import BlogPost from './pages/BlogPost'
import './styles/custom.css'

function App() {
  return (
    <>
      <div className="islamic-pattern">
        <img src="/images/geometric-pattern.svg" alt="Islamic Pattern" />
      </div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/blog" element={<Blog />} />
        <Route path="/blog/:postId" element={<BlogPost />} />
      </Routes>
      <Footer />
    </>
  )
}

export default App
