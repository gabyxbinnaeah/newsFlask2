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

    get_sourceurl=source_url.formart(api_key)
    with urllib.request.urlopen(get_sourceurl) as url:
        get_sources_data=url.read()
        get_sources_response=json.loads(get_sources_data)

        source_results=None 

        if get_sources_response['sources']:
            source_result_list=get_sources_response['sources']
            source_results=process_results(source_result_list)



    return source_results
