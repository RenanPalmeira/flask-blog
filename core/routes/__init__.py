# -*- coding: utf8 -*-

import datetime
from flask import Blueprint, request, render_template, redirect, \
				  url_for, session, render_template_string, Markup
from core.db import db
from core.models import Contrib, Blog, Tag

def session_info_blog():
	response=Blog.query.filter_by(website=request.url_root,status=1).first()
	tabs=list()
	tags=Tag.query.filter_by(status=1).all()
	for tag in tags:
		if tag.post_set.count()>=1:
			tabs+=[tag.name]
	session_response={
		"id_blog":response.id_blog,
		"author":response.author,
		"title":response.title,
		"logo":response.logo,
		"website":response.website,
		"about":response.about,
		"tab":tabs,
		"url":request.url_root,
	}
	session['blog']=session_response
	return session['blog']

def check_session_blog():
	if 'blog' in session:
		return session['session']
	session_blog=session_info_blog()
	return session_blog