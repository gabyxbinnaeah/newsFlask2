from flask import render_template
from app import app
from .request import get_sources

sourceSamples =get_sources()

@app.route('/')
def index():
    '''
    returns that template pages
    '''

    title="Home -News site"
    return render_template('index.html',title=title, sourceList=sourceSamples)


