from flask import Blueprint, render_template, request, flash, jsonify, session
from telebot import TeleBot
from . import db
import datetime
import os
# from .telebot import message
# from .icici_login import api_login
try:
    from memory_profiler import profile
    from website import result
    
    import psutil
except Exception as e:
    print('Error in calculation  ::', e)
views = Blueprint('views', __name__)


@profile
@views.route('/home', methods = ['POST', 'GET'])
def test():
    if request.method == 'POST':
        cal1 = int(request.form.get('cal1'))
        cal2 = int(request.form.get('cal2'))
        result1 = result.add_result(cal1, cal2)
        print(result1)
        print(result.rel1.sub_result(cal1, cal2))
    
        # Get the memory usage of the current process
    # memory_info = psutil.virtual_memory()

    # print("Total Memory:", memory_info.total)
    # print("Available Memory:", memory_info.available)
    # print("Used Memory:", memory_info.used)
    # print("Memory Usage Percentage:", memory_info.percent)
    return render_template('first.html')


# @views.route('/',methods= ['GET', 'POST'])
# def home():
#     if request.method == 'POST' and 'first' in request.form:
#         t = TeleBot(token= os.getenv(teleapi))
#         n= os.getenv('sudip')
#         print(n)
        
#         t.send_message(n, f'Hello : {datetime.datetime.now().isoformat()}')
#     # t.mess
#     return render_template('index.html')