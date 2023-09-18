from flask import Blueprint, render_template, request, flash, jsonify, session
from telebot import TeleBot
from . import db
import datetime
import os, uuid
# from .telebot import message
# from .icici_login import api_login
from .models import Test
try:
    from memory_profiler import profile
    from website import result
    from website.result import first_test, FirstTest
    
    import psutil
except Exception as e:
    print('Error in calculation  ::', e)
views = Blueprint('views', __name__)


@profile
@views.route('/home', methods = ['POST', 'GET'])
def test():
    # print('I am working')
    if request.method == 'POST' and 'calculated' in request.form:
        cal1 = int(request.form.get('cal1'))
        cal2 = int(request.form.get('cal2'))
        uid = str(uuid.uuid4().int)
        # result1 = result.add_result(cal1, cal2)
        # print(result1)
        # print(result.rel1.sub_result(cal1, cal2))
        # use thread with raw sql
        first_test(cal1, cal2)   
        t = Test(first = cal1, second = cal2, uid = uid)
        db.session.add(t)
        db.session.commit() 
        FirstTest(first=cal1, second=cal2, uid=uid )
        # Get the memory usage of the current process
    # memory_info = psutil.virtual_memory()

    # print("Total Memory:", memory_info.total)
    # print("Available Memory:", memory_info.available)
    # print("Used Memory:", memory_info.used)
    # print("Memory Usage Percentage:", memory_info.percent)
    # Delete the id
    if request.method == 'POST' and 'uni_id' in request.form:
        uid_ = request.form.get('uni_id')
        print(uid_)
        t = Test.query.filter_by(uid = uid_).first()
        if 'delete' in request.form:
            db.session.delete(t)
            db.session.commit()
        elif 'stop' in request.form:
            t.status = 'done'
            db.session.commit()
    test = Test.query.all()
    data ={'test':test}
    return render_template('first.html', data= data)


# @views.route('/',methods= ['GET', 'POST'])
# def home():
#     if request.method == 'POST' and 'first' in request.form:
#         t = TeleBot(token= os.getenv(teleapi))
#         n= os.getenv('sudip')
#         print(n)
        
#         t.send_message(n, f'Hello : {datetime.datetime.now().isoformat()}')
#     # t.mess
#     return render_template('index.html')