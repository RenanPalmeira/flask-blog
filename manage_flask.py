#!/usr/bin/python
# -*- coding: utf8 -*-
import server
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

app = server.app
db = server.db
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
