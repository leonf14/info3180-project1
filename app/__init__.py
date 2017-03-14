from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
#from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "random key"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pro1@localhost/pro1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

#Flask-Login login manager
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view='logi

import logging
import sys




app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)




app.config.from_object(__name__)
from app import views, models
