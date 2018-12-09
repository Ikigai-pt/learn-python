from flask import request
from flask_restplus import Resource

from ..util.dto import StockDto
from ..service.stock_service import save_new_stock, get_all_stocks, get_a_stock

api = StockDto.api
_stock = StockDto.stock


@api.route('/')
class StockList(Resource):
    @api.doc('list_of_registered_stocks')
    @api.marshal_list_with(_stock, envelope='data')
    def get(self):
        """List all registered stocks"""
        return get_all_stocks()

    @api.response(201, 'Stock successfully created.')
    @api.doc('create a new stock')
    @api.expect(_stock, validate=True)
    def post(self):
        """Creates a new Stock """
        data = request.json
        return save_new_stock(data=data)


@api.route('/<symbol>')
@api.param('symbol', 'The Stock identifier')
@api.response(404, 'Stock not found.')
class Stock(Resource):
    @api.doc('get a stock')
    @api.marshal_with(_stock)
    def get(self, symbol):
        """get a stock given its identifier"""
        stock = get_a_stock(symbol)
        if not stock:
            api.abort(404)
        else:
            return stock