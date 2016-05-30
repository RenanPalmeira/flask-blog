# -*- coding: utf8 -*-

from flask import Flask, render_template
from wtforms.meta import DefaultMeta
from core.db import db
from core.routes import Routes
from core.filters import Filters

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/dev.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

DefaultMeta.locales = ('pt_BR', 'pt')

db.init_app(app)
f=Filters(app)
r=Routes(app)

if __name__ == "__main__":
	app.debug = True
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	app.run(host='localhost', port=4242)
