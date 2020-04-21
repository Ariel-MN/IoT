import DataBase.sensorsDB as db; from sys import argv; from ast import literal_eval

try:
    arg = literal_eval(argv[1])
except SyntaxError:
    pass

try:
    if 'IP' in arg:
        db.read_from_database(ip=str(arg['IP']))
    elif 'Number' in arg:
        db.read_from_database(numb=str(arg['Number']))
except NameError:
    pass
