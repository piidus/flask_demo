
try:
    import threading, time
    from flask import current_app, Flask
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import text
    # from main import app
    # from website import db
    # from website.models import Test
except Exception as e:
    print(e)
def first_test(first, second):
    print(first, second)
class FirstTest:
    def __init__(self, first, second, uid) -> None:
        self.first = first
        self.second = second
        self.uid = uid
        self.round = 0
        self.start = self.first_test()

    def test(self):
        time.sleep(3)
        print('Thread is working = ::', self.round)
        if self.round<=3:
            self.round += 1
            app = Flask(__name__)
            db = SQLAlchemy()
            app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
            db.init_app(app)
            with app.app_context():
                 # Get a database connection
                conn = db.engine.connect()
                # Access the database using a raw SQL query with text()
                sql_query = text("SELECT * FROM test WHERE uid = :name")
                result = conn.execute(sql_query, {'name': self.uid}).fetchone()
                
                conn.close()
            # db.session.
                if result != None:
                    print(result.status)
                    if result.status == 'due':
                        threading.Timer(3, function=self.test).start()
                    else:
                        print('it force close')
                else:
                    print('no due')

    def first_test(self):
        print(self.first, self.second, self.uid)
        threading.Thread(target=self.test).start()
