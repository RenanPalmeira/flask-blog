# -*- coding: utf8 -*-

import datetime
from core.db import db

class Blog(db.Model):
	id_blog = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(80))
	email = db.Column(db.String(255), default = 'blog@flaskblog.com', unique = True) 
	password = db.Column(db.String(255))
	description = db.Column(db.String(255), default = None, nullable = True) 
	logo = db.Column(db.String(255), default = None, nullable = True)
	website = db.Column(db.String(255))
	about = db.Column(db.String(255))
	author = db.Column(db.String(80))
	create_date = db.Column(db.DateTime, default=datetime.datetime.now())
	update_date = db.Column(db.DateTime, default=datetime.datetime.now())
	
	genre = db.Column(db.String(255))

	status = db.Column(db.Boolean, default=True)	

	_tablename_='blog'