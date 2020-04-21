from hashlib import sha512; import Login.loginDB as login


def convert_hash(user, password):
    user_hash = sha512(user.encode()).hexdigest(); pwd_hash = sha512(password.encode()).hexdigest()
    del user, password; login.read_from_database(user_hash, pwd_hash)
    del user_hash, pwd_hash; return
