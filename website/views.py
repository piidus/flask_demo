from flask import Blueprint, render_template, request, flash, jsonify, session
from telebot import TeleBot
from . import db
import datetime
import os
# from .telebot import message
# from .icici_login import api_login

views = Blueprint('views', __name__)


@views.route('/',methods= ['GET', 'POST'])
def home():
    if request.method == 'POST' and 'first' in request.form:
        t = TeleBot(token= '6045365738:AAFJXULGdym7748jtVk5ksrgdDfGVoJeEeM')
        n= os.getenv('sudip')
        print(n)
        
        t.send_message(n, f'Hello : {datetime.datetime.now().isoformat()}')
    # t.mess
    return render_template('index.html')