class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    @property
    def name(self):
        return self.__name
    
    @name.setter 
    def name(self, val):
        if val == "paolo":
            self.__name = val

p = Person("Fabio", "Danubbio")
print(p.name)
p.name = "Giacomo"
print(p.name)