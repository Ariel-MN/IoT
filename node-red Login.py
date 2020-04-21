from ast import literal_eval; from os import path as os_path; from sys import path as sys_path; from sys import argv, version

# Control the current Python version in use:
v = float(''.join(list(version[:3])))
if v < 3.8:
    raise Exception("Must use Python 3.8 or higher. Instead, currently using: Python " + str(v))

# Add the directory of the program to the sys path:
current_dir = os_path.dirname(os_path.abspath(__file__))
sys_path.append(current_dir)

import Login.pwdhash as start

try:
    arg = literal_eval(argv[1])
except SyntaxError:
    pass

try:
    start.convert_hash(arg['username'], arg['password'])
except NameError:
    pass
