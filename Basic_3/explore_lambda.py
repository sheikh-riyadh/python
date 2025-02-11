
numbers  =  [ 10, 20, 30, 40, 50, 60, 70, 80, 9, 100, 110, 120]
# If we want to create function with nano verison we can use lambda function like:


def doubled(num):
    return num*num

# We can create the doubled function nano version using lambda keyword
doubled_2 = lambda num:num*num
result= doubled_2(20)
print(result)


add = lambda x,y:x+y
result_2= add(10,20)
print(result_2)


# Map function
result_3 = map(lambda nums:nums*2, numbers)
print(list(result_3))


# Filter function
result_4 = filter(lambda num: num>20, numbers)
print(list(result_4))