import sqlite3



DB_FOLDER='../BD/exp.sqlite3'



CREATE1 = """
    CREATE TABLE IF NOT EXISTS Users (
    
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
    )          
"""

try:
    conn = sqlite3.connect(DB_FOLDER)
    cur = conn.cursor()
    cur.execute(CREATE1)
    conn.commit()
    conn.close()
    
except Exception as e:
    conn.close()
    print(f'## E20 ## ERROR: { e }')


