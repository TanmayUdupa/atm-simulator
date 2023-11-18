from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def home():
    return render_template('home.html')

@app.route("/view_transactions")
def view_transactions():
    return render_template('view_transactions.html', transactions=transactions)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

