from abc import ABC,abstractmethod

class Principal(ABC):

    @abstractmethod
    def wear_uniform(self):
        pass

    @abstractmethod
    def do_homework(self):
          pass



class Student(Principal):
    def wear_uniform(self):
            print("Uniform pehen li!")


    def do_homework(self):
            print("Homework kar liya!")

s = Student()
s.wear_uniform()
s.do_homework()
        
    