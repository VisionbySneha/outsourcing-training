class Instagram:
    __password = "Akshay12345" 
    __followers = 500 

    def change_password(self,old,new):
        if old == self.__password:
            self.__password = new
            print("password changed successfully")
        else :
            print("Wrong password")

    def add_follower(self):
        self.__followers += 1
        print(f"New Follower ! Total : {self.__followers}")


    def get_followers(self):
        print(f"Followers : {self.__followers}")


acc = Instagram()
acc.change_password("rahul@123","newpass@4567")
acc.add_follower()
acc.get_followers()

print(acc.__password)
print(acc.__followers)