class Teacher:
    def teach(self):
        print("Teacher is teaching")

class Principal:
    def manage_school(self):
        print("Principal is managing school")

class HeadTeacher(Teacher, Principal):   # inherits BOTH
    def take_assembly(self):
        print("HeadTeacher is taking assembly")

# Create object and call all methods
ht = HeadTeacher()
ht.teach()           # from Teacher
ht.manage_school()   # from Principal
ht.take_assembly()   # own method