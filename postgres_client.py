import os
import psycopg2

conn = psycopg2.connect("dbname=eventdb user=charlie")
pgdb = conn.cursor()

def dbSetup():
    try:
        pgdb.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
        pgdb.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
        try:
            conn.commit()
            conn.close()
            print 'Successfully wrote to db.'
        except Exception as e:
            print "Couldn't commit:"
            print e.message
    except Exception as e:
        print 'Shit:'
        print e.message

dbSetup()


# Open a cursor to perform database operations

# Execute a command: this creates a new table

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)

# Query the database and obtain data as Python objects
# result1 = pgdb.execute("SELECT * FROM test;")
# result2 = pgdb.fetchone()(1, 100, "abc'def")

# Make the changes to the database persistent
# conn.commit()

# Close communication with the database
# pgdb.close()
# conn.close()
