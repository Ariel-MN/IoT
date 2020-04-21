from pymongo import MongoClient; import Login.login_id as log_id


def read_from_database(user_hash, pwd_hash):
    try:
        u = "LoginCheck"; p = "uqOs9h4DU6NnRoRy"  # User and Password 'Login' database cloud.
        client = MongoClient(f'mongodb+srv://{u}:{p}@login-omhv2.mongodb.net/test?retryWrites=true&w=majority')
        db = client["DataBase"]; del u, p, client
        database = db.get_collection('Login-Data')
    except: print("2"); return  # Error: Server Down!

    try:
        doc = database.find_one({'User': user_hash, 'Password': pwd_hash})
        if user_hash == doc['User'] and pwd_hash == doc['Password']:
            _id = str(doc['_id']); del doc, db; print("0")
            log_id.read_from_database(_id); return
        else: print("1"); return  # Error: Wrong User or Password!
    except: print("1"); return
