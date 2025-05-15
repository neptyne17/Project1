import sqlite3

class DbConnection:
    
    _DB_NAME = '/home/student/DEV/eclipse-workspace/Neptyne_Eclipse/BD/ex.sqlite3'

    def __init__(self):
        try:
            self._connection = sqlite3.connect(self._DB_NAME)
        except Exception as e:
            print(f'## e2020 ## ERROR: { e }')
            self._connection = None
    
    def commit(self):
        self._connection.commit()
        
    def close(self):
        try:
            self._connection.close()
        except Exception as e:
            print (f"## e 2020 ## ERROR: { e }")
    @property
    def connection(self):
        return self._connection
    @property
    def cursor (self):
        return self._connection.cursor

if __name__ == '__main__':
    
    QUERY = "SELECT * FROM Users"
    
    dbc = DbConnection()
    cur = dbc.cursor()
    cur.execute(QUERY)
    rows = cur.fetchall()
    
    
    for row in rows:
        print(row)