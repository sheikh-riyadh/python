# Set is a collection of unique value like we have an array or list if any duplicate value exist in the list or array set is remove all the duplicate value from the array or list like:

numbers_list = [3,1,2,2,1,3,4,5,6,4,7,5,8] # here we can see 2, 4 and 5 exist multiple times in the list


# if we want to remove the duplicate value from the list we can use set:
numbers_set = set(numbers_list)
print(numbers_set)


# If we want to add new value into set
numbers_set.add(70)
print(numbers_set)


# If we want to remove the specific number from set:
numbers_set.remove(70)
print(numbers_set)


# If we want to add a number which is already exist in the set the set is ignore the new number which is already exist




# Loop the set

for number in numbers_set:
    if number%2==0:
        print(number)
