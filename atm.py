from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c02b344bb1ba461b033bb918540bcfd8'

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
def view_transactions():
    return render_template('view_transactions.html', transactions=transactions)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.account_number.data == '12345678901' and form.pin.data == '9876':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check account number and pin', 'danger')
    return render_template('login.html', title = 'Login', form = form)   

if __name__ == "__main__":
    app.run(debug = True)