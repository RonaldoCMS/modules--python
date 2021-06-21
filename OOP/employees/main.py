from listEmployee import ListEmployee 
from employee import Employee

list = ListEmployee()
list.addEmployee(Employee("Fabio", "Danubbio", "Developer"))
list.addEmployee(Employee("Fabio", "Danubbio", "Developer"))
list.addEmployee(Employee("Fabio", "Danubbio", "Developer"))
print(list.getEmployees())