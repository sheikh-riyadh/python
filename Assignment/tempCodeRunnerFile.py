b_string = input("Enter balance string : ")
l_count=0
r_count =0
balance_count=0
result = ""

result_arr = []




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
    

print(result_arr)
# for result in result_arr:
#     print(result)