class Person:
    def walk(self):
        print("Person is walking")
    
    def talk(self):
        print("Person is talking")

class Student(Person):          # Student inherits Person
    def study(self):
        print("Student is studying")
    
    def attend_class(self):
        print("Student is attending class")

# Create object and call all methods
s = Student()
s.walk()           # inherited from Person
s.talk()           # inherited from Person
s.study()          # own method
s.attend_class()   # own method