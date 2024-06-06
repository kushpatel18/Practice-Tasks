# PROJECT 1: WORD ANALYSER INCLUDING COUNTING NO. OF CHAR(S), CHECKING IF WORD IS PALINDROME
#           AND IDENTIFYING THE NO. OF VOWELS AND CONSONANTS IN WORD

def Word_Analyser():
    string = input("Enter any String: ")
    string2=string[::-1]

    if(string.lower()==string2.lower()):
        print(string, " is palindrome")
    else:
        print(string," is not palindrome")

    char=len(string)
    print("No. of characters:",char)
    vowels=0
    consonants=0



    for i in string:
        if(i =='a' or i=='e' or i=='i' or i=='o' or i=='u' ):
            vowels+=1
        elif(i==" "):
            continue
        else:
            consonants+=1

    print("No. of vowels:",vowels)
    print("No. of consonants:", consonants)

Word_Analyser()