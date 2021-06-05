from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    returns that template pages
    '''
    
    title="Home -News site"
    return render_template('index.html',title=title)


