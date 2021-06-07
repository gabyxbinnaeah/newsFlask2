import urllib.request, json
from .models import Article,Source

 #getting api key 
api_key=None


#geting base url

source_url=None  
source_article_url=None

def configure_request(app):
    global api_key,source_url,source_article_url
    api_key = app.config['NEWS_API_KEY']
    source_url=app.config['NEWS_SOURCE_API']
    source_article_url=app.config['NEWS_SOURCES_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''

    get_sourceurl=source_url.format(api_key)
    with urllib.request.urlopen(get_sourceurl) as url:
        get_sources_data=url.read()
        get_sources_response=json.loads(get_sources_data)

        source_results=None 

        if get_sources_response['sources']:
            source_result_list=get_sources_response['sources']
            source_results=process_results(source_result_list)



    return source_results


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results= []

    for source_items in source_list:
        id=source_items.get('id')
        name=source_items.get('name')
        description=source_items.get('description')
        url=source_items.get('url')
        category=source_items.get('category')

        new_source=Source(id,name,description,url,category)

        source_results.append(new_source)

    return source_results


def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url=source_article_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data=url.read()
        get_articles_response=json.loads(get_articles_data)

        article_result=None

        if get_articles_response['articles']:
            article_result_list=get_articles_response['articles']
            article_results=process_result(article_result_list) 

    return article_results 

def process_result(article_list):
    
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
             movie_results: A list of movie objects
    '''

    article_results=[]
    for article_result in article_list:
        id=article_result.get('id')
        author=article_result.get('author')
        title=article_result.get('title')
        description=article_result.get('description')
        url=article_result.get('url')
        urlToImage=article_result.get('urlToImage') 
        publishedAt=article_result.get('publishedAt')
        content=article_result.get('content')

        
        article_object=Article(id,author,title,description,url,urlToImage,publishedAt,content)

        article_results .append(article_object)
    return article_results 




            
    
         














