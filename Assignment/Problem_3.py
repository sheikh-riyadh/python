def sum_total_number(*args):
    sum=0
    for num in args:
        sum+=num
    return sum


print(sum_total_number(10,20,30,40,50,74))



def details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


details(name="Sheikh muhammad riyadh hasan", department="Computer department")