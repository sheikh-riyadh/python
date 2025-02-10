#index (+):   0   1   2   3   4    5   6   7  8   9   10   11
numbers  =  [ 10, 20, 30, 40, 50, 60, 70, 80, 9, 100, 110, 120]
#index (-):  -12 -11 -10  -9  -8  -7  -6  -5 -4   -3   -2  -1



# list(start : end ) start from the start index and stop before the end index
print(numbers[2:5]) 


# list(start : end : steps)
print(numbers[2:9:2])

# list(start : end ) print reverse order
print(numbers[6:2:-1])

# list(start : end : steps) print reverse order with 2 steps
print(numbers[11:3:-2])

# print from start to last index
print(numbers[5:])

# print end index to start index
print(numbers[:5])

# print first to last index with 2 steps or as we want steps
print(numbers[::2])

# print first to last index
print(numbers[:])

# print reverse the full list or array
print(numbers[::-1])