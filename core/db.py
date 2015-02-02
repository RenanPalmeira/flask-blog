# -*- coding: utf8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from mongokit import Connection, MongoClient	

def MongoDB_Connection(app):
	global connection
	if not 'config' in dir(app):
		connection=False
	if 'MONGODB_URL' in app.config:
		connection=MongoClient(app.config['MONGODB_URL'])
	elif 'MONGODB_HOST' and 'MONGODB_PORT' in app.config:
		connection=Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])
	else:
		connection=False
	return connection

db = SQLAlchemy()