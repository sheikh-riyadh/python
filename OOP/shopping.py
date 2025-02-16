class Shopping:
    def __init__(self):
        self.cart = []
    

    def add_to_cart(self, item_name, price, quantity):
        item ={
            "name":item_name,
            "price":price,
            "quantity":quantity
        }
        self.cart.append(item)

    def remove_item(self,item_name):
       self.cart = list(filter(lambda x: x["name"]!=item_name, self.cart ))
            


sheikh = Shopping()
sheikh.add_to_cart("Rice",60,5)
sheikh.add_to_cart("Potato", 35,5)
sheikh.add_to_cart("Oil", 210,5)
sheikh.add_to_cart("Onion", 25,5)
print(sheikh.cart)
sheikh.remove_item("Onion")
print(sheikh.cart)