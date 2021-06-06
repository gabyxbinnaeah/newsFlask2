from flask import render_template
from app import app
from .request import get_sources,get_source



@app.route('/')
def index():
    '''
    returns that template pages
    '''
   
    sourceSamples =get_sources()

    title="Home -News site"
    return render_template('index.html',title=title, sourceList= sourceSamples)


@app.route('/source/<id>')
def source(id):
    '''
    View source page function that returns the source details page and its data
    '''
    source=get_source(id)
    title=f'{source.title}'
    return render_template('source.html',title=title,source=source)

