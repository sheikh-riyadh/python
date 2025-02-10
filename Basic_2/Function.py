def multiply(pera):
    for num in range(1,11):
        print(f'{pera} X {num} = {pera*num}')

multiply(10)



# Default perameter
def double_it (num1, num2=0):
    return num1*num2
print(double_it(10,20))


# args perameter
def total_sum (*args):
    sum=0
    for num in args:
        sum+=num
    return sum

print(total_sum(10,20,30,40,50))


# first two peramter mandatory 

def multiplication(num1, num2, *args):
    sum=0
    for num in args:
        sum+=num
    print(sum)
    return num1*num2

result = multiplication(10,20,54,68,69,8,12)
print(result)