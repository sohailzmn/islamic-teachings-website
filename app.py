from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import markdown
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    summary = db.Column(db.String(300))

    def content_html(self):
        return markdown.markdown(self.content)

@app.route('/')
def index():
    # Content for the website
    biography = {
        'name': 'Sohailzamn',
        'title': 'Content Creator sharing Islamic knowledge',
        'description': 'Making Islamic teachings accessible and relatable through modern content creation.',
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
    
    return render_template('index.html', 
                         biography=biography,
                         teachings=teachings,
                         social_media=social_media)

@app.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('blog_post.html', post=post)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
