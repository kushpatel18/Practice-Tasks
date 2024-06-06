#                        Lists in Python
lst=[1,2,3]
lst2=["kush",20,19]

# Length of List(Counts all the elements irrespective of the datatype
print(len(lst2))

# Indexing and Slicing
lst3=["one","two","three"]
print(lst3[0])
print(lst3[1:])
print(lst3)
lst4=[4,5]
newlst=lst4+lst3
print(newlst)
# The original lists do not change
print(lst3)
print(lst4)

# Reassigning different value using Indexing
newlst[0]="four"
print(newlst)

# List Methods
newlst.append("six")
print(newlst)
newlst.append("seven")
print(newlst)
pop_item=newlst.pop()
print(newlst)
print(pop_item)
newlst.pop(1)    #Default value in brackets of pop is -1
print(newlst)


let_lst=['a','e','x','b','c']
num_lst=[4,1,8,3]

let_lst.sort()
print(let_lst)
sortedlst=num_lst.sort()  #printing this list gives no output
print(type(sortedlst))

num_lst.sort()
sortedlst2=num_lst
print(sortedlst2)
num_lst.reverse()
print(num_lst)


#                           Dictionaries
dict1={'Kush':385,'Mihir':411}
print(dict1)
print(dict1['Kush'])

prices = {'apple':2.99,'oranges':1.99,'milk':5.89}
print(prices['milk'])

dicto={'k1':123,'k2':[0,1,2],'k3':{'in_key':10}}
print(dicto['k2'])
print(dicto['k3'])
print(dicto['k3']['in_key'])
print(dicto['k2'][2])

dict2={'key1':[10,20,30]}

print(dict2)
lst=dict2['key1']
print(lst)
num=lst[2]
print(num)

print(dict2['key1'][2])

#         Dictionary Methods
d={'k1':100,'k2':200}
print(d)
d['k3']=300         #Adding a new element
print(d)
d['k1']='new_value' #Changing value associsted with a key
print(d)

print(d.keys())     #Displaying all the keys of dictionary
print(d.values())   #Displaying all the values associated with their respective keys
print(d.items())    #Displaying all key:value pairs using tuples


#                  TUPLES
t =(1,2,3)
lst = [1,2,3]
print(type(t))
print(type(lst))
print(len(t))
print(t)
t1=('one',2)
print(t1[-1])
print(t1[0])
t3 = ('a','a','b')
print(t3.count('a'))
print(t3.count('b'))
print(t3.index('a'))
print(t3.index('b'))
lst[0]='new'    #Lists are mutable,value can be changed using indexing
print(lst)
# t[0]='new' --> Tuples are immutable, therefore value already assigned cannot be changed
# print(t)



#                    SETS
set1=set()
print(set1)
set1.add(1)
print(set1)
set1.add(2)
print(set1)
set1.add(2)
print(set1)
lst=[1,1,1,1,2,2,2,2,3,3,3,3]
print(lst)
print(set(lst))


