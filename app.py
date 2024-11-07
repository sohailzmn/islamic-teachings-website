from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
