# If any probalitity to get error in code then we use try,except and finally


try:
    result = 45/0 # We know if any number divide by zero the result is infinite that's why we getting an error
except:
    print("catched the error") #This line is exicute



try:
    result= 40/0
except:
    print("Getting error")
finally:
    print("I am must exicute") # This line must exicute ather getting error or not the finally code must exicute

