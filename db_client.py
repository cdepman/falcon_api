import os
import rethinkdb as rdb
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

RDB_HOST = 'localhost'
RDB_PORT = 28015

PROJECT_DB = 'todo'
PROJECT_TABLE = 'notes'

db_connection = rdb.connect(RDB_HOST, RDB_PORT)

def dbSetup():
    try:
        rdb.db_create(PROJECT_DB).run(db_connection)
        print 'Database setup completed.'
    except RqlRuntimeError:
        try:
            rdb.db(PROJECT_DB).table_create(PROJECT_TABLE).run(db_connection)
            print 'Table creation completed.'
        except:
            print 'Table already exists.'

dbSetup()
