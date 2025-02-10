numbers = [2,3,8,7,9,6,45]
odd_numbers=[]

for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

print(odd_numbers)

# list comprehension

odd_numbers_2 = [num for num in numbers if num % 2 ==1]
print(odd_numbers_2)