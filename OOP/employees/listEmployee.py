from employee import Employee

class ListEmployee:
    def __init__(self):
        self.list = []

    def addEmployee(self, item):
        self.list.append(item)

    def getEmployees(self):
        return self.list
    