#genelde hep ayni
# setup and organize the applications general configuration

import os 

#
# bilgisyarin file absolutepath 
basedir = os.path.abspath(os.path.dirname(__name__))

#config varibales setup
class Config:
    """
    set 
    """
    
    # set names - variables must be the names listed 'FLASK_APP, FLASL_ENV, SECRET_KEY'
    FLASK_APP =  os.environ.get('FLASK_APP') # go get the flask_app value form .env # bu __init__'deki app
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    