def objectify(cursor):
    return [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
Objectify = objectify
