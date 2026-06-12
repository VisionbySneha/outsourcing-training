from abc import ABC,abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def check_balance(self):
        pass



class SBI(ATM):
    def withdraw(self):
        server = "SBI CORE BANKING SERVER"
        language = "Java 8"
        database = "Oracle DB"


        print("Cash Withdraw Sucessfully")



    def check_balance(self):
        server = "SBI CORE BANKING SERVER"
        language = "Java 8"
        database = "Oracle DB"
    
        print("Balance: 100000")


sbi =SBI()
sbi.withdraw()
sbi.check_balance()



