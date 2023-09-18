try:
    
    from flask import current_app, Flask
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import text
    # from main import app
    # from website import db
    # from website.models import Test
except Exception as e:
    print('db_class error',e)

class DatabaseOperation:
    def __init__(self, uid) -> None:
        self.uid = uid
    def get_first_row(self):
        app = Flask(__name__)
        db = SQLAlchemy()
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
        db.init_app(app)
        with app.app_context():
                # Get a database connection
            conn = db.engine.connect()
            # Access the database using a raw SQL query with text()
            sql_query = text("SELECT * FROM test WHERE uid = :name")
            result = conn.execute(sql_query, {'name': self.uid}).first()
            conn.close()
            return result