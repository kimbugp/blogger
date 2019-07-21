from flask import flash, redirect
from flask.templating import render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Simon Peter'}
    posts = [
        {
            'author': {'username': 'Martin'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Amos'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/index')
    return render_template('login.html', title='Sign-in', form=form)
