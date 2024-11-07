import os
import shutil
from flask_frozen import Freezer
from app import app, BlogPost, db

freezer = Freezer(app)

# Clean build directory if it exists
if os.path.exists('build'):
    shutil.rmtree('build')
os.makedirs('build')

# URL generators for dynamic routes
@freezer.register_generator
def blog_post():
    with app.app_context():
        posts = BlogPost.query.all()
        for post in posts:
            yield {'post_id': post.id}

@freezer.register_generator
def blog():
    # Generate the /blog route
    yield {}

@freezer.register_generator
def static():
    # Register static files
    yield {"filename": "css/custom.css"}
    yield {"filename": "js/main.js"}
    yield {"filename": "images/geometric-pattern.svg"}

if __name__ == '__main__':
    # Configure Freezer
    app.config['FREEZER_DESTINATION'] = 'build'
    app.config['FREEZER_RELATIVE_URLS'] = True
    app.config['FREEZER_REMOVE_EXTRA_FILES'] = True
    
    # Generate static files
    with app.app_context():
        freezer.freeze()
