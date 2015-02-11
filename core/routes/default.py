# -*- coding: utf8 -*-

import datetime
import markdown
from flask import Blueprint, request, render_template, redirect, \
				  url_for, session, render_template_string, Markup
from core.db import db, connection
from core.models import Author, Blog, Post, Tag
from routes import Routes
app = Blueprint('default', __name__, url_prefix='')

@app.route("/")
def default():
	response=Routes.session_blog()
	post=Post.query.filter_by(blog_id=response['id_blog'],status=1).all()
	return render_template("index.html",blog=response,posts=post)

@app.route("/<int:id_post>")
def read_profile(id_post):
	blog = Routes.session_blog()
	post = Post.query.filter_by(id_post=id_post, blog_id=blog['id_blog'], status=1)
	if post.count()==1:
		post=post.first()
		post.content = Markup(markdown.markdown(post.content))
		return render_template("post.html", **locals())
	return redirect(url_for('default.default'))

@app.errorhandler(404)
def page_not_found(e):
	return render_template_string("Not Found")	