from pymongo import MongoClient; from json import dumps


def read_from_database(numb="", ip=""):
    u = "SensorsRead"; p = "SnXfvEoPbA5q43m7"  # Permission: Read Only

    try:
        client = MongoClient(f'mongodb+srv://{u}:{p}@sensors-data-sobsn.mongodb.net/test?retryWrites=true&w=majority')
        db = client["DataBase"]; del u, p, client
        database = db.get_collection('Sensors-Data')
    except:
        return

    try:
        if numb != "":
            doc = database.find_one({'Number': numb})
            del doc['_id']; print(dumps(doc))

        elif ip != "":
            doc = database.find_one({'IP': ip})
            del doc['_id']; print(dumps(doc))
    except TypeError: print("1"); return
