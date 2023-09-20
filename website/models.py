from . import db

import datetime

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.Integer)
    second = db.Column(db.Integer)
    uid = db.Column(db.String(150))
    status = db.Column(db.String(10), default = 'due')
    close = db.Column(db.String(50), nullable = True)

class Stock(db.Model):
    __table_name__ = 'stock'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10))
    uid = db.Column(db.String(150))
    num = db.Column(db.String(15))