# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    #print( "  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
print("Welcome to Ghost!")


def valid(word, list_of_words):
  word = word.lower()
  if word in list_of_words and len(word) == 3 :
    return True
  else:
    return False

def play_game(list_of_words):
  word = ''
  print ("Player 1 goes first")
  print ("Current word fragment: ", word)
  player_1 = str(input("Player 1 says letter: "))
  word = word + player_1

  print ("Current word fragment: ", word)

  print ("Player2's turn. ")
  player_2 = str(input("Player 2 says letter: "))
  word = word + player_2

  print ("Player 1's turn")
  player_1 = str(input("Player 1 says letter "))
  word = word + player_1
  print ("Current word fragment: ", word)

  if valid(word,wordlist):
    print ("Player 1 wins!")
  else:
    print ("Player 2 wins!")
  play_another_round(wordlist)

def play_another_round(word_list):
  new_game = str(input("Enter n for another round or e to end: "))
  if new_game == "n" or "N":
    play_game(wordlist)
  elif new_game == 'y' or new_game == 'Y':
    print("Thank you for playing")
  else:
    print ("Invalid command")
  



if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
  
  
  



