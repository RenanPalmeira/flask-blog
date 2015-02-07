# -*- coding: utf8 -*-

from wtforms import Form, BooleanField, TextField, PasswordField, validators

class AuthorForm(Form):
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.Required(),
    ])