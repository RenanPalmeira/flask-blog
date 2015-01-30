# -*- coding: utf8 -*-

import datetime
from core.db import db

class Tag(db.Model):
	id_tag = db.Column(db.Integer, primary_key = True)
	
	name = db.Column(db.String(80))
	
	#blog_id = db.Column(db.Integer, db.ForeignKey('blog.id_blog'))
	post_set = db.relationship('Post',backref='tag',lazy='dynamic')
	
	create_date = db.Column(db.DateTime, default=datetime.date.today())
	update_date = db.Column(db.DateTime, default=datetime.date.today())

	status = db.Column(db.Boolean, default=True)	

	_tablename_='tag'