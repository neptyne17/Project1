from crud.USER_CRUD import USER_CRUD




if __name__ == '__main__':
    
    u_crud = USER_CRUD()
    rows = u_crud.select_all_obj()
    
    for row in rows:
        print (row[1])
