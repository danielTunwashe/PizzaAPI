import os
from decouple import config
from datetime import timedelta



BASE_DIR=os.path.dirname(os.path.realpath(__file__))



class Config:
    SECRET_KEY=config('SECRET_KEY','secret')
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_SECRET_KEY=config('JWT_SECRET_KEY')
    
    
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR,'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG=True
    SQLALCHEMY_ECHO=True
    
    
    
class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI='sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=config('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUF=config('DEBUG', cast=bool)

config_dict={
    'dev' : DevConfig,
    'prod' : ProdConfig,
    'test' : TestConfig
}