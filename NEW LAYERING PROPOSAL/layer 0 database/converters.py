#TODO Refer to https://docs.python.org/3/library/sqlite3.html#adapter-and-converter-recipes

def convert_date(val):
    """Convert ISO 8601 date to datetime.date object."""
    return datetime.date.fromisoformat(val.decode())

def convert_time(val):
    """Convert 24-hr time to datetime.time object."""
    iso_time_string = convert_to_iso(val) # TODO 2359 --> T23:59:00Z or sum like that
    return datetime.time.fromisoformat()

def convert_to_iso(val):
    raise NotImplementedError()

def convert_datetime(val):
    """Convert ISO 8601 datetime to datetime.datetime object."""
    return datetime.datetime.fromisoformat(val.decode())

def convert_file(val):
    return "FILE"

def convert_yaml(val):
    return "YAML FILE"

def convert_txt(val):
    return val