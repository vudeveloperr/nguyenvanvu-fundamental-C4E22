import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds249123.mlab.com:49123/c4e22-pool

host = "ds249123.mlab.com"
port = 49123
db_name = "c4e22-pool"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())