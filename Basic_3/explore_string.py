

# We can write string in a 3 ways 1. single quotation (' ') 2. double quotation (" ") 3. (""" """)
name_1 = 'Sheikh Riyadh\'s' 
name_2 = "Sheikh muhammad riyadh hasan"

# This are called multiline string
name_3 = """ 

Sheikh muhammad
Riyadh hasan

 """


# String is sequance of character string can perform like list not the same here is some key point of differance like: 1.string is a immutable that means we can't able to modifiy the string 2. we can't push or append new value or not assign a new value name = "Sheikh riyadh" name[2]="m" here is some example:


# We can't able to reassign the string like:
name_1[0]='M'

# We can access the specific of index value
print(name_1[2]) 

# We can perform like list but not the some list(start : end)
print(name_1[1:5])


# Another example list(start : end : steps)
print(name_1[0::2])