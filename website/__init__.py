from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
# from flask_socketio import SocketIO
from sqlalchemy import create_engine
# engine = create_engine('mysql://piidusi1_piidusi1:C(6q3!b3JtCj9K@Python01/piidusi1_test', encoding='utf-8')

load_dotenv('.env')

# socketio = SocketIO()
db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_name = os.getenv('DB_NAME')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pass}@103.185.74.60:3306/{db_name}'
    # 'mysql://username:password@remote_hostname/database_name'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Set the time zone to Asia/Kolkata
    app.config['TIME_ZONE'] = 'Asia/Kolkata'
    db.init_app(app)
    # socketio.init_app(app=app)


    from .views import views

    app.register_blueprint(views, url_prefix='/')
    

    # from .models import User, Note
    
    with app.app_context():
        db.create_all()
        

    return app
