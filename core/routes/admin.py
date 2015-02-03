# -*- coding: utf8 -*-

import datetime
import markdown
from hashlib import md5
from flask import Blueprint, request, render_template, redirect, \
				  url_for, session, render_template_string, Markup
from core.db import db
from core.models import Contrib, Blog, Post, Tag
from core.forms import BlogForm
from routes import Routes

app = Blueprint('admin', __name__, url_prefix='/admin')

@app.route("/")
def default():
	response = Routes.session_blog()
	post = Post.query.filter_by(blog_id=response['id_blog'], status=1).all()
	return render_template("admin/login.html", blog=response, posts=post)

@app.route("/login/", methods=['POST'])
def login():
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

		db.session.commit()
		
        return redirect(url_for('admin.default'))

	response = Routes.session_blog()
	return render_template("admin/login.html", blog=response)