import sqlite3

db_folder = "/home/student/DEV/eclipse-workspace/Neptyne_Eclipse/BD/exp.sqlite3"


insert1 = '''
        INSERT INTO Users (name,age)
        VALUES (?, ?)    
'''
Delete = '''
    DELETE FROM Users
'''

users = [
    ("Vasia", 20),
    ("Vera", 20),
    ("Kolia", 20),
    ("Olia", 20)
]

users2 = [
    ("Alex", 20),
    ("Fred", 20),
    ("Georg", 20),
    ("Tom", 20)
]

try:
    conn = sqlite3.connect(db_folder)
    cur = conn.cursor()
    cur.executemany(insert1, users2)
    conn.commit()
    conn.close()
    
except Exception as e:
    conn.rollback()
    conn.close()
    print(f"## E20 ## ERROR: { e }")