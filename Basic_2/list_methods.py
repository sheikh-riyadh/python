#index (+):   0   1   2   3   4    5   6   7  8   9   10   11
numbers  =  [ 10, 20, 30, 40, 50, 60, 70, 80, 9, 100, 110, 120]
#index (-):  -12 -11 -10  -9  -8  -7  -6  -5 -4   -3   -2  -1



# add the new value in last position
numbers.append(88)


# insert a new value with specific position list.insert(index, value)
numbers.insert(2, 0)

# remove value from the list
if 44 in numbers:
    numbers.remove(44)

# remove last index value from the list
numbers.pop()


# Get the index number a specific value from list
if 44 in numbers:
    numbers.index(44)


# sort the list assending order
numbers.sort()


# reverse value from list
numbers.reverse()