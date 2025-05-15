from classes.User import User

def row_to_user(row):
    u = User(row[0], row[1], row[2])
    return u