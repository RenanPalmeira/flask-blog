#!/usr/bin/python
# -*- coding: utf8 -*-
import server
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
"""from alembic.ddl.sqlite import SQLiteImpl

SQLiteImpl.add_constraint = lambda *args, **kwargs: None
SQLiteImpl.drop_constraint = lambda *args, **kwargs: None
"""
app = server.app
db = server.db
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
