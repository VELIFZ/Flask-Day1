#genelde hep ayni
# set up and organize the applications general configuration
# what secret variables does it need (secret key, database info, mailer info, api keys, etc.)
# what does it's file structure look like?

# we're gonna get a little help from the os package
import os 

# # set up the base directory of the entire application - aka help our computer figure out our file system and where to find the different pieces of this project
basedir = os.path.abspath(os.path.dirname(__name__))

#config varibales setup
class Config:
    """
    set configuration variables for our entire flask app 
    """
    
    # set names - variables must be the names listed 'FLASK_APP, FLASL_ENV, SECRET_KEY'
    FLASK_APP =  os.environ.get('FLASK_APP') # go get the flask_app value form .env # bu __init__'deki app
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    