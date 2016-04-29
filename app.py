import falcon
import json
import redis

from rethink_client import *
from postgres_client import *
from utils import *

class NoteResource:

    def on_get(self, req, resp):
        if req.get_param("id"):
            result = {'note': rethinkdb.db(PROJECT_DB).table(PROJECT_TABLE).get(req.get_param("id")).run(db_connection)}
        else:
            note_cursor = rethinkdb.db(PROJECT_DB).table(PROJECT_TABLE).run(db_connection)
            result = {'notes': [i for i in note_cursor]}
        resp.body = json.dumps(result)

    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e.message)

        try:
            result = json.loads(raw_json, encoding='utf-8')
            sid = rethinkdb.db(PROJECT_DB).table(PROJECT_TABLE).insert({'title':result['title'], 'body': result['body']}).run(db_connection)
            resp.body = 'Succesffuly inserted %s' % (sid)
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON', 'Could not decode the request body.')

class DefaultResource:

    def on_get(self, req, resp):
        resp.body = json.dumps({'hello': 'world'})

class EventResource:

    conn = psycopg2.connect("dbname=eventdb user=charlie")
    pgdb = conn.cursor()

    def on_get(self, req, resp):
        id = req.get_param('id')
        if id:
            try:
                pgdb.execute("SELECT * FROM test WHERE id = %s;", (id))
                if True:
                    for record in pgdb:
                        print record
                else:
                    print "not found"
            except Exception as e:
                print "D'oh:"
                print e.message
        else:
            try:
                pgdb.execute("SELECT * FROM test;")
                result = Objectify(pgdb)
                resp.body = json.dumps(result[0] if result else None)
                pgdb.connection.close()
            except Exception as e:
                conn.rollback()
                print "Derp:"
                print e.message
                resp.body = json.dumps({'Thanks!': 'For attempting to get some test enties!'})

            # result2 = pgdb.fetchone()(1, 100, "abc'def")

api = falcon.API()
api.add_route('/notes', NoteResource())
api.add_route('/events', EventResource())
api.add_route('/', DefaultResource())
