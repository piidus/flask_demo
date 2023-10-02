from flask import Blueprint, render_template, request, flash, jsonify, session, current_app
from telebot import TeleBot
from . import db
import datetime
import os, uuid
# from .telebot import message
# from .icici_login import api_login
from .models import Test, Stock
try:
    # from memory_profiler import profile
    from website import result
    from website.result import FirstTest #first_func
    
    # import psutil
except Exception as e:
    print('Error in calculation  ::', e)
views = Blueprint('views', __name__)



@views.route('/home', methods = ['POST', 'GET'])
def test():
    # print('I am working')
    if request.method == 'POST' and 'calculated' in request.form:
        cal1 = int(request.form.get('cal1'))
        cal2 = int(request.form.get('cal2'))
        uid = str(uuid.uuid4().int)
        tine_ = request.form.get('time')
        print(tine_)
        # result1 = result.add_result(cal1, cal2)
        # print(result1)
        # print(result.rel1.sub_result(cal1, cal2))
        # use thread with raw sql
           
        t = Test(first = cal1, second = cal2, uid = uid)
        db.session.add(t)
        db.session.commit() 
        # with current_app.app_context().push():
        from main import app
    
        FirstTest(app=app, uid=uid,num1=cal1, num2=cal2, endtime=tine_)
            
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

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected!')

# # Define your Socket.IO events here
# # Example:
# @socketio.on('divisible_event')
# def handle_divisible_event(data):
#     print(f'Divisible event received with data: {data}')
#     # Broadcast the event to all connected clients
#     socketio.emit('divisible_response', {'message': 'A divisible number event occurred!'})

# @views.route('/',methods= ['GET', 'POST'])
# def home():
#     if request.method == 'POST' and 'first' in request.form:
#         t = TeleBot(token= os.getenv(teleapi))
#         n= os.getenv('sudip')
#         print(n)
        
#         t.send_message(n, f'Hello : {datetime.datetime.now().isoformat()}')
#     # t.mess
#     return render_template('index.html')