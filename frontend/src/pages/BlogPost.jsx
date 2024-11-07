import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';

function BlogPost() {
  const [post, setPost] = useState(null);
  const { postId } = useParams();

  useEffect(() => {
    fetch(`/api/blog/${postId}`)
      .then(res => res.json())
      .then(data => setPost(data))
      .catch(err => console.error('Error fetching post:', err));
  }, [postId]);

  if (!post) return <div>Loading...</div>;

  return (
    <section className="section-padding">
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-lg-8">
            <article className="blog-post">
              <h1 className="mb-4">{post.title}</h1>
              <div className="mb-4">
                <small className="text-muted">{post.created_at}</small>
              </div>
              <div className="blog-content" dangerouslySetInnerHTML={{ __html: post.content }}></div>
            </article>
            <div className="mt-5">
              <Link to="/blog" className="btn btn-secondary">← Back to Blog</Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default BlogPost;
