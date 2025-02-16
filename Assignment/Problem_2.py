n = int(input("Please enter N : "))
sequence = []
remove_count = 0
for _ in range(n):
    value = int(input("enter value : "))
    sequence.append(value)

for num in sequence:
    if sequence.count(num) == num:
        continue
    else:
        remove_count+=1
        sequence.remove(num)

print(remove_count)
