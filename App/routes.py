from . import app
from flask import url_for, redirect, request, render_template
from .forms import SigninForm, SignupForm, PassResetForm
from flask_bcrypt import generate_password_hash, check_password_hash


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

        except:
            form = SigninForm(request.form)

            if form.validate():
                username = form.username.data
                hashed_password = str()

            else:
                print('Validation failed.')

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
