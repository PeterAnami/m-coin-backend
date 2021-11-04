from . import app
from flask import url_for, redirect, request, render_template
from .forms import SigninForm, SignupForm, PassResetForm


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
            print('Creating account...')
            print((email, username, password, confirm_pass))
        except:
            print('Logging in...')
            print((username, password))

    except:
        email = request.form['email']
        print('Resetting password...')
        print(email)

    return redirect('/home')


TEMP_ADDR = '3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5'


@app.route('/home')
def home():
    return render_template('home.html', wallet_addr=TEMP_ADDR)


@app.route('/signout')
def signout():
    return redirect('/')
