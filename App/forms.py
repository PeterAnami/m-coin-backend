from flask_wtf import FlaskForm
from werkzeug.wrappers import request
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, Length, EqualTo, ValidationError


class SigninForm(FlaskForm):
    username = StringField(label='username', validators=[
                           InputRequired(), Length(min=4, max=64)])

    password = PasswordField(label='password', validators=[
                             InputRequired(), Length(min=4, max=24)])

    submit = SubmitField(label='SignIn')


class SignupForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])

    username = StringField(label='username', validators=[
                           DataRequired(), Length(min=4, max=64)])

    password = PasswordField(label='password', validators=[
                             DataRequired(), Length(min=4, max=24)])

    confirm_password = PasswordField(label='confirm password', validators=[
                                     DataRequired(), EqualTo(password)])

    submit = SubmitField(label='SignUp')


class PassResetForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    submit = SubmitField(label='Reset')
