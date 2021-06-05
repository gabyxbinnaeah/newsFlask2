from app import app
import urllib.request, json
from .models import article
from .models import source 

Article=article.Article
Source=source.Source


#getting api key 

api_key=app.config['NEWS_API_KEY']

#geting base url

source_url=app.config['NEWS_SOURCES_URL']
source_article_url=app.config['NEWS_SOURCE_API']

