import React, { useState, useEffect } from 'react';

function Home() {
  const [content, setContent] = useState(null);

  useEffect(() => {
    fetch('/api/content')
      .then(res => res.json())
      .then(data => setContent(data))
      .catch(err => console.error('Error fetching content:', err));
  }, []);

  if (!content) return <div>Loading...</div>;

  return (
    <>
      <section className="hero-section text-center">
        <div className="container">
          <h1 className="bismillah mb-5" style={{ fontFamily: 'Amiri, serif', fontSize: '3rem' }}>
            بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ
          </h1>
          <h2 className="display-2 mb-4">{content.biography.name}</h2>
          <h3 className="h2 mb-4">{content.biography.title}</h3>
          <p className="lead mb-4">{content.biography.description}</p>
        </div>
      </section>

      <div className="section-divider"></div>

      <section id="biography" className="section-padding">
        <div className="container">
          <div className="row justify-content-center">
            <div className="col-md-8">
              <p className="lead text-center">
                {content.biography.long_description}
              </p>
            </div>
          </div>
        </div>
      </section>

      <div className="section-divider"></div>

      <section id="recent-posts" className="section-padding">
        <div className="container">
          <h2 className="text-center h1 mb-5">Recent Posts</h2>
          <div className="row g-4">
            {content.recent_posts.map(post => (
              <div className="col-md-4" key={post.id}>
                <div className="card teaching-card h-100">
                  <div className="card-body">
                    <h3 className="card-title h4 mb-3">{post.title}</h3>
                    <p className="card-text">{post.summary}</p>
                    <div className="mt-3">
                      <small className="text-muted">{post.created_at}</small>
                    </div>
                    <a href={`/blog/${post.id}`} className="btn btn-secondary mt-3">Read More</a>
                  </div>
                </div>
              </div>
            ))}
          </div>
          <div className="text-center mt-5">
            <a href="/blog" className="btn btn-secondary">View All Posts</a>
          </div>
        </div>
      </section>

      <div className="section-divider"></div>

      <section id="contact" className="section-padding">
        <div className="container text-center">
          <h2 className="h1 mb-5">Connect With Me</h2>
          <div className="social-links">
            {Object.entries(content.social_media).map(([platform, url]) => (
              <a key={platform} href={url} target="_blank" rel="noopener noreferrer" className="social-icon">
                <i className={`fab fa-${platform}`}></i>
              </a>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}

export default Home;
