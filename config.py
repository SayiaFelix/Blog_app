import os

class Config:
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://mwtvnlerdottey:f8a17940e5c7983fd4ae2999dfa5939498ffbc0cdd0ea2f63620d54647c87807@ec2-54-165-184-219.compute-1.amazonaws.com:5432/dcmp8l9rgi8chs'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jay123@localhost/blogpost'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'SiR Feliz Blogs ::'
    SENDER_EMAIL = 'sayiafelix18@gmail.com'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    #  uri = os.getenv("DATABASE_URL")  
    #  if uri.startswith("postgres://"):
    #     uri = uri.replace("postgres://", "postgresql://", 1)

    #     SQLALCHEMY_DATABASE_URI=uri
  pass
  
class TestConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jaysafu@localhost/blogpost_test'
  

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jay123@localhost/blogpost'
 
DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}