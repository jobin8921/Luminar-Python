# creatae a class for bank attributes
# name ,place,account_type,balance,bank_name

#methods: show_details,deposit,withdrawal,balance
class Bank:

    name:str
    place:str
    account_type:str
    balance:int
    bank_name="SBI Bank"

    def __init__(self,name,place,account_type,balance):
        self.name=name
        self.place=place
        self.account_type=account_type
        self.balance=balance
        

    def show_details(self):
        print(f"{self.name},{self.place},{self.account_type},{self.balance}")

    def deposit(self,amount):
        self.amount= amount
        self.balance=self.balance + self.amount

        print(f"{self.balance}")

    def withdrwal(self,amount):
        self.amount=amount
        if self.balance < self.balance :
            self.balance=self.balance-amount
            print(f"Transcation sucessfull your available balance is {self.balance}")   

        else:
            print(f"Insufficent balance of {self.balance} - {self.amount}")

obj1=Bank(name="josel",account_type="savings",place="kochi",balance=1000)

obj1.show_details() 
# obj1.deposit(amount=4000)
obj1.withdrwal(amount=5000)


