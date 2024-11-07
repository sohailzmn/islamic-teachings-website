import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function Blog() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch('/api/blog')
      .then(res => res.json())
      .then(data => setPosts(data))
      .catch(err => console.error('Error fetching posts:', err));
  }, []);

  return (
    <section className="section-padding">
      <div className="container">
        <h1 className="text-center mb-5">Islamic Reflections & Insights</h1>
        <div className="row g-4">
          {posts.map(post => (
            <div className="col-md-6" key={post.id}>
              <div className="card teaching-card h-100">
                <div className="card-body">
                  <h2 className="card-title h4 mb-3">{post.title}</h2>
                  <p className="card-text">{post.summary}</p>
                  <div className="mt-3">
                    <small className="text-muted">{post.created_at}</small>
                  </div>
                  <Link to={`/blog/${post.id}`} className="btn btn-secondary mt-3">Read More</Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Blog;
