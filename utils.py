def cursor_to_arr(cursor):
    arr = []
    for row in cursor.fetchall():
        obj = {}
        for i, value in enumerate(row):
            obj[cursor.description[i][0]] = value
        arr.append(obj)
    return arr
