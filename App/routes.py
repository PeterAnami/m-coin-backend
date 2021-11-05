from . import app
from flask import url_for, redirect, request, render_template, flash
from .forms import SigninForm, SignupForm, PassResetForm
from flask_bcrypt import generate_password_hash, check_password_hash
from . import User, Transactions as Trans


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        signinform = SigninForm()
        signupform = SignupForm()
        passresetform = PassResetForm()

        return render_template('index.html', signin=signinform, signup=signupform, passreset=passresetform)

    try:
        username = request.form['username']
        password = request.form['password']

        try:
            confirm_pass = request.form['confirm_password']
            email = request.form['email']

            form = SignupForm(request.form)

            if not form.validate():
                return redirect('/')

            email = form.email.data
            username = form.username.data
            password = form.password.data

            new_user = User(id=123, email=email, username=username,
                            password=generate_password_hash(password))

            return redirect('/home')

        except:
            form = SigninForm(request.form)

            if form.validate():
                username = form.username.data
                user = User.query.filter_by(username).first()
                print(user)

            else:
                # danger is a bootstrap class
                flash('Incorrect login details!', 'danger')
                return redirect('/')

    except:
        email = request.form['email']

        form = PassResetForm(request.form)

    return redirect('/')


TEMP_ADDR = '3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5'


@app.route('/home')
def home():
    return render_template('home.html', wallet_addr=TEMP_ADDR)


@app.route('/signout')
def signout():
    return redirect('/')
