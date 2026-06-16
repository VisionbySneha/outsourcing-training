class Grandfather:
    def __init__(self,name):
        self.name = name

    def property(self):
        print(f"{self.name} owns a house")


class Father (Grandfather):
    def business(self):
        print(f"{self.name} runs a shop")

class Son(Father):
    def study(self):
        print(f"{self.name} is studying")

s = Son("Rahul")
s.property()
s.business()
s.study()


