import os


class Config:
    '''
    Parent configuration class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json (Links to an external site.)'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:7166@localhost/watchlist'

class DevConfig(Config):
    '''
    Child configuration class

    Args:
        Config:takes the configuration child class as an argument 
    '''

    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: takes the parent configuration class as an argument
    '''


config_options={
    'development':DevConfig,
    'production':ProdConfig
}