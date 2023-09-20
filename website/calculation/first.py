def add(x, y):
    print('This is from first')
    return x+y
# from website.__init__ import db
from website.models import Stock
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker



def sample_save(status, uid, second_value):
    try:
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        print('--------------')
        # print(Stock())
        try:
            new_data = Stock(status=status,uid = uid, num=second_value)
            session = Session()
            session.add(new_data)
            session.commit()
            # # s = Stock(status = status, uid = uid, num = second_value)
            # sql_query = text("INSERT INTO stock (status, uid, num) VALUES (:status,:uid,:num)")
            # with engine.connect() as conn:
            #     conn.execute(sql_query, {'status': status, 'uid':uid, 'num': second_value})
        except Exception as e:
            print('here is prob', e)
        print('--****************------')
        return True
    except Exception as e:
        print(e)