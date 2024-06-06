# Create a program that allows the user to enter a list of numbers, and then prints out the following:

# The first three elements of the list
# The last three elements of the list
# The middle three elements of the list
# The reversed list
# The trimmed list (the list without the first and last elements)
# Whether a given number is in the list
# The number of occurrences of a given number in the list
# The sorted list in ascending order
# The sorted list in descending order

# Finding the minimum and maximum values in the list
# Calculating the sum and average of the values in the list
# Removing duplicate values from the list
# Sorting the list by a specified criteria
# Searching for a given value in the list
# Splitting the list into two sublists
# Merging two lists

import math as m
from enum import Enum
def Int_List():
    size=int(input("Enter the no. of elements of integer list: "))
    list=[]

    for i in range(0,size):
        num=int(input("Enter integer element: "))
        list.append(num)

    print("\nOriginal list of numbers: ",list)
    print("\nLength of list is: ",len_list(list))
    len=len_list(list)

    # F3(list,len)
    # L3(list,len)
    # M3(list,len)
    # Reverse(list)
    # Trimmed_List(list,len)
    #
    # target_value=int(input("\nEnter the no. to be searched: "))
    # is_Present(list,target_value)
    #
    # multiple_value=int(input("\nEnter the no. with multiple occurrences: "))
    # Count_Occur(list,multiple_value)
    #
    # order=bool(input("\nEnter a boolean value for choosing sort order: "))
    # Sort(list,order)
    #
    # n=bool(input("\nEnter a boolean value to determine min or max value: "))
    # MIN_MAX(list,n)
    #
    # a=bool(input("\nEnter a boolean value to determine sum or average: "))
    # SUM_AVG(list,len,a)
    #
    # Make_Unique(list)

    # list2=["india","brazil","netherlands","usa","australia"]
    order2=bool(input("\nEnter a boolean value for choosing sort order: "))
    criteria =int(input("Enter a criteria number to sort in a specific order: "))
    Sort_Criteria(order2,criteria)

    # search_element=int(input("\nEnter the element to be searched: "))
    # Search(list,len,search_element)

    # Split_Lists(list,len)

    Merge_Lists(list)

    # append_list(list)


    # target=int(input("Enter the element to be removed from the list: "))
    # remove_occur=int(input("Enter the no. of occrrences you want to remove: "))
    # Remove_element(list,len,target,remove_occur)

    # target_element=int(input("\nEnter the element to be inserted in the list: "))
    # index_choice=int(input("Enter a value to choose where to insert the element: "))
    # Insert_Element(list,len,index_choice,target_element)

    # choice_index=int(input("Enter a value to determine position of element to be removed: "))
    # Pop_Element(list,len,choice_index)

def len_list(l):

    return  len(l)


def append_list(l):

    n=int(input("\nEnter the element to be inserted at last: "))
    l.append(n)
    print("Updated List: ",l)

def F3(l,len):

    print("\nFirst 3 elements of list are: ")
    if(len<3):
        print("Invalid Request! Inadequate Length")
    else:
        print(l[0:3])
        # for i in range(0,3):
        #     print(l[i])

def L3(l,len):

    print("\nLast 3 elements of list are: ")
    if(len<3):
        print("Invalid Request! Inadequate Length")
    else:
        print(l[len-3:len])
        # for i in range (len-3,len):
        #     print(l[i])

def M3(l,len):

    print("\nMiddle 3 elements of list are: ")
    if(len<5):
        print("Invalid Request! Inadequate Length")
    else:
        mid=m.floor(len/2)
        print(l[mid-1:mid+2])
        # for i in range(mid-1,mid+2):
        #     print(l[i])

def Reverse(l):

    print("\nReverse List is:\n",l[::-1])

def Trimmed_List(l,len):

    print("\nTrimmed List:")
    if(len<2):
        print([])       #Empty String
    else:
        print(l[1:len-1])

def is_Present(l,target):

    if(target in l):
        print(f"First Occurrence of element {target} in the list is at index {l.index(target)} ")
    else:
        print(f"Element {target} is not present in the list")

def Count_Occur(l,multiple):

    if(multiple in l):
        print(f"Element {multiple} occurs a total of {l.count(multiple)} time(s) in the list")
    else:
        print(f"Element {multiple} does not occur even once in the list")

def Sort(l,n):

    class Order(Enum):
        ASC=0
        DESC=1

    if(n==Order.ASC.value):
        l.sort()
        print("List in Ascending order: ",l)
    else:
        l.sort()
        l.reverse()
        print("List in Descending Order: ",l)


def MIN_MAX(l,n):

    class Min_Max(Enum):
        MIN=0
        MAX=1

    if(n==Min_Max.MIN.value):
        print("Element with Minimum Value: ",min(l))
    else:
        print("Element with Maximum Value: ",max(l))

def SUM_AVG(l,len,a):

    class Sum_Avg(Enum):
        SUM=0
        AVG=1

    if(a==Sum_Avg.SUM.value):
        print("Sum of all elements of the list: ",sum(l))
    else:
        print("Average of all elements of the list: ",sum(l)/len)

def Make_Unique(l):

    l2=set(l)
    l3=list(l2)

    print("\nList with non-duplicate values are: ",l3)

def Sort_Criteria(n,crit):

    size=int(input("\nEnter the no. of elements of list: "))
    list2=[]

    for i in range(0,size):
        str=input("Enter string element: ")
        list2.append(str    )

    class Order(Enum):
        ASC=0
        DESC=1

    class Criteria(Enum):
        LEN=0
        CHAR_COUNT=1
        VOWEL_COUNT=2

    if(crit==Criteria.LEN.value):

        print("\nList Sorted by Length of Element")

        def Length(list2):
            return  len(list2)

        if(n==Order.ASC.value):
            list2.sort(key=Length)
            print("List in Ascending order: ",list2)
        else:
            list2.sort( reverse=True ,key=Length)
            print("List in Descending Order: ",list2)

    elif(crit==Criteria.CHAR_COUNT.value):

        print("\nList Sorted by Character Count")
        char=input("Enter a character to determine a specific sort order: ")

        def Count_char(ele):
            return ele.count(char)

        if(n==Order.ASC.value):
            list2.sort(key=Count_char)
            print("List in Ascending order: ",list2)
        else:
            list2.sort(reverse=True,key=Count_char)
            print("List in Descending Order: ",list2)

    elif(crit==Criteria.VOWEL_COUNT.value):

        print("\nList Sorted By Vowel Count")
        def Vowel_Count(ele):
            total=0
            for vowel in "aeiou":
                total+=ele.count(vowel)
            return total

        if(n==Order.ASC.value):
            list2.sort(key=Vowel_Count)
            print("List in Ascending order: ",list2)
        else:
            list2.sort(reverse=True, key=Vowel_Count)
            print("List in Descending Order: ",list2)

    else:

        print("Invalid Input! No other criterias available")

def Search(l,len,val):

    if val in l:
        print(f"Element {val} is present  at index {l.index(val)} in the list")
    else:
        print(f"Element {val} is not present in the list")

def Split_Lists(l,len):

    print("\nSplitting A List Into Two Sublists")
    mid=m.floor(len/2)
    list2,list3=[],[]

    for i in range(0,mid+1):
        list2.append(l[i])

    for j in range(mid+1,len):
        list3.append(l[j])

    print("First Sublist: ",list2)
    print("Second Sublist: ",list3)

def Merge_Lists(l1):

    size=int(input("\nEnter the no. of elements of list: "))
    l2=[]

    for i in range(0,size):
        str=input("Enter string element: ")
        l2.append(str)

    print("\nMerging Two Lists")
    l3=l1.copy()
    l3.extend(l2)

    print("Merged List: ",l3)


def Remove_element(l,len,val,remove):

    class Remove(Enum):
        FIRST_OCCUR=0
        ALL_OCCUR=1
        DUPLICATE=2

    if val in l:
        if( remove==Remove.FIRST_OCCUR.value):
            l.remove(val)
            print("Updated List: ",l)
        elif( remove==Remove.ALL_OCCUR.value):
            while(l.count(val)!=0):
                l.remove(val)
            print("Updated List: ",l)
        elif(remove==Remove.DUPLICATE.value):
            while(l.count(val)!=1):
                l.remove(val)
            print("Updated List: ",l)
        else:
            print("Invalid Input! Specify choice of the no. of occurrences you want to remove ")

    else:
        print(f"Element {val} is not present in the list")

def Insert_Element(l,len,choice,ele):

    class Insert_Element(Enum):
        RANDOM=0
        SORTED=1

    if(choice==Insert_Element.RANDOM.value):
        index=int(input("\nEnter the index position where you want to insert the element: "))
        if(index<len | index>(-len)):
            l.insert(index,ele)
            print("Updated List: ",l)
        else:
            print("IndexError! Index Out of Range")

    elif(choice==Insert_Element.SORTED.value):

        class Order(Enum):
            ASC=0
            DESC=1

        order=int(input("\nEnter a value to determine sort order: "))

        if(order==Order.ASC.value):
            l.sort()
            for i in range(1,len-1):
                if(ele>l[i-1] & ele<=l[i]):
                    l.insert(i+1,ele)
                    break
            print("Updated List in Ascending Order: ",l)

        elif(order==Order.DESC.value):
            l.sort()
            for i in range(1,len-1):
                if(ele>l[i-1] & ele<=l[i]):
                    l.insert(i+1,ele)
                    break
            l.reverse()
            print("Updated List in Descending Order: ",l)

        else:
            print("Invalid Input! Choose Sort Order carefully")

    else:
        print("Invalid Input! Try Again")

def Pop_Element(l,len,choice):

    class Pop_index(Enum):
        LAST_INDEX=0
        RANDOM=1

    if(choice==Pop_index.LAST_INDEX.value):
        print(f"\nPopped element from the list: {l.pop()}")
        print("Updated List:",l)

    elif(choice==Pop_index.RANDOM.value):
        index=int(input("\nEnter the index postion from where the element is to be removed: "))
        if(index<len | index>= (-len)):
            print(f"Popped element from the list: {l.pop(index)}")
            print("Updated List:",l)
        else:
            print("Invalid Input! Index Bound Out of Range")

    else:
        print("Invalid Input! Try Again with an available choice")

Int_List()