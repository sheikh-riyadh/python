balance = 3000

def buy_anything(item, price):
    # We can use global variable without using global keyword
    print(f"New balance buyed {item} {balance-price}")


def buy_anything_2(item, price):
    # we can use global variable without using global keyword but 
    # if we want to modify the main variable we must have use global keyword
    global balance
    balance = balance - price
    print(f"New balance buyed {item} {balance}")


buy_anything_2("Sunglasses",1000)
print("Now balance is outside of function",balance)