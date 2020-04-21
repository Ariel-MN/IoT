from pymongo import MongoClient; from sys import argv; from ast import literal_eval

try:
    arg = literal_eval(argv[1])
except SyntaxError:
    pass


def write_in_database(Number, Date, Employee, Dustbins):
    u = "ServiceWriter"; p = "gA9ofgNMht3K2ugI"  # Permission: Write

    try:
        client = MongoClient(f'mongodb+srv://{u}:{p}@service-order-icvp2.mongodb.net/test?retryWrites=true&w=majority')
        db = client["DataBase"]; del u, p, client
        database = db.get_collection('Service-Order')
    except:
        return
    # Create a new service order if no one have the same number:
    if database.find_one({'Number': Number}) == None:
        db.get_collection('Service-Order').insert_one({'Number': Number, 'Date': Date, 'Employee': Employee, 'Dustbins': Dustbins})
        print(""""Service Order" created successfully.""")
    # Update the service order who has the same number:
    else:
        database.update_one({'Number': Number}, {'$set': {'Date': Date, 'Employee': Employee, 'Dustbins': Dustbins}})
        print('''"Service Order" updated successfully.''')


if __name__ == "__main__":
    try:
        if 'Number' in arg and 'Date' in arg and 'Employee' in arg and 'Dustbins' in arg:
            Number = str(arg['Number']); Date = str(arg['Date']); Employee = str(arg['Employee']); Dustbins = str(arg['Dustbins'])
            write_in_database(Number, Date, Employee, Dustbins)
    except NameError:
        pass
