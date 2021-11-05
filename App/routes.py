from . import app, db
from flask import redirect, request, render_template, flash
from .forms import SigninForm, SignupForm, PassResetForm, TransactionForm
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
            confirm_password = request.form['confirm_password']

            form = SignupForm(request.form)

            print(f'Validation passed? {form.validate()}')
            return redirect('/')

        except:
            form = SigninForm(request.form)

            if not form.validate():
                # danger is a bootstrap class
                flash('Incorrect login details!', 'danger')
                return redirect('/')

            username = form.username.data

            user = User.query.filter_by(username=username).first()

            if not user:
                flash('Username not found. Please try again...')
                return redirect('/')

            password = form.password.data

            if password != user.password:
                flash('Incorrect login credentials')
                return redirect('/')

            return redirect('/home')

    except:
        email = request.form['email']

        form = PassResetForm(request.form)
        if not form.validate():
            flash('Invalid email/Email not found!')
            return redirect('/')

    return redirect('/')


TEMP_ADDR = '3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5'


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        form = TransactionForm()

        return render_template('home.html', wallet_addr=TEMP_ADDR, form=form)

    form = TransactionForm(request.form)

    if form.validate():
        print('Form validated successfully...')

    return render_template('home.html', wallet_addr=TEMP_ADDR, form=form)


@app.route('/signout')
def signout():
    return redirect('/')
