from flask import Flask 
from .config import DevConfig 
from flask_bootstrap import Boostrap

app=Flask(__name__,instance_relative_config=True)

 #setting up configurations 
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')          


#initializing flask extensions
bootstrap =Boostrap(app)

from app import views    





