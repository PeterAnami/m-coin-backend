from flask_wtf import FlaskForm
from werkzeug.wrappers import request
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class SigninForm(FlaskForm):
    formname = 'signin'

    username = StringField(label='username', validators=[
                           DataRequired(), Length(min=5, max=64)])

    password = PasswordField(label='password', validators=[
                             DataRequired(), Length(min=4, max=64)])

    submit = SubmitField(label='SignIn')


class SignupForm(FlaskForm):
    formname = 'signup'

    email = StringField(label='email', validators=[DataRequired(), Email()])

    username = StringField(label='username', validators=[
                           DataRequired(), Length(min=4, max=12)])

    password = PasswordField(label='password', validators=[
                             DataRequired(), Length(min=4, max=64)])

    confirm_password = PasswordField(label='confirm password', validators=[
                                     DataRequired(), EqualTo(password)])

    submit = SubmitField(label='SignUp')


class PassResetForm(FlaskForm):
    formname = 'passreset'

    email = StringField(label='email', validators=[DataRequired(), Email()])
    submit = SubmitField(label='Reset')
