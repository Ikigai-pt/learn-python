from flask_restplus import Namespace, fields


class StockDto:
    api = Namespace('stock', description='stock related operations')
    stock = api.model('stock', {
        'symbol': fields.String(required=True, description='stock symbol'),
        'name': fields.String(required=True, description='stock name'),
        'price': fields.String(required=True, description='stock price'),
        'sector': fields.String(required=True, description='stock sector'),
        'category': fields.String(description='stock category')
    })