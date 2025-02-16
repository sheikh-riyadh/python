# We will learn how do we diclear a class and access the class property:

class Phone :
    brand="Samsung"
    color="Black"
    price=341


my_phone = Phone()

# We can access the Phone property with 3 way like:

# NO 01:
print(my_phone.brand)

# NO 02:
print(Phone.brand)

# NO 03:
print(Phone().brand)