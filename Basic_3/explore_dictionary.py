person={
    "name":"Sheikh riyadh",
    "age":25,
    "skin_color":"Brown"
}




# If we want to get the value we can use key instead of index
print(person["age"])


# If we want to modify any value
person["name"]="Sheikh muhammad riyadh hasan"
print(person)

# If we want to get the keys
print(person.keys())


# If we want to get the values
print(person.values())


# We can add new key and value 
person["father_name"]="Abbas ali"


# Delete value from dictionary
del person["age"]
print(person)