# Class atribute shared they are data to all the instance 

class Shop:
    cart=[]
    def add_to_cart(self, item):
        self.cart.append(item)


sheikh = Shop() # "Sheikh" is a instance of "Shop class"
sheikh.add_to_cart("Samsung s25 ultra")
print(sheikh.cart)


hasan = Shop()
hasan.add_to_cart("Samsung watch")
print(hasan.cart) # Out put is ["Samsung s25 ultra","Samsung watch"]


""" 

If we notice that the "Samsung s25 ultra" was not added the sheikh when we trying to see output
of hasan "cart" the output was show ["Samsung s25 ultra","Samsung watch"] 
but the "Samsung s25 ultra" not added hasan so why we see out "Samsung s25 ultra"?
Because of "Class atribute" When we use class atribute into class, the atribute data show all of 
the instance

 """

