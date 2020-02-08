import random

"""
Start the program and load the file.
"""
def main():
    print("Welcome to the word generator!")
    dictionary = load_dictionary()
    user_loop(dictionary)


"""
Prompt the user to choose an action and call the appropriate function.

:param dictionary: a list of words
"""
def user_loop(dictionary):
    action = int(input("\nWhat would you like to do?\n" +
                       "1 - Generate word\n" +
                       "2 - Enter new words\n" +
                       "3 - Save and quit\n"))
    if action == 1:
        choose_words(dictionary)
    elif action == 2:
        dictionary = get_new_words(dictionary)
    elif action == 3:
        save_dictionary(dictionary)
        exit()
        
    user_loop(dictionary) #run this method again!
    
    
"""
Pick two different words from the dictionary and print them.

:param dictionary: a list of words
"""
def choose_words(dictionary):
    word1 = random.choice(dictionary)
    word2 = None
    while word2 == None or word2 == word1:
        word2 = random.choice(dictionary)
        
    print("\n",word1, word2)
    

"""
Prompt the user to enter new words and add them to the dictionary

:param dictionary: a list of words
:return: the same list of words with any that the user entered in addition
"""
def get_new_words(dictionary):
    print(dictionary)
    while True:
        word = input("\nEnter a word or type Done to return: ")
        if word.lower() == "done":
            break
        else:
            dictionary.append(word)
    
    return dictionary

"""
Read the file into a list and return it

:return: a list of words
"""
def load_dictionary():
    with open("dictionary.txt", "r") as file:
        dictionary = file.readlines()
        dictionary = [word.strip() for word in dictionary]
        return dictionary


"""
Parse the dictionary as a string and write it to the file

:param dictionary: a list of words
"""
def save_dictionary(dictionary):
    with open("dictionary_test.txt", "w") as file:
        file.write(str(dictionary))
        
"""
Convert a list into a string separated by new lines

:param lst: a list of strings
:return: a string containing the words in the list
"""
def list_to_string(lst):  
    string = "\n" 
    return (string.join(lst))

if __name__ == "__main__":
    main()