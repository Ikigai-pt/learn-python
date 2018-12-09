import uuid
import datetime

from app.main import db
from app.main.model.stock import Stock


def save_new_stock(data):
    stock = Stock.query.filter_by(symbol=data['symbol']).first()
    if not stock:
        new_stock = Stock(
            symbol=data['symbol'],
            price=data['price'],
            category=data['category'],
            sector=data['sector'],
            name=data['name'],
            trackedSince=datetime.datetime.utcnow()
        )
        save_changes(new_stock)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Stock already exists.',
        }
        return response_object, 409


def get_all_stocks():
    return Stock.query.all()


def get_a_stock(symbol):
    return Stock.query.filter_by(symbol=symbol).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()