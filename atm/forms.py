from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError
from flask_login import current_user

class LoginForm(FlaskForm):
    account_number = StringField('Account Number (11-digit)', validators=[DataRequired(), Length(min = 11, max = 11), Regexp(regex=r'^\d{11}$')])
    pin = PasswordField('Pin (4-digit)', validators=[DataRequired(), Length(min = 4, max = 4), Regexp(regex=r'^\d{4}$')])
    submit = SubmitField('Log In')

class WithdrawForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Withdraw')
    def validate_amount(self, amount):
        if amount.data > current_user.account_balance:
            raise ValidationError('Amount is greater than your account balance')