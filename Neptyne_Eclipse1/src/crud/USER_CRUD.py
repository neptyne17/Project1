from crud.DbConnection import DbConnection
from helpers.obj_helper import row_to_user


class USER_CRUD:
    
    def __init__(self):
        self._dbc = DbConnection()
        self._cursor = self._dbc.cursor()
                
    def select_all(self):
        QUERY = "SELECT * FROM Users"
        
        
        rows = None
        try:
            self._cursor.execute(QUERY)
            rows = self._cursor.fetchall()
            self._dbc.commit()
        except Exception as e:
            print (f'## e3030 ## ERROR: { e }')
            
            
        return rows
            
    def select_all_obj(self):
        rows = self.select_all()
        users = []
        for row in rows:
            users.append(row_to_user(row))
            
        return users        
        

if __name__ == '__main__':
    u_crud = USER_CRUD()
    rs = u_crud.select_all()
    
    for i in rs:
        print (row_to_user(i))        
                
                