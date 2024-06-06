# str1=input("Enter any string: ")
# lower=[]
# upper=[]
# special=[]


def Sort_Crit(str):

    str2=""
    str3=""

    for i in str:
        if(i.islower()==True):
            lower.append(i)
        elif(i.isupper()==True):
            upper.append(i)
        else:
            special.append(i)

    lower.sort()
    upper.sort()
    print(lower)
    print(upper)

    for i in lower:
        str2+=i

    for j in upper:
        str3+=j

    print(str2+str3)

import sys

str1=sys.stdin
str_sorted=sys.stdout

lower=[]
upper=[]
odd_digit=[]
eve_digit=[]
sorted_str=[]

str2=""
str3=""
odd_digits=""
eve_digits=""

for i in str1:
    if(i.islower()):
        lower.append(i)
    elif(i.islower()):
        upper.append(i)
    elif(i.isalnum()):
        digit=int(i)
        if(digit%2==0):
            even=str(digit)
            eve_digit.append(even)
        else:
            odd=str(digit)
            odd_digit.append(odd)
    else:
        exit(0)


lower.sort()
upper.sort()
odd_digit.sort()
eve_digit.sort()



for i in lower:
    str2+=i
sorted_str.append(str2)
for j in upper:
    str3+=j
sorted_str.append(str3)
for k in odd_digit:
    odd_digits+=k
sorted_str.append(odd_digits)
for l in eve_digit:
    eve_digits+=l
sorted_str.append(eve_digits)

for ele in sorted_str:
    str_sorted.write(ele)