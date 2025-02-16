class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_balance =100
        self.max_balance = 100000
    

    def withdraw(self, withdraw_balance):
        if self.balance < withdraw_balance:
            print("You don't have enough balance")
        elif self.min_balance > withdraw_balance:
            print(f"You must have withraw minimum {self.min_balance} TK")
        elif self.max_balance < withdraw_balance:
            print(f"You don't withdraw more than {self.max_balance} TK")
        else:
            self.balance-=withdraw_balance
            print(f"withdraw success ! your new balance is {self.balance}")


    def deposit(self, new_balance):
        if new_balance<0:
            print(f"Please deposit minimum {self.min_balance}")
        else:
            self.balance+=new_balance
            print(f"deposit success ! your new balance is {self.balance}")



sheikh = Bank(100000)
print(sheikh.balance)

hasan = Bank(5000)
print(hasan.balance)


