# Base class or perant class

class Features:
    def __init__(self, brand, price, color, ram):
        self.brand = brand
        self.price = price
        self.color = color
        self.ram = ram


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