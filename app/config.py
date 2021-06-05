class Config:
    '''
    General configurations setting class 
    '''
    NEWS_SOURCE_API='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_SOURCES_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
class ProdConfig(Config):
    '''

    Args:
         general configuration class from which the child class inherits configurations settings.
    '''
    pass
class DevConfig(Config):
    '''
    development configuration settings class
    Args:
         general configuration class from which the child class inherits configurations settings.
    '''
    DEBUG=True
