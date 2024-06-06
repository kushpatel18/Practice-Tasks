#Q1]  Print *s in a row

def Row_Pattern():
    num=int(input("Enter the no. of asterisks: "))

    #For Loop
    for i in range(0,num):
        print("*",end=" ")

    #While Loop
    # i=0
    # while i<num:
    #     print("*",end=" ")
    #     i+=1

# Row_Pattern()


#Q2] Print a square pattern of asterisks

def SquarePattern():
    side=int(input("Enter the side of the square: "))
    for i in range(0,side):
        for j in range(0,side):
            print("*",end=" ")
        print(" ")


SquarePattern()

#Q3] Print a square pattern of digit

def Sqaure_DigitPattern():
    num=int(input("Enter the digit: "))
    for i in range(0,num):
        for j in  range(0,num):
            print(num,end=" ")
        print(" ")

# Sqaure_DigitPattern()

#Q4] Number Guessing Game

def Number_Guess():
    target_val=33
    attempts=0
    flag=1

    print("\n\nWelcome to the Number Guessing Game!")
    print("\n\nGuess a number between 1 to 100")

    while (flag==1):

        guess=int(input("Enter your guess: "))
        attempts+=1

        if guess<target_val:
            print("Guess a higher number")
        elif guess>target_val:
            print("Guess a lower number")
        else:
            print(f"Congratulations! You guessed the correct number {target_val} in {attempts} attempts ")
            flag==0
            break

# Number_Guess()



