# -*- coding: utf8 -*-
import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from server import app
from core.models import Blog

db = SQLAlchemy(app)

b=Blog(
	author= 'flask-blog',
	title = 'Flask-Blog',
	description = 'your blog in Python Flask' ,
	logo = None,
	website = 'http://0.0.0.0:4242/',
	about = None,
	create_date = datetime.datetime.now(),
	update_date = datetime.datetime.now(),
	status = 1,
)

if __name__=='__main__':
	db.session.add(b)
	db.session.commit()