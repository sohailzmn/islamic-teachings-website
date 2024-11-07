from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Content for the website
    biography = {
        'name': 'Sohailzamn',
        'title': 'Islamic Teacher & Content Creator',
        'description': 'Dedicated to spreading the message of Islam through authentic teachings and modern content creation.',
    }
    
    teachings = [
        {
            'title': 'Quranic Studies',
            'description': 'In-depth exploration of Quranic verses and their practical application in daily life.'
        },
        {
            'title': 'Islamic Ethics',
            'description': 'Understanding and implementing Islamic moral values in contemporary society.'
        },
        {
            'title': 'Prophetic Traditions',
            'description': 'Learning from the life and teachings of Prophet Muhammad (peace be upon him).'
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
