from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    returns that template pages
    '''

    return render_template('index.html')
    