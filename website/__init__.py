from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv('.env')


db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Set the time zone to Asia/Kolkata
    app.config['TIME_ZONE'] = 'Asia/Kolkata'
    db.init_app(app)



    from .views import views

    app.register_blueprint(views, url_prefix='/')
    

    # from .models import User, Note
    
    with app.app_context():
        db.create_all()
        

    return app
