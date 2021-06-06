from flask import render_template,request,redirect,url_for 
from app import app
from .request import get_sources,get_source,search_source



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
    source=get_source(name)
    title=f'{source.name}'
    return render_template('source.html',title=title,source=source)

@app.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the  source search results
    '''
    source_name_list=source_name.split(" ")
    source_name_format="+".join(source_name_list)
    searched_sources=search_source(source_name_format)
    title=f'search result for {source_name}'

    return render_template('search.html',sources=searched_sources)


