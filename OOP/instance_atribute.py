class Shop:
    def __init__(self):
        self.cart = []
    def add_to_cart(self , item):
        self.cart.append(item)



sheikh = Shop()
sheikh.add_to_cart("Samsung s25 ultra")

hasan = Shop()
hasan.add_to_cart("Samsung watch")


print(hasan.cart) 
print(hasan.cart) 


""" 
# If we trying to see the hasan cart output will show ["Samsung watch"]
# Same with If we trying to see the sheikh cart output will show ["Samsung s25 ultra"]


Now the question is why we don't see ["Samsung s25 ultra","Samsung watch"] output because of
instance atribute when we use instance atribute into the class Every object has its own copy of the instance attribute that's why we don't see ["Samsung s25 ultra","Samsung watch"] output

 """