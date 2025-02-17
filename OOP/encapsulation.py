""" 
Access modifier
===============

Private : If we create a property with double underscore it's call "private" property.

Example:
========
__Name
__Roll




Protected : If we create a property with single underscore it's call "protected" property.

Example:
========

_name,
_roll



Public : If we not mention anything it's call "public" property .

Example:
========

name,
roll


 """


class Bank:
    def __init__(self, balance):
        self.__balance = balance
    
    def withdraw(self, withdraw_balance):
        if self.__balance<withdraw_balance:
            print(f"You don't have enough balance {self.__balance}")
        else:
            self.__balance-=withdraw_balance
            print(f"Withdraw success ! new balance is {self.__balance}")



obj = Bank(500000,1000)
# print(obj.__balance) # We can not access the balance cz the balance attribute is private

print(obj.withdraw(100000))