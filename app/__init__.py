from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
# the toolbar is only enabled in debug mode:
app.debug = True
toolbar = DebugToolbarExtension(app)

from app import routes

