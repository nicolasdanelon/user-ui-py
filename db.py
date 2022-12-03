import sqlite3, random, datetime
from user import User

def getNewId():
    return random.getrandbits(28)

def connect():
    conn = sqlite3.connect('database')
    cur = conn.cursor()
    cur.execute("CREATE TABLE users(id INT PRIMARY KEY NOT NULL, name TEXT NOT NULL, email TEXT NOT NULL, created_at datetime default current_created_at)")
    conn.commit()
    conn.close()
    # for i in users:
    #     usr = User(getNewId(), i['name'], i['email'], i['created_at'])
    #     insert(usr)

def insert(user):
    conn = sqlite3.connect('database')
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?,?)", (
        user.id,
        user.available,
        user.title,
        user.timestamp
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('database')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    users = []
    for i in rows:
        user = User(i[0], i[1], i[2], i[3])
        users.append(user)
    conn.close()
    return users

def update(user):
    conn = sqlite3.connect('database')
    cur = conn.cursor()
    cur.execute("UPDATE users SET name=?, email=? WHERE id=?", (user.name, user.eamail, user.id))
    conn.commit()
    conn.close()

def delete(theId):
    conn = sqlite3.connect('database')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=?", (theId,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('database')
    cur = conn.cursor()
    cur.execute("DELETE FROM users")
    conn.commit()
    conn.close()
