from flask import render_template
from app import app
from .request import get_sources



@app.route('/')
def index():
    '''
    returns that template pages
    '''
    sourceSamples =get_sources()

    title="Home -News site"
    return render_template('index.html',title=title, sourceList= sourceSamples)


