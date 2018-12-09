from .. import db, flask_bcrypt

class Stock(db.Model):
    """ Stock Model for storing stock related details """
    __tablename__ = "stock"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    sector = db.Column(db.String(50))
    category = db.Column(db.String(50))
    trackedSince = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Stock '{}'>".format(self.name)