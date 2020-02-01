'''
Calculator gets two numbers from the user, and then according to user preference adds
or averages them.
'''

# addition takes the two user-input numbers, adds them together, and return the sum
#
# :param number_a: the first integer entered by the user
# :param number_b: the second integer entered by the user
# :return: the sum of number_a and number_b
def addition(number_a, number_b):
    added_value = number_a + number_b
    return added_value

# average takes the two user-input numbers, finds the average, and gives it back.
# average calls the addition function
#
# :param number_a: the first number entered by the user
# :param number_b: the second number entered by the user
# :return: the average of number_a and number_b
def average(number_a, number_b):
    averaged_value = addition(number_a, number_b) / 2
    return averaged_value

# queries prompts the user to give two numbers and asks which operation they would like
def question():
    first_number = int(input("Enter a number "))
    second_number = int(input("Enter another number "))
    
    operation = input("which would you like to do? Add or average? ").lower()
    
    if operation == "add":
        answer = addition(first_number, second_number)
    elif operation == "average":
        answer = average(first_number, second_number)
    else:
        print ("I don't understand!")
        
    print(answer)


if __name__ == '__main__':
    question()
