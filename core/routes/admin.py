# -*- coding: utf8 -*-

import datetime
import markdown
from flask import Blueprint, request, render_template, redirect, \
				  url_for, session, render_template_string, Markup
from core.db import db
from core.models import Contrib, Blog, Post, Tag

app = Blueprint('admin', __name__, url_prefix='/admin')

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

@app.route("/")
def default():
	response=session_info_blog()
	post=Post.query.filter_by(blog_id=response['id_blog'],status=1).all()
	return render_template("admin/login.html",blog=response,posts=post)

@app.route("/sobre/")
def sobre():
	content = """
	Chapter
	=======

	Section
	-------

	* Item 1
	* Item 2
	"""
  	content = Markup(markdown.markdown(content))
  	return render_template("about.html", **locals())
	#response=session_info_blog()
	#post=Post.query.filter_by(blog_id=response['id_blog'],status=1).all()
	#return render_template("index.html",blog=response,posts=post)

@app.errorhandler(404)
def page_not_found(e):
	response={
		'title':'vaiiiii',
		'author':'geroudo',
		'content':'iejfiejfpwenoinviow iv weiv eiov peio viowqn fionwefoq we',
		'post_class':'post',
		'url':'renan',
	}
	return render_template("post.html",post=response,blog={'title':'fdsfd'})	