from flask import render_template,request,redirect,url_for 
from . import main
from ..request import get_sources,get_articles 



@main.route('/')
def index():
    '''
    view root page function that returns the template pages
    '''
   
    sourceSamples =get_sources()
    

    title="Home -News site"
    
      
    
    return render_template('index.html',title=title, sourceList= sourceSamples)

@main.route('/article/<id>')
def article(id):
    '''
    view root page function that returns the template pages
    '''

    source_articles=get_articles(id)

    return render_template('article.html', articleList=source_articles)








