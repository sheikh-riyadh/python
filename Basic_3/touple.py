# Touple like a touple but not the same



# index (+) : 0        1        2         3
fruits = ("Banana", "Apple", "Pinaple", "Orange")
# index (-) : -4      -3       -2        -1


# We can't able to reassign the string like:
fruits[0]='M'

# We can access the touple element using index
print(fruits[0])


# touple(start : end ) start from the start index and stop before the end index
print(fruits[2:5]) 


# touple(start : end : steps)
print(fruits[2:9:2])

# touple(start : end ) print reverse order
print(fruits[6:2:-1])

# touple(start : end : steps) print reverse order with 2 steps
print(fruits[11:3:-2])

# print from start to last index
print(fruits[5:])

# print end index to start index
print(fruits[:5])

# print first to last index with 2 steps or as we want steps
print(fruits[::2])

# print first to last index
print(fruits[:])

# print reverse the full touple or array
print(fruits[::-1])


# Index :  {           0             }  {          1       }  {    2    }    
fruits_1= (["Banana","Apple","Orange"], ["Jackfood","lemon"], ["Pinaple"])
# Index        0        1       2           0          1           0


# We know list is changable here we can see list exist in touple one think we know we can't able to change touple but we can change list in the touple like:

fruits_1[1][0] = "Mango"
print(fruits_1)

