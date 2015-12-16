from flask import Flask, render_template, session, redirect, url_for, flash
from app import app
from .forms import LoginForm

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'name': 'Carlos'}
    return render_template('index.html', title='My Profile', user=user)

@app.route('/data', methods=['GET', 'POST'])
def data():
    return render_template('data.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Log In', form=form,
                            providers=app.config['OPENID_PROVIDERS'])

@app.route('/user')
def user():
    return render_template('user.html')