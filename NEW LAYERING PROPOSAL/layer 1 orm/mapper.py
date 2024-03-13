
rows = Database.select(query)
objs = map(func,rows)

def func:
    for row in rows:
        keys = row.key()
        values = [val for val in row]
        Class[keys[0]] = values[0]
        
return objs

    """
        Identify what type of class I need
    """