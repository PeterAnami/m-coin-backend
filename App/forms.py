from flask_wtf import FlaskForm
from werkzeug.wrappers import request
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError


class SigninForm(FlaskForm):
    username = StringField(label='username', validators=[
                           InputRequired(), Length(min=4, max=64)])

    password = PasswordField(label='password', validators=[
                             InputRequired(), Length(min=4, max=24)])

    submit = SubmitField(label='SignIn')


class SignupForm(FlaskForm):
    email = StringField(label='email', validators=[
                        InputRequired(), Email(), Length(min=6, max=24)])

    username = StringField(label='username', validators=[
                           InputRequired(), Length(min=4, max=64)])

    password = PasswordField(label='password', validators=[
                             InputRequired(), Length(min=4, max=24)])

    confirm_password = PasswordField(label='confirm password', validators=[
                                     InputRequired(), EqualTo(password)])

    submit = SubmitField(label='SignUp')


class PassResetForm(FlaskForm):
    email = StringField(label='email', validators=[InputRequired(), Email()])
    submit = SubmitField(label='Reset')
