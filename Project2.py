def PatternLA(n):
    for i in range(0,n+1):
        for j in range(0,i):
            print("*",end=" ")
        print(" ")
    print("\n")

def PatternLD(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print(" ")
    print("\n")
def PatternRA(n):
    str="* "
    str_emp="  "
    for i in range(0,n+1):
        str*=i
        for j in range(n-(i-1),0,-1):
            str_emp*=j
            print(str+str_emp)
            break
        str="* "
        str_emp="  "
    print("\n")
def PatternRD(n):
    str="* "
    str_emp="  "
    for i in range(0,n+1):
        str_emp*=i
        for j in range(n-i,0,-1):
            str*=j
            print(str_emp+str)
            break
        str="* "
        str_emp="  "
    print("\n")

def PatternMA(n):
    str="* "
    str_emp=" "
    for i in range(0,n+1):
        str*=i
        for j in range(n-(i-1),0,-1):
            str_emp*=j
            print(str_emp+ str)
            break
        str="* "
        str_emp=" "
    print("\n")

def PatternMD(n):
    str="* "
    str_emp=" "
    for i in range(0,n+1):
        str_emp*=i
        for j in range(n-i,0,-1):
            str*=j
            print(str_emp+str)
            break
        str="* "
        str_emp=" "
    print("\n")


n=int(input("Enter the no. of rows: "))
PatternLA(n)
PatternLD(n)
PatternRA(n)
PatternRD(n)
PatternMA(n)
PatternMD(n)
