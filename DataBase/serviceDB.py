from pymongo import MongoClient; from json import dumps; from sys import argv; from ast import literal_eval; from datetime import datetime

try:
    arg = literal_eval(argv[1])
except SyntaxError:
    pass

today = date_time = datetime.now()


def read_from_database(numb="", emp=""):
    u = "ServiceRead"; p = "m4dFJGirIoYU5312"  # Permission: Read Only

    try:
        client = MongoClient(f'mongodb+srv://{u}:{p}@service-order-icvp2.mongodb.net/test?retryWrites=true&w=majority')
        db = client["DataBase"]; del u, p, client
        database = db.get_collection('Service-Order')
    except:
        return

    try:
        if numb != "":
            doc = database.find_one({'Number': numb})
            del doc['_id']; print(dumps(doc))
    except TypeError: print("1"); return

    if emp != "":
        temp = []
        date = []

        for doc in database.find():
            if doc['Employee'] == emp:
                # Control date and pick all the orders that have not expired.
                date_time_obj = datetime.strptime(doc['Date'], '%d/%m/%Y')
                if today.date() <= date_time_obj.date():
                    temp.append(date_time_obj)
            else: print("1"); return

        for date_temp in temp:
            # Control date and select the nearest order for the employee.
            date1 = date_temp
            if date != []:
                date2 = date[0]
                if date1.date() < date2.date():
                    date[0] = date1
            else:
                date.insert(0, date_temp)

        doc = database.find_one({'Date': date[0].strftime('%d/%m/%Y'), 'Employee': emp})
        del doc['_id']; print(dumps(doc))


if __name__ == "__main__":
    try:
        if 'Number' in arg:
            read_from_database(numb=str(arg['Number']))

        elif 'Employee' in arg:
            read_from_database(emp=str(arg['Employee']))
    except NameError:
        pass
