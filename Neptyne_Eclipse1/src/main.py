from crud.DbConnection import DbConnection


if __name__ == "__main__":
    
    QUERY = 'SELECT * FROM Users'
    
    DbConnection._DB_NAME = '/home/student/DEV/eclipse-workspace/Neptyne_Eclipse/BD/exp.sqlite3'
    
    dbc = DbConnection()
    cur = dbc.cursor()
    cur.execute(QUERY)
    rows = cur.fetchall()
    
    for row in rows:
        print(row)