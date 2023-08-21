class Employee:
  def __init__(self, name, salary, da, pf, age):
   self.name = name
   self.salary = salary
   self.da = da
   self.pf = pf
   self.age = age
  def calculate_net_salary(self):
   net_salary = self.salary + self.da - self.pf
   return net_salary
  def __str__(self):
   return f"Name: {self.name}, Salary: {self.salary}, DA: {self.da}, PF: {self.pf}, Age: {self.age}"
# Example usage
if __name__ == "__main__":
  employees = []
 # Create some employee objects
  employee1 = Employee("John Doe", 50000, 2000, 1500, 30)
  employee2 = Employee("Jane Smith", 60000, 2500, 2000, 35)
  employee3 = Employee("Bob Johnson", 70000, 3000, 2500, 28)
 # Add employees to the list
  employees.append(employee1)
  employees.append(employee2)
  employees.append(employee3)
 # Calculate and display net salaries for each employee
  print("Employee Information:")
  for employee in employees:
    net_salary = employee.calculate_net_salary()
    print(employee)
    print(f"Net Salary: {net_salary}\n")