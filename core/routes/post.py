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
from admin import app

@app.route("/<int:id_post>")
def profile_post(id_post):
	blog = Routes.session_blog()
	post = Post.query.filter_by(id_post=id_post, blog_id=blog['id_blog'], status=1)
	if post.count()==1:
		post=post.first()
		post.content = Markup(markdown.markdown(post.content))
		return render_template("admin/profile_post.html", **locals())
	return redirect(url_for('admin.default'))

@app.route("/edit/<int:id_post>")
def edit_post(id_post):
	blog = Routes.session_blog()
	post = Post.query.filter_by(id_post=id_post, blog_id=blog['id_blog'], status=1)
	if post.count()==1:
		post=post.first()
		return render_template("admin/edit_post.html", **locals())
	return redirect(url_for('admin.default'))


@app.route("/new/")
def new_post():
	response = Routes.session_blog()
	return render_template("admin/new_post.html", blog=response)

@app.route("/save/", methods=['POST'])
def save_post():
	form=PostForm(request.form)
	if request.method=='POST' and form.validate():
		blog = Routes.response_sql()
		title = form.title.data
		content = form.content.data
		p=Post(
			title = title,
			content = content, 
			blog_id = blog.id_blog,
			create_date = datetime.datetime.now(),
			update_date = datetime.datetime.now(),
			status = 1,
		)
		
		db.session.add(p)
		db.session.commit()	
	return redirect(url_for('admin.default'))

@app.route("/edit_save/<int:id_post>", methods=['POST'])
def edit_save_post(id_post):
	form=PostForm(request.form)
	if request.method=='POST' and form.validate():
		blog = Routes.response_sql()
		title = form.title.data
		content = form.content.data
		p=Post.query.filter_by(id_post=id_post, status=1)
		if p.count()==1:
			p.update(dict(title=title, content=content))
			db.session.commit()	
	return redirect(url_for('admin.default'))