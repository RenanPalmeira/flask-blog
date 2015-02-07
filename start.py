# -*- coding: utf8 -*-
import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from server import app
from core.models import Blog

db = SQLAlchemy(app)

b=Blog(
	author = 'flask-blog',
	title = 'Flask-Blog',
	description = 'your blog in Python Flask' ,
	logo = None,
	website = 'http://localhost:4242/',
	about = None,
	email = 'renan@flaskblog.com', 
	password = 'c4d8af46f455557f60e91fb716affa9f',
	create_date = datetime.datetime.now(),
	update_date = datetime.datetime.now(),
	genre = 'tutorial',
	status = 1,
)

if __name__=='__main__':
	try:
		db.session.add(b)
		db.session.commit()
	except:
		print "Run this file.py only once"
    	
