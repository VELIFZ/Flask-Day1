# imports at the op of any necessart modules/files/classes/packages/functions - 
# from the flask package import the Flask  object/class
from flask import Flask
#from config.py import the co=infig class that we cretaed
from config import Config

# define/instantiate or Flask object.. aka tell the computer thet this is a flask app
app = Flask(__name__) # tells flask what we name the object, and it is app

# tell this app how it should be configure(like it's development flask app, or has password etc)
  #-over to the config.py file to set up for this!
# 2 step of configuration before we tye to app object -- in config.py
app.config.from_object(Config)
# aka configure our flask app from the Congig object we just wrote

#buraya kadar content yok ama flask app'imiz var- yani run edebiliriz ama icinde bir sey olmadigi icin error alabiliriz
