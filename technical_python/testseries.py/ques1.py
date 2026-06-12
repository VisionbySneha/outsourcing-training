class Employee:
    def __init__(self):
        self.__salary = 50000

    def increment(self):
        self.__salary += 10000
        print(self.__salary)

    def deduct(self):
        self.__salary -= 5000
        print(self.__salary)

    def get_salary(self):
        print(self.__salary) 

e = Employee()
e.increment()
e.deduct()
e.get_salary()

