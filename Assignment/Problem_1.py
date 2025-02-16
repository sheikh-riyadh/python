
l_count=0
r_count =0
balance_count=0
result = ""
result_arr = []

b_string = input("Enter balance string : ")




for char in b_string:
    result += char
    if char =='R':
        r_count+=1
    else:
        l_count+=1

    if r_count == l_count:
            balance_count+=1
            result_arr.append(result)
            result=""
    
    

print(balance_count)
for result in result_arr:
    print(result)