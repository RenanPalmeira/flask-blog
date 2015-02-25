# -*- coding: utf8 -*-

import datetime
import markdown
from hashlib import md5
from flask import Blueprint, request, render_template, redirect, \
				  url_for, session, render_template_string, Markup, flash
from core.db import db
from core.models import Author, Blog, Post, Tag
from core.forms import BlogForm, AuthorForm, PostForm
from routes import Routes

app = Blueprint('admin', __name__, url_prefix='/admin')

@app.route("/")
def default():
	for t in Tag.query.all():
		print t.name

	response = Routes.session_blog()
	post = Post.query.filter_by(blog_id=response['id_blog'], status=1).order_by(Post.id_post.desc()).all()
	if response['genre'] == 'tutorial':
		return render_template("admin/new_login_form.html", blog=response)
	elif 'author' in session:
		return render_template("admin/panel.html", blog=response, posts=post)
	return render_template("admin/login.html", blog=response)

@app.route("/new_login/", methods=['POST'])
def new_login():
	form=BlogForm(request.form)
	if request.method=='POST' and form.validate():
		blog = Routes.response_sql()
		title = form.title.data
		author = form.author.data
		email = form.email.data
		password = md5(form.password.data).hexdigest()
		
		blog.title = title
		blog.author = author
		blog.email = email
		blog.password = password
		blog.update_date = datetime.datetime.now()
		blog.genre = 'first blog'

		a=Author(author,email,password)
		db.session.add(a)

		db.session.commit()
		
        return redirect(url_for('admin.default'))

	response = Routes.session_blog()
	return render_template("admin/login.html", blog=response)

@app.route("/login/", methods=['POST'])
def login():
	response = Routes.session_blog()
	
	form=AuthorForm(request.form)
	if request.method=='POST' and form.validate():
		blog = Routes.response_sql()
		email = form.email.data
		password = md5(form.password.data).hexdigest()

		a=Author.query.filter_by(email=email,password=password)
		
		if a.count()==1:		
			a=a.first()
			
			session_response={
				"id_blog":response['id_blog'],
				"author":a.name,
				"title":response['title'],
				"email":a.email
			}
			session['author']=session_response
		elif a.count()<=0:
			flash("User not found")
		else:
			flash("42")
        return redirect(url_for('admin.default'))
	return render_template("admin/login.html", blog=response)