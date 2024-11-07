from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import markdown
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    summary = db.Column(db.String(300))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': markdown.markdown(self.content),
            'created_at': self.created_at.strftime('%B %d, %Y'),
            'summary': self.summary
        }

@app.route('/api/content')
def get_content():
    biography = {
        'name': 'Sohailzamn',
        'title': 'Sharing Islamic Content & Reflections',
        'description': 'Exploring and sharing the beauty of Islam through personal experiences and reflections.',
        'long_description': 'As a passionate Muslim content creator, I share my personal journey and insights about Islam. Through my blog posts and social media content, I aim to connect with fellow Muslims, sharing experiences and reflections that help us grow in our faith together.'
    }
    
    teachings = [
        {
            'title': 'Daily Life & Faith',
            'description': 'Practical guidance on applying Islamic principles in everyday situations.'
        },
        {
            'title': 'Modern Challenges',
            'description': 'Addressing contemporary issues through an Islamic perspective.'
        },
        {
            'title': 'Personal Growth',
            'description': 'Developing character and spirituality in the modern world.'
        }
    ]
    
    social_media = {
        'youtube': 'https://youtube.com/sohailzamn',
        'instagram': 'https://instagram.com/sohailzamn',
        'twitter': 'https://twitter.com/sohailzamn'
    }
    
    recent_posts = [post.to_dict() for post in BlogPost.query.order_by(BlogPost.created_at.desc()).limit(3).all()]
    
    return jsonify({
        'biography': biography,
        'teachings': teachings,
        'social_media': social_media,
        'recent_posts': recent_posts
    })

@app.route('/api/blog')
def get_blog_posts():
    posts = [post.to_dict() for post in BlogPost.query.order_by(BlogPost.created_at.desc()).all()]
    return jsonify(posts)

@app.route('/api/blog/<int:post_id>')
def get_blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return jsonify(post.to_dict())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
