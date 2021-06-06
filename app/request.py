from app import app
import urllib.request, json
from .models import article
from .models import source 

Article=article.Article
Source=source.Source


#getting api key 

api_key=app.config['NEWS_API_KEY']

#geting base url

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


def get_source(api_key):
    get_source_details_url=source_url.format(api_key)
    with urllib.urlopen(get_source_details_url) as url:
        source_details_data=url.read()
        source_details_response=json.loads(source_details_data)

        source_object=None
        if source_details_response:
            name=source_details_response.get('name')
            description=source_details_response.get('description')
            url=source_details_response.get('url')
            category=source_details_response.get('category')

            source_object=Source(id,name,description,url,category)

    return source_object


def sear_source(source_name):
    search_source_url='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(source_name,api_key)
    with urllib.urlopen(search_source_url)as url:
        search_source_data=url.read()
        search_source_response=json.loads(search_source_data)

        search_source_results=None

        if search_source_response['sources']:
            search_source_list=search_source_response['sources']
            search_source_results=process_results(search_source_list)
    
    return search_source_results


