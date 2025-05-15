import sqlite3


DB_NAME = "../DB/ex.sqlite3"

QRY_UPDATE = '''
    UPDATE Users
    SET age = ?
    WHERE id = ?
'''


age = 24
id = 2

try:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(QRY_UPDATE, (age, id))
    conn.commit()
    conn.close()
    print("All done")
    
except Exception as e:
    conn.rollback()
    conn.close()
    print(f"## E20 ## ERROR: { e }")



