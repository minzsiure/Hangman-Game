# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_list = list (secret_word) 
    i = 0
    while i < len(secret_list):
        if secret_list[i] in letters_guessed:
            del(secret_list[i])
            if len(secret_list) == 0:
                return True
        else:
            return False
        
    
# secret_word = "apple"
# letters_guessed = ['a','p','l'] 
# print(is_word_guessed(secret_word,letters_guessed))     



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_list = list (secret_word)
    underscore = '_'
    output = list(underscore * len(secret_list))

    i = 0
    for i in range (len(secret_list)):
        if secret_list[i] in letters_guessed:
            temp = secret_list[i] 
            output[i] = temp
            
        else:
            # return output
            pass

    return output
    
# secret_word = "apple"
# letters_guessed = ['p','l'] 
# print(get_guessed_word(secret_word, letters_guessed))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alpha = list(string.ascii_lowercase)
    i = 0
    for i in range (len(letters_guessed)):
        if letters_guessed[i] in alpha:
            del (alpha[i])
        else:
            pass
    return "Available options are: " + str(alpha)
    
# print(get_available_letters(letters_guessed))
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print ("Welcome to the game Hangman!") #welcome
    secret_word = choose_word(wordlist) #randomly generated a word
    secret_list = list (secret_word)
    letters_guessed = [] #your guess
   
    # print (secret_word)
    
    print ("I am thinking of a word that is",len(secret_word),"letters long." )
    print("--------------------")
    
    guess = 6 #your guess number
    print ("You have", guess, "guess(es) left.")
    print (get_available_letters(letters_guessed))
 

    while is_word_guessed(secret_word, letters_guessed) != True:
        response = input("Please guess a letter: ")
        letters_guessed.append(response)

        if response in secret_list and guess > 0:
            
        
            print("Good guess: " + str(get_guessed_word(secret_word, letters_guessed)))
            print("--------------------")
            print("You have", guess, "guess(es) left.")
            print (get_available_letters(letters_guessed))

        else:
            guess -= 1
            if guess > 0:
                print("Opps! That letter is not in my word: " + str(get_guessed_word(secret_word, letters_guessed)))
                print("--------------------")
                print("You have", guess, "guess(es) left.")
                print (get_available_letters(letters_guessed))
            
            else:
                return print ("Sorry, you ran out of guess. The word was", secret_word)
    
    return print("Congratulations, you won!")
    # pass   
        
        
# secret_word = "apple"
# letters_guessed = ['a','p','l'] 
# print(get_guessed_word(secret_word, letters_guessed))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    len_my = len(my_word)
    len_other = len(other_word)
    
    list_my = list(my_word)
    list_other = list(other_word)
    
    if len_my == len_other:
     i = 0
     temp1 = 0
     temp2 = 0
     for i in range (len_other):
         if list_my[i] == '_':
             temp1 += 1
         else:
            temp1 += 0
    
     for i in range (len_other):
         if list_my[i] != '_' and list_my[i] == list_other[i]:
             temp2 += 1
         else:
             temp2 += 0
     
     temp3 = temp1 + temp2   
     if temp3 == len_other:
         return True
     else:
         return False
     
    else:
        return False
    

# my_word = 'app__'
# other_word = 'bpple'
# print(match_with_gaps(my_word, other_word))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
  
    words = []
    i = 0
    for i in range (len(wordlist)):
        other_word = wordlist[i]
        if match_with_gaps(my_word, other_word) == True:
            words.append(other_word)
        else:
            pass
    
    if len(words) > 1:
        return words
    
    else:
        return "None or only one match found."

# my_word = 'b______'
# print(show_possible_matches(my_word))
        



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    print ("Welcome to the game Hangman with hints!") #welcome
    print ("You can enter '*' to get hints. I'll generate match words for you.")
    secret_word = choose_word(wordlist) #randomly generated a word
    secret_list = list (secret_word)
    letters_guessed = [] #your guess
   
    # print (secret_word)
    
    print ("I am thinking of a word that is",len(secret_word),"letters long." )
    print("--------------------")
    
    guess = 6 #your guess number
    print ("You have", guess, "guess(es) left.")
    print (get_available_letters(letters_guessed))
 

    while is_word_guessed(secret_word, letters_guessed) != True:
        response = input("Please guess a letter: ").lower()
        letters_guessed.append(response)
        
        if response not in string.ascii_lowercase and response != '*':
            print("Invalid enter. Please re-enter.")

        if response in secret_list and guess > 0:
            
        
            print("Good guess: " + str(get_guessed_word(secret_word, letters_guessed)))
            print("--------------------")
            print("You have", guess, "guess(es) left.")
            print (get_available_letters(letters_guessed))

        elif response not in secret_list and guess > 0 and response != '*' and response in string.ascii_lowercase:
            guess -= 1
            if guess > 0:
                print("Opps! That letter is not in my word: " + str(get_guessed_word(secret_word, letters_guessed)))
                print("--------------------")
                print("You have", guess, "guess(es) left.")
                print (get_available_letters(letters_guessed))
            
            else:
                return print ("Sorry, you ran out of guess. The word was", secret_word)
            
        elif response == '*':
            print ("Possible word matches are: ")
            print (show_possible_matches(secret_word))
            print ("--------------------")
            
    return print("Congratulations, you won!")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
