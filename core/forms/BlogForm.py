# -*- coding: utf8 -*-

from wtforms import Form, BooleanField, TextField, PasswordField, validators

class BlogForm(Form):
    title = TextField('Title', [validators.Length(min=4, max=25)])
    author = TextField('Author', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.Required(),
    ])