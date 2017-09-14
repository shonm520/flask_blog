# -*- coding: utf-8 -*-

import flask
import flask_bootstrap 
import flask_moment
import datetime
#from flask_wtf import FlaskForm
#from flask_wtf import FlaskForm
#import flask_wtf

import flask_wtf as fw
import wtforms
from wtforms.validators import Required


app = flask.Flask(__name__)
#app.config.from_object("config")
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = flask_bootstrap.Bootstrap(app)
moment = flask_moment.Moment(app)

@app.route('/')
def index():
    return flask.render_template("welcome.html", title="Welcome")
    
@app.route('/home')
def home():
    return flask.render_template('base.html', title='Home'), 404
    #return flask.redirect('https://www.baidu.com')
    #return flask.abort(404)
    
@app.route('/user/<name>')
def user(name):
    return flask.render_template("user.html", name=name)

    
@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 500
    
    
    
class NameForm(fw.FlaskForm):
    name = wtforms.StringField("What is your name?", validators=[Required()])
    submit = wtforms.SubmitField('Submit')
    
@app.route('/zhu', methods = ['GET', 'POST'])
def index2():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = flask.session.get('name')
        name = form.name.data
        if old_name is not None and old_name != name:
            flask.flash('Looks like you have changed your name!')
        form.name.data = ''
        flask.session['name'] = name
        return flask.redirect(flask.url_for('index2'))
    return flask.render_template('index.html', form = form, name = flask.session['name'])
    