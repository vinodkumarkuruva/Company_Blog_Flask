import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)

app.config['SECRET_KEY']='MYKEY'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir+'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIICATIONS'] = False

# postgresql://username:password@host:port/database_name

db = SQLAlchemy(app)
Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='users.login'


from puppycompanyblog.core.views import core 
app.register_blueprint(core)

from puppycompanyblog.users.views import users
app.register_blueprint(users)

from puppycompanyblog.error_pages.handlers import error_pages 
app.register_blueprint(error_pages)

from puppycompanyblog.blog_posts.views import blog_posts
app.register_blueprint(blog_posts)

from .models import User,BlogPost

with app.app_context():
    db.create_all()