from sqlalchemy.orm import backref
from . import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(24), unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(24), nullable=False)
    transactions = db.relationship('Transactions', backref='sender', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}','{self.email}')"


class Transactions(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    time = db.Column(db.DateTime, default=datetime.utcnow())
    amount_btc = db.Column(db.Float, nullable=False)
    amount_ksh = db.Column(db.Float, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    wallet_addr = db.Column(db.String(64), nullable=False)
    transaction_id = db.Column(db.String(64), nullable=False, primary_key=True)

    def __repr__(self) -> str:
        return f"Transaction('{self.time}','{self.transaction_id}','{self.amount_btc}','{self.amount_ksh}','{self.phone_number}','{self.wallet_addr}')"
