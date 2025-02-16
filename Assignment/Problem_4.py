operation_count=0
numbers=[]
isContinue=True
numbers_len = int(input("Enter list length : "))

for num in range(numbers_len):
    value = int(input("Enter value : "))
    numbers.append(value)



while isContinue:
    for i,num in enumerate(numbers):
        if num%2==0:
            numbers.pop(i)
            numbers.insert(i,num//2)
            if i == numbers_len-1:
                operation_count+=1
        else:
           isContinue=False
           break


print(operation_count)