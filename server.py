# -*- coding: utf8 -*-

from flask import Flask, render_template
from core.db import db
from core.routes import default, post, admin
from core.filters import Filters

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/dev.db'
db.init_app(app)
Filters(app)

app.register_blueprint(default.app)
app.register_blueprint(post.app)
app.register_blueprint(admin.app)

if __name__ == "__main__":
	app.debug = True
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	app.run(host='0.0.0.0', port=4242)