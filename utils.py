def cursor_to_arr(cursor, already_fetched):
    arr = []
    if already_fetched:
        for row in cursor:
            obj = {}
            for i, value in enumerate(row):
                obj[cursor.description[i][0]] = value
            arr.append(obj)
    else:
        for row in cursor.fetchall():
            obj = {}
            for i, value in enumerate(row):
                obj[cursor.description[i][0]] = value
            arr.append(obj)
    return arr
