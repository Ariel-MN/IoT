from sys import argv

try:
    arg = argv[1]; _id = str(arg).strip()
except SyntaxError:
    pass

try:
    # Control who login and assign the Permissions:
    if _id == "5ddb086812454f2c54964284": print("0")    # Permissions: Read and Write
    elif _id == '5ddb098412454f2c54964287': print("1")  # Permissions: Read
    elif _id == '5ddc597512454f2c5496428a': print("2")  # Permissions: Maintenance
except NameError:
    pass
