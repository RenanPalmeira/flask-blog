# -*- coding: utf8 -*-

import datetime
from core.db import db

class Post(db.Model):
	id_post = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(80))
	content = db.Column(db.String(255)) 
	logo = db.Column(db.String(255), default = None, nullable = True)

	create_date = db.Column(db.DateTime, default=datetime.date.today())
	update_date = db.Column(db.DateTime, default=datetime.date.today())

	tag_id = db.Column(db.Integer, db.ForeignKey('tag.id_tag'))
	blog_id = db.Column(db.Integer, db.ForeignKey('blog.id_blog'))
	
	status = db.Column(db.Boolean, default=True)	

	_tablename_='post'