#!/usr/bin/python
# -*- coding: utf8 -*-
import server
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = server.app
db = server.db
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
