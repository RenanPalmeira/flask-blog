# -*- coding: utf8 -*-

from wtforms import Form, BooleanField, TextField, PasswordField, validators

class BlogForm(Form):
    title = TextField('Title', [validators.Length(min=4, max=25)])
    content = TextField('Content', [validators.Length(min=4, max=None)])