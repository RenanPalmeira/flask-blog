# -*- coding: utf8 -*-

import datetime
from core.db import db

class User(db.Model):
	id_user = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), unique = True)
	name = db.Column(db.String(80))
	password = db.Column(db.String(255))
	website = db.Column(db.String(255))
	profile = db.Column(db.String(255), default = None, nullable = True)
	
	create_date = db.Column(db.DateTime, default=datetime.date.today())
	update_date = db.Column(db.DateTime, default=datetime.date.today())

	status = db.Column(db.Boolean, default=True)	

	_tablename_='user'