from . import db


class User(db.Model):
    id = int()
    email = str()
    username = str()
    password = str()


class Transactions(db.Model):
    id = int()

    time = int()
    amount = float()
    phone_number = int()
    wallet_addr = str()
    transaction_id = str()
