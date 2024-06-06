# Create a program that allows the user to enter a list of numbers, and then performs the following:

# Returns Total no. of Elements(Length) of the List
# Adds an element to the end of List
# Display the first three elements of the list
# Display the last three elements of the list

# Display the middle three elements of the list
# Display the reversed list
# Display the trimmed list (the list without the first and last elements)
# Determines whether a given number is in the list

# Count the number of occurrences of a given number in the list
# Sort list in ascending order
# Sort list in descending order
# Finding the minimum and maximum values in the list

# Calculating the sum and average of the values in the list
# Removing duplicate values from the list
# Sorting the list by a specified criteria
# Searching for a given value in the list

# Splitting the list into two sublists
# Merging two lists
# Remove an Element from the List
# Insert an Element from the List
# Pop an Element from the List



import math as m
from enum import Enum
import LIST_METHODS.LIST_PROJECT_FUNCTIONS as lst_func
def Int_List():

    flag=1

    print("WELCOME TO THE LIST PROJECT")
    print("CREATE YOUR OWN LIST")
    print("PERFORM ALL DIVERSE FUNCTIONS BASED ON YOUR CHOICE ALONG WITH VARIATIONS")

    print("\nFunctions based on Choice Number are: ")
    print("\t[1]:  Find Length of the List")
    print("\t[2]:  Add an Element to the end of the List")
    print("\t[3]:  Display First 3 Elements of the List")
    print("\t[4]:  Display Last 3 Elements of the List")
    print("\t[5]:  Display Middle 3 Elements of the List")
    print("\t[6]:  Reverse the List")
    print("\t[7]:  Display Trimmed List without first and last elements of the Original List")
    print("\t[8]:  Find Whether a Given number is in the List")
    print("\t[9]:  Find the No. of Occurrences of a Number in the List")
    print("\t[10]: Display List Sorted in Ascending/Descending Order")
    print("\t[11]: Finding the Minimum and Maximum Values in the List")
    print("\t[12]: Calculating the Sum and Average of the Values in the List")
    print("\t[13]: Making the List Consist only Unique Elements")
    print("\t[14]: Sorting the List by a Specific Criteria")
    print("\t[15]: Searching for a Given Value in the List")
    print("\t[16]: Splitting the List Into Two Sublists")
    print("\t[17]: Merging Two Lists")
    print("\t[18]: Remove an Element from the List")
    print("\t[19]: Insert an Element in the List")
    print("\t[20]: Pop an Element from the List")

    class Choice(Enum):
        LEN=1
        APPEND=2
        DIS_F3=3
        DIS_L3=4
        DIS_M3=5
        REV_LST=6
        TRIM_LST=7
        IS_PRESENT=8
        COUNT=9
        SORT=10
        MIN_MAX=11
        SUM_AVG=12
        UNQ_LST=13
        SORT_CRIT=14
        SEARCH=15
        SPLIT_LSTS=16
        MERGE_LSTS=17
        REMOVE_ELE=18
        INSERT_ELE=19
        POP_ELE=20


    print("\nFirst We Have To Create A List of Integer Numbers To Perform Functions on it")
    print("----------------------------------------------------------------------------------------------------------")

    size=int(input("\nEnter the no. of elements of integer list: "))
    list=[]

    for i in range(0,size):
        num=int(input("Enter integer element: "))
        list.append(num)

    print("\nOriginal list of numbers: ",list)
    print("Length of list is: ", lst_func.len_list(list))
    len=lst_func.len_list(list)
    print("----------------------------------------------------------------------------------------------------------")

    while(flag==1):
        print("\n\n==========================================================================================================")
        choice=int(input("Enter your choice: "))

        if(choice==Choice.LEN.value):
            print("\nList of numbers: ",list)
            print("Length of list is: ",lst_func.len_list(list))
            print("==========================================================================================================")

        elif(choice==Choice.APPEND.value):
            print("\nList of numbers: ",list)
            lst_func.append_list(list)
            print("==========================================================================================================")

        elif(choice==Choice.DIS_F3.value):
            lst_func.F3(list,len)
            print("==========================================================================================================")

        elif(choice==Choice.DIS_L3.value):
            lst_func.L3(list,len)
            print("==========================================================================================================")

        elif(choice==Choice.DIS_M3.value):
            lst_func.M3(list,len)
            print("==========================================================================================================")

        elif(choice==Choice.REV_LST.value):
            lst_func.Reverse(list)
            print("==========================================================================================================")

        elif(choice==Choice.TRIM_LST.value):
            lst_func.Trimmed_List(list,len)
            print("==========================================================================================================")

        elif(choice==Choice.IS_PRESENT.value):
            target_value=int(input("\nEnter the value to be found in list: "))
            lst_func.is_Present(list,target_value)
            print("==========================================================================================================")

        elif(choice==Choice.COUNT.value):
            multiple_value=int(input("\nEnter the no. with multiple occurrences: "))
            lst_func.Count_Occur(list,multiple_value)
            print("==========================================================================================================")

        elif(choice==Choice.SORT.value):

            print("\n---------------------------------------------------------------------------------------------------------")
            print("Choice Values for Sorting Order:")
            print("\tAscending Order  : 0")
            print("\tDescending Order : 1")
            print("---------------------------------------------------------------------------------------------------------")

            order=int(input("\nEnter a boolean value for choosing sort order: "))
            lst_func.Sort(list,order)
            print("==========================================================================================================")

        elif(choice==Choice.MIN_MAX.value):

            print("\n---------------------------------------------------------------------------------------------------------")
            print("Choice Values To Determine Minimum/Maximum Element:")
            print("\tMinimum : 0")
            print("\tMaximum : 1")
            print("---------------------------------------------------------------------------------------------------------")

            n=int(input("\nEnter a boolean value to determine min or max value: "))
            lst_func.MIN_MAX(list,n)
            print("==========================================================================================================")

        elif(choice==Choice.SUM_AVG.value):

            print("\n---------------------------------------------------------------------------------------------------------")
            print("Choice Values To Determine Minimum/Maximum Element:")
            print("\tSum     : 0")
            print("\tAverage : 1")
            print("---------------------------------------------------------------------------------------------------------")

            a=int(input("\nEnter a boolean value to determine sum or average: "))
            lst_func.SUM_AVG(list,len,a)
            print("==========================================================================================================")

        elif(choice==Choice.UNQ_LST.value):
            lst_func.Make_Unique(list)
            print("==========================================================================================================")

        elif(choice==Choice.SORT_CRIT.value):

            print("\n---------------------------------------------------------------------------------------------------------")
            print("Choice Values for Sorting Order:")
            print("\tAscending Order  : 0")
            print("\tDescending Order : 1")
            print("---------------------------------------------------------------------------------------------------------")

            order2=int(input("\nEnter a boolean value for choosing sort order: "))

            print("\n---------------------------------------------------------------------------------------------------------")
            print("Choice Values for Specifying Criteria:")
            print("\tLength of List  : 0")
            print("\tCharacter Count : 1")
            print("\tVowel Count     : 2")
            print("---------------------------------------------------------------------------------------------------------")

            criteria =int(input("\nEnter a criteria number to sort in a specific order: "))
            lst_func.Sort_Criteria(order2,criteria)
            print("==========================================================================================================")

        elif(choice==Choice.SEARCH.value):

            search_element=int(input("\nEnter the element to be searched: "))
            lst_func.Search(list,len,search_element)
            print("==========================================================================================================")

        elif(choice==Choice.SPLIT_LSTS.value):

            lst_func.Split_Lists(list,len)
            print("==========================================================================================================")

        elif(choice==Choice.MERGE_LSTS.value):

            lst_func.Merge_Lists(list)
            print("==========================================================================================================")

        elif(choice==Choice.REMOVE_ELE.value):

            target=int(input("\nEnter the element to be removed from the list: "))

            print("\n---------------------------------------------------------------------------------------------------------")
            print("Choice Values To Determine Occurremces of an Element to be Removed:")
            print("\tFirst Occurrence : 0")
            print("\tAll Occurrences  : 1")
            print("\tDuplicate        : 2")
            print("---------------------------------------------------------------------------------------------------------")

            remove_occur=int(input("\nEnter the no. of occrrences you want to remove: "))
            lst_func.Remove_element(list,len,target,remove_occur)
            print("==========================================================================================================")

        elif(choice==Choice.INSERT_ELE.value):
            target_element=int(input("\nEnter the element to be inserted in the list: "))

            print("\n---------------------------------------------------------------------------------------------------------")
            print("Choice Values To Determine where Element is to be Inserted:")
            print("\tRandom Position : 0")
            print("\tSorted Position : 1")
            print("---------------------------------------------------------------------------------------------------------")

            index_choice=int(input("\nEnter a value to choose where to insert the element: "))
            lst_func.Insert_Element(list,len,index_choice,target_element)
            print("==========================================================================================================")

        elif(choice==Choice.POP_ELE.value):

            print("\n---------------------------------------------------------------------------------------------------------")
            print("Choice Values To Determine Position of Element to be Popped:")
            print("\tLast Index  : 0")
            print("\tRandom      : 1")
            print("---------------------------------------------------------------------------------------------------------")

            choice_index=int(input("\nEnter a value to determine position of element to be popped: "))
            lst_func.Pop_Element(list,len,choice_index)
            print("==========================================================================================================")

        else:
            print("\nInvalid Input! Out of Range Choice No. due to Limited Functions")
            print("EXIT: Try Again Later")
            flag=0
            print("==========================================================================================================")


Int_List()