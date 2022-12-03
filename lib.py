import os, re, datetime
import db
from user import User

# source https://medium.com/@hillarywando/how-to-create-a-basic-crud-api-using-python-flask-cd68ef5fd7e3

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def connect_and_add():
    if not os.path.isfile('database'):
        db.connect()

    # INSERT
    usr = User(db.getNewId(), "cesar@bikes.org", "Cesar Bikes", datetime.datetime.now())
    print('new user added: ', usr.serialize())
    db.insert(usr)
