def fullName(firstName, lastName):
    print(f"{firstName} {lastName}")





def full_name(**kargs):
    for key, value in kargs.items():
        print(f"{key} : {value}")

full_name(title="Hello", country="bangladesh")


# return multiple values from function:

def sum (num1, num2):
    sum = num1+num2
    mult= num1*num2
    sub = num1-num2
    return sum,mult,sub

result = sum(10,20)

for num in result:
    print(num)
