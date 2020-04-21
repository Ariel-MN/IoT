from pymongo import MongoClient; from ast import literal_eval; from sys import argv


try:
    arg = literal_eval(argv[1])
except SyntaxError:
    pass


def write_in_database(Number, IP, Battery, Measure):
    u = "SensorsWrite"; p = "E8EsF6HSBY5QR9qH"  # Permission: Write

    try:
        client = MongoClient(f'mongodb+srv://{u}:{p}@sensors-data-sobsn.mongodb.net/test?retryWrites=true&w=majority')
        db = client["DataBase"]; del u, p, client
        database = db.get_collection('Sensors-Data')
    except:
        return
    # Create a new sensor if no one have the same number:
    if database.find_one({'Number': Number}) == None:
        db.get_collection('Sensors-Data').insert_one({'Number': Number, 'IP': IP, 'Battery': Battery, 'Measure': Measure})
        print(""""Service Order" created successfully.""")
    # Update the sensor who has the same number:
    else:
        database.update_one({'Number': Number}, {'$set': {'IP': IP, 'Battery': Battery, 'Measure': Measure}})
        print(""""Service Order" updated successfully.""")


if __name__ == "__main__":
    try:
        if 'Number' in arg and 'IP' in arg and 'Battery' in arg and 'Measure' in arg:
            Number = str(arg['Number']); IP = str(arg['IP']); Battery = str(arg['Battery']); Measure = str(arg['Measure'])
            write_in_database(Number, IP, Battery, Measure)
    except NameError:
        pass
