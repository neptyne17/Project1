import sqlite3
from classes.User import User

DB_NAME = '../BD/ex.sqlite3'

QRY_SELECT = '''
    SELECT *
    FROM Users
    WHERE   id > 1 AND
            name LIKE ?
'''

name = '%'


try:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(QRY_SELECT, (name,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    
except Exception as e:
    conn.rollback()
    conn.close()
    print(f"## E20 ## ERROR: { e }")

for row in rows:
    u = User(row[0], row[1], row[2])
    print (f'Name: { u.name } \t (age: { u.age })')