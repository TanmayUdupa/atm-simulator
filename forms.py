from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class LoginForm(FlaskForm):
    account_number = StringField('Account Number (11-digit)', validators=[DataRequired(), Length(min = 11, max = 11), Regexp(regex=r'^\d{11}$')])
    pin = PasswordField('Pin (4-digit)', validators=[DataRequired(), Length(min = 4, max = 4), Regexp(regex=r'^\d{4}$')])
    submit = SubmitField('Log In')