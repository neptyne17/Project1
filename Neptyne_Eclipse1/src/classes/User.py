class User:
    
    def __init__(self, id_, name, age):
        self._id = id_
        self._name = name
        self._age = age
        
        
    @property
    def id (self):
        return self._id
    
    @property
    def name (self):
        return self._name
    
    @property
    def age (self):
        return self._age
    
    @id.setter
    def id (self, a):
        self._id = a
    
    @name.setter
    def name (self, a):
        self._name = a
    
    @age.setter
    def age (self, a):
        self._age = a

    
    
    
    def __str__(self):
        return  f'class User [\n' +\
                f'    id:    { self._id}\n' +\
                f'    name:    { self._name}\n' +\
                f'    age:    { self._age}\n' +\
                f']\n'
  
  
if __name__ == '__main__':                
    u = User(10, 'Vasia', 20)
    print(u)
    u.name = 'Vera'
    print(u)
