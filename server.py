# -*- coding: utf8 -*-

from flask import Flask, render_template
from wtforms.meta import DefaultMeta
from core.db import db, MongoDB_Connection, MongoDB_Models
from core.routes import Routes
from core.filters import Filters

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/dev.db'
# if you  use mongoDB, remove '#' the 2 lines in bottom

#app.config['MONGODB_HOST'] = 'localhost'
#app.config['MONGODB_PORT'] = 27017

# if you need a mongoDB url, just set app.config['MONGODB_URL']

DefaultMeta.locales = ('pt_BR', 'pt')

db.init_app(app)
connection=MongoDB_Connection(app)
m=MongoDB_Models()
f=Filters(app)
r=Routes(app)

if __name__ == "__main__":
	app.debug = True
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	app.run(host='localhost', port=4242)