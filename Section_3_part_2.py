# Indexing and Slicing of Strings
mystring = "hello world"
print(mystring[0])
print(mystring[8])
print(mystring[9])
print(mystring[-1])
print(mystring[-11])
print(mystring[-3])
print("last character always:",mystring[-1])
print(mystring[2:])
print(mystring[:3])
print(mystring[3:6])
print(mystring[1:3])
print(mystring[::])
print(mystring[::2])
print(mystring[2:7:2])
print("Reverse String:",mystring[::-1])

#                                   String Properties and Methods
#                       Immutability
name="Kush"
# name[0]="P"
# print(name) ---> Error, we cannot change the value at any index of string


last_letters=name[1:]
print(last_letters)

# String Concatenation
print("P"+last_letters)
x= "Hello world"
print(x)
x= x+" it is beautiful outside"
print(x)

# String Replication
letter ='z'
print(letter*10)

print(2+3)
print('2'+'3')

#                       Methods
x="Hello world"
print(x.upper())
print(x.lower())
print(x.split())
print(x.split('l'))


#                      Print Formatting with Strings
#                    .format() method
print("There is a {} string ".format("INSERTED"))
print("Not {} {} {}".format("now","then","when"))
print("Not {0} {2} {1}".format("now","then","when"))
print("Not {n} {w} {t}".format(n="now",t="then",w="when"))

# FLOAT FORMATTING {value:width.precision f} , width -> white spaces
result = 100/777
print(result)
print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))
print("The result was {r:10.3f}".format(r=result))

#             fstrings
name="Kush"
print(f"Hello, my name is {name}")
age=19
print(f"{name} is {age} years old")