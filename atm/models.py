from datetime import datetime
from atm import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    account_number = db.Column(db.String(11), unique = True, nullable = False)
    account_balance = db.Column(db.Numeric, unique = True, nullable = False)
    profile_pic = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    pin = db.Column(db.String(60), unique = True, nullable = False)
    type_acc = db.Column(db.String(7), nullable = False)
    transactions = db.relationship('Transaction', backref = 'user', lazy = True)

    def __repr__(self):
        return f"User('{self.name}', '{self.account_number}', '{self.profile_pic}', '{self.account_balance}', '{self.type_acc}')"
    
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type_trans = db.Column(db.String(8), nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    prev_balance = db.Column(db.Numeric, nullable = False)
    curr_balance = db.Column(db.Numeric, nullable = False)
    amount = db.Column(db.Numeric, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Transaction('{self.type_trans}', '{self.date}', '{self.prev_balance}', '{self.amount}', '{self.curr_balance}')"