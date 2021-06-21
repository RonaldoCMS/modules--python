from person import Person 

class Employee(Person):
    def __init__(self, name, surname, job):
        super().__init__(name, surname)
        self.job = job
    
    def __str__(self):
        return super().__str__() + 'and my job is ' + self.job

if __name__ == '__main__':
    fabio = Employee("Fabio", "Danubbio", "Developer")
    print(fabio.__str__())
    
