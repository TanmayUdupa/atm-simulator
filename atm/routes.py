from flask import render_template, url_for, flash, redirect, request
from atm import app, bcrypt
from atm.forms import LoginForm
from atm.models import User, Transaction
from flask_login import login_user, current_user, logout_user, login_required

transactions = [
    {
        'type': 'Withdraw',
        'owner': 'Corey Schafer',
        'amount': 50,
        'prev_balance': 2550,
        'curr_balance': 2500,
        'date': '20-04-2023'
    },
    {
        'type': 'Deposit',
        'owner': 'Jane Doe',
        'amount': 50,
        'prev_balance': 3000,
        'curr_balance': 3050,
        'date': '18-08-2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/view_transactions")
@login_required
def view_transactions():
    return render_template('view_transactions.html', transactions=transactions)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(account_number = form.account_number.data).first()
        if user and bcrypt.check_password_hash(user.pin, form.pin.data):
            login_user(user, remember = False)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check account number and pin', 'danger')
    return render_template('login.html', title = 'Login', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))