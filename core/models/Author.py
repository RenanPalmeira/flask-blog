# -*- coding: utf8 -*-

import datetime
from hashlib import md5
from core.db import db

class Author(db.Model):
	id_author = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), unique = True)
	name = db.Column(db.String(80))
	password = db.Column(db.String(255))
	website = db.Column(db.String(255), nullable=True)
	profile = db.Column(db.String(255), default = None, nullable = True)
	
	create_date = db.Column(db.DateTime, default=datetime.date.today())
	update_date = db.Column(db.DateTime, default=datetime.date.today())

	status = db.Column(db.Boolean, default=True)	

	_tablename_='author'

	def __init__(self, name=None, email=None, password=None):
		self.name = name
		self.email = email
		self.password = password
		self.create_date = datetime.datetime.now()
		self.update_date = datetime.datetime.now()