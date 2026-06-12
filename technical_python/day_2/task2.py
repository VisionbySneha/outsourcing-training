class Mobile:
    def __init__(self):
        self.__battery = 100

    def charge(self):
        self.__battery += 10
        print(self.__battery)

    def use_phone(self):
        self.__battery -= 10
        print(self.__battery)
    
    def check_battery(self):
        print(self.__battery) 

m = Mobile()
m.charge()
m.use_phone()
m.check_battery()   