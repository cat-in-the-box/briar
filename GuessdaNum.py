import random

def Main():
    num = random.randint(1, 100)
    guess = getandevaluateguess("Guess the number! ", num)
    
    while (not num == guess):
        getandevaluateguess("Try again ", num)
    
    end = int(input("You guessed the number! Do you want to: \n1. Guess another number \n2. Exit "))
    if end == 1:
        main()
    
    elif (end==2):
        
        
        exit()       
def getandevaluateguess(message, number):
    amount = 0
    while (amount <= 1):
        amount =input("Please guess a number. ")
        amount = int(amount)
        
    if (number > amount):
        print("Guess is too low")
    
    elif (amount < number):
        print("Guess is too high")
        
    return amount

###
main()