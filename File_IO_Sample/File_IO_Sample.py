import random

def main():
    print("Welcome to the word generator!")
    dictionary = load_dictionary()
    user_loop(dictionary)

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
    

def choose_words(dictionary):
    word1 = random.choice(dictionary)
    word2 = None
    while word2 == None or word2 == word1:
        word2 = random.choice(dictionary)
        
    print("\n",word1, word2)
    

def get_new_words(dictionary):
    while True:
        word = input("\nEnter a word or type Done to return: ")
        if word.lower() == "done":
            break
        else:
            dictionary.append(word)
        
    return dictionary

def load_dictionary():
    with open('dictionary.txt', 'r') as file:
        dictionary = list(file.readlines())
        dictionary = [word.strip() for word in dictionary] 
        return dictionary

def save_dictionary(dictionary):
    string_dictionary = list_to_string(dictionary)
    
    with open('dictionary.txt', 'w') as file:
        file.write(string_dictionary)
        
# Function to convert   
def list_to_string(lst):  
    string = "\n" 
    return (string.join(lst))

if __name__ == "__main__":
    main()