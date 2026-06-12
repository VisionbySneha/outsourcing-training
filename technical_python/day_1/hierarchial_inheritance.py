class Father:
    def property(self):
        print("Father owns a house")
    
    def money(self):
        print("Father has money")

class Son(Father):
    def cricket(self):
        print("Son plays cricket")

class Daughter(Father):
    def dance(self):
        print("Daughter loves Dancing")

class YoungSon(Father):
    def gaming (self):
        print("Young Son plays games")

s = Son()
s.property()
s.cricket()

d = Daughter()
d.property()
d.dance()

y = YoungSon()
y.property()
y.gaming()
