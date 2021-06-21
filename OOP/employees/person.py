class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Hello ' + self.name + " " + self.surname

if __name__ == '__main__':
    fabio = Person("Fabio", "Danubbio")
    print(fabio.__str__())
        