# -*- coding: utf8 -*-

import datetime
from flask import Blueprint, request, render_template, redirect, url_for, session

app = Blueprint('default', __name__, url_prefix='')

@app.route("/")
def index():
	posts=[{
		'title':'vaiiiii',
		'author':'geroudo',
		'content':'iejfiejfpwenoinviow iv weiv eiov peio viowqn fionwefoq we',
		'post_class':'post',
		'url':'renan'
	},{
		'title':'vaiiiii',
		'author':'geroudo',
		'content':'iejfiejfpwenoinviow iv weiv eiov peio viowqn fionwefoq we',
		'post_class':'post',
		'url':'renan',
	},{
		'title':'vaiiiii',
		'author':'geroudo',
		'content':'iejfiejfpwenoinviow iv weiv eiov peio viowqn fionwefoq we',
		'post_class':'post',
		'url':'renan'
	}]
	response={
		'title':'Dia de Programador',
		'description':'Pensamentos , histórias e ideias sobre programação.'.decode('utf8'),
		'logo':None,
		'posts':posts,
		'meta':{
			'title':'Dia de Programador'
		},
		'author':{
			'image':None,
		}
	}
	return render_template("index.html",blog=response)

@app.route("/admin/")
def admin():
	posts=[{
		'title':'vaiiiii',
		'author':'geroudo',
		'content':'iejfiejfpwenoinviow iv weiv eiov peio viowqn fionwefoq we',
		'post_class':'post',
		'url':'renan'
	},{
		'title':'vaiiiii',
		'author':'geroudo',
		'content':'iejfiejfpwenoinviow iv weiv eiov peio viowqn fionwefoq we',
		'post_class':'post',
		'url':'renan',
	},{
		'title':'vaiiiii',
		'author':'geroudo',
		'content':'iejfiejfpwenoinviow iv weiv eiov peio viowqn fionwefoq we',
		'post_class':'post',
		'url':'renan'
	}]
	response={
		'title':'Dia de Programador',
		'description':'Pensamentos , histórias e ideias sobre programação.'.decode('utf8'),
		'logo':None,
		'posts':posts,
		'meta':{
			'title':'Dia de Programador'
		},
		'author':{
			'image':None,
		}
	}
	return render_template("admin.html",blog=response)


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
