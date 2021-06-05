class Config:
    '''
    General configurations setting class 
    '''
    pass
class ProdConfig(Config):
    '''
    Production configuration settings class
    Args:
         general configuration class from which the child class inherits configurations.
    '''
    pass
class DevConfig(Config):
    '''
    Production configuration settings class
    Args:
         general configuration class from which the child class inherits configurations.
    '''
    DEBUG=True
