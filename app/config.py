class Config:
    '''
    General configurations setting class 
    '''
    pass
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
