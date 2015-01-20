# -*- coding: utf8 -*-

import datetime
from flask import Blueprint, request, render_template, redirect, url_for, session

app = Blueprint('post', __name__, url_prefix='/post')

@app.route("/")
def post():
    return render_template('post.html')