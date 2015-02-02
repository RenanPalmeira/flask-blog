# -*- coding: utf8 -*-

import datetime
import markdown
from flask import Blueprint, request, render_template, redirect, \
				  url_for, session, render_template_string, Markup
from core.db import db
from core.models import Contrib, Blog, Post, Tag
from routes import Routes

app = Blueprint('admin', __name__, url_prefix='/admin')

@app.route("/")
def default():
	response=Routes.session_blog()
	post=Post.query.filter_by(blog_id=response['id_blog'],status=1).all()
	return render_template("admin/login.html",blog=response,posts=post)