class School:
    def infrastructure(self):
        print("School has buildings and grounds")

class Department(School):        # Level 2
    def department_name(self):
        print("This is the Science Department")

class Classroom(Department):     # Level 3
    def total_students(self):
        print("Total students in classroom: 40")

# Create object of Classroom and call all methods
c = Classroom()
c.infrastructure()    # from School (grandparent)
c.department_name()   # from Department (parent)
c.total_students()    # own method