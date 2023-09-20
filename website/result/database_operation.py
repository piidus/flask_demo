
try:
    import threading, time    
    import datetime    
    from website import db   
    from website.models import Stock, Test
except Exception as e:
    print(e, 'database operation')
def first_test(first, second):
    print(first, second)
class FirstTest:
    def __init__(self, app, uid, num1, num2, endtime:str) -> None:
        self.__app = app
        self.__uid = uid
        self.__num1 = num1
        self.__num2 = num2
        self.__end_time:str = endtime.split(':')
        self.count = 0
        self.first_run()

    def super_close(self):
        hh = int(self.__end_time[0])
        mm = int(self.__end_time[1])
        now = datetime.datetime.now()
        target_time = now.replace(hour=hh, minute=mm)
        # print(target_time)
        if target_time > now:
            print(target_time, self.count)
            # print(now)

        else:
            print('it\'s a past time')
    def filter_status(self):
        with self.__app.app_context():
            qu = Test.query.filter_by(uid = self.__uid).first()
            if qu:
                print(qu.status)
            else:
                print('None')
    def first(self):
        t = self.super_close()
        if self.count == 0:
            with self.__app.app_context():
                s = Stock(status ='run', uid = self.__uid, num = self.__num1)
                db.session.add(s)
                db.session.commit()

            threading.Timer(3, function=self.filter_status).start()
            threading.Timer(3, function=self.first).start()
        elif (self.count > 0) and (self.count < 5):
            
            threading.Timer(3, function=self.filter_status).start()
            threading.Timer(3, function=self.first).start()
        elif self.count == 5:
            with self.__app.app_context():
                s = Stock.query.filter_by(uid = self.__uid).first()
                s.status = 'done'
                db.session.commit()
                time.sleep(1)
            threading.Timer(3, function=self.first).start()
        else:
            threading.Timer(3, function=self.filter_status).start()
            print('completed')
        self.count += 1
    def first_run(self):
        threading.Thread(target=self.first).start()

lock = threading.Lock()
counter = 5
def test(cal1, uid, app, model, db1, model2):
    global counter
    # with lock:
    counter -=1
    print('i am working : ',counter, cal1, uid)
    if counter > 0:
        with app.app_context():
            t = model.query.filter_by(uid = uid).first()
            print(t.status)
        threading.Timer(3, function=test, args=[cal1, uid, app, model, db1, model2]).start()
    else:
        try:
            with app.app_context():
                t = model.query.filter_by(uid = uid).first()
                t.status = 'done'
                db1.session.commit()
                print('database edited')
        except Exception as e:
            print(e, '------------here')
def first_func(cal1, uid, model, db1, app, model2):
    
    with app.app_context():
        m  = Stock(status = 'run', uid = uid, num = cal1)
        db.session.add(m)
        db.session.commit()
        # print(current_app._get_exc_class_and_code)
        # print(current_app._get_current_object())
        t = threading.Thread(target=test, args=[cal1, uid, app,  model, db, model2]) 
        t.start()
        # current_app._get_current_object()