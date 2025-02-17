# Base class or perant class

class Features:
    def __init__(self, brand, price, color, ram):
        self.brand = brand
        self.price = price
        self.color = color
        self.ram = ram
    
    def show_details(self):
        print(f"Brand : {self.brand} \n Price : {self.price} \n color : {self.color} \n Ram : {self.ram}")


# Child class
class Laptop(Features):
    def __init__(self, brand, price, color, ram, motherboard):
        self.motherboard = motherboard
        super().__init__(brand, price, color, ram)


# Child class
class Phone (Features):
    def __init__(self, brand, price, color, ram, sensor, display):
        self.sensor = sensor
        self.display = display
        super().__init__(brand, price, color, ram)





""" 
Now the question is how we got "brand, price, color, ram" this atribute is own
by "Feature" class but we inherite "Laptop" class how is this posible?

Answer:
Because "Laptop" class already inherited the "Feature" class so that all of the atributes
are available in "Laptop" class 

When we inherited "Laptop" class in "Desktop" class that's why we got "brand, price, color, ram"
in the "Desktop" class because of in "Laptop" class inherited "Feature" class that's why "brand, price, color ram" are avaible in "Laptop" class so that we got "brand, price, color, ram" this atribute 


"""
class Desktop(Laptop):
    def __init__(self, brand, price, color, ram, motherboard,casing):
        self.casing = casing
        super().__init__(brand, price, color, ram, motherboard)




my_desktop = Desktop("Asus",150000,"black",32,"MSI","PC Power 180B Mid-Tower ATX Desktop Casing")
print(my_desktop.casing)


my_phone = Phone("I Phone", 200000, "black", 16,"Dragoan","Gorila" )
print(my_phone.brand)


my_laptop = Laptop("Asus",200000, "Silver", 32, "MSI")
print(my_desktop.price)

