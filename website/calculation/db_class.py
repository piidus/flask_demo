# try:
    
#     from flask import current_app, Flask
#     from flask_sqlalchemy import SQLAlchemy
#     from sqlalchemy import text
#     # from website.views import views
#     # from . import db_class 
    
#     # from website.models import Test
# except Exception as e:
#     print('db_class error',e)

# class DatabaseOperation:
#     def __init__(self, uid, table_name,  **kwargs) -> None:
#         self.uid = uid
#         self.table_name = table_name
#         self.search_column = kwargs.get('search_column', '')
#         self.second_column = kwargs.get('second_column', '')
#         self.second_value = kwargs.get('second_value', '')
#         self.status = kwargs.get('status','')
#         self.app = Flask(__name__)
#         self.db = SQLAlchemy()
#         self.app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
#         self.db.init_app(self.app)
#     # Get the db table
#     def get_first_row(self):
        
#         with self.app.app_context():
#                 # Get a database connection
#             conn = self.db.engine.connect()
#             # Access the database using a raw SQL query with text()
#             sql_query = text(f"SELECT * FROM {self.table_name} WHERE {self.search_column} = :name")
#             result = conn.execute(sql_query, {'name': self.uid}).first()
#             conn.close()
#             return result
    
#     # Two parameter
#     def search_by_two_param(self):
#         with self.app.app_context():
#             conn = self.db.engine.connect()
#             # Access the database using a raw SQL query with text()
#             sql_query = text(f"SELECT * FROM {self.table_name} WHERE {self.search_column} = :name AND {self.second_column} = :name2" )
#             result = conn.execute(sql_query, {'name': self.uid, 'name2': self.second_value}).first()
#             conn.close()
#             return result
    
   
#         # with db.app.app_context():
#         #     try:
#         #         conn = db.engine.connect()
#         #     # Access the database using a raw SQL query with text()
            
#         #         sql = text("INSERT INTO stock (status, uid, num) VALUES (:status, :uid, :second)" )
#         #         conn.execute(sql, { 'status': self.status, 'uid': self.uid, 'second': self.second_value} )
#         #         db.session.commit()
#         #         print('Data saved')
#         #     except Exception as e:
#         #         print(e)
        #     finally:
        #         conn.close()
        
