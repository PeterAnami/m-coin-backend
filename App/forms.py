from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.core import FloatField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Email, Length, EqualTo, ValidationError


class SigninForm(FlaskForm):
    username = StringField(label='username', validators=[
                           InputRequired(), Length(min=4, max=64)])

    password = PasswordField(label='password', validators=[
                             InputRequired(), Length(min=4, max=24)])

    submit = SubmitField(label='SignIn')


class SignupForm(FlaskForm):
    email = StringField(label='email', validators=[
                        InputRequired(), Email(), Length(min=4, max=64)])

    username = StringField(label='username', validators=[
                           InputRequired(), Length(min=4, max=64)])

    password = PasswordField(label='password', validators=[
                             InputRequired(), Length(min=4, max=24)])

    confirm_password = PasswordField(label='confirm password', validators=[
                                     InputRequired(), EqualTo(password, message='Passwords do not match!')])

    submit = SubmitField(label='SignUp')


class PassResetForm(FlaskForm):
    email = StringField(label='email', validators=[InputRequired(), Email()])
    submit = SubmitField(label='Reset')


class TransactionForm(FlaskForm):
    amount_btc = FloatField(label='Bitcoin amount',
                            validators=[InputRequired()])

    amount_ksh = FloatField(label='Equivalent ksh')
    phone_number = IntegerField(
        label='MPesa number', validators=[DataRequired()])

    wallet_addr = StringField(label='Wallet Address')

    submit = SubmitField(label='Proceed')
