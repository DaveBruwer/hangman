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
	num_of_letters = 0
	letter_found = False
	
	for char1 in secret_word:
		for char2 in letters_guessed:
			if char1 == char2:
				letter_found = True
		if letter_found == True:
			num_of_letters += 1
		letter_found = False
	return num_of_letters == len(secret_word)

def is_guess_right(secret_word, guessed_letter):
	'''
	secret_word: string, the word the user is guessing; assumes all letters are
	lowercase
	guessed_letter: string, the last letter that was guessed.
	returns: boolean, True if the guessed letter is in the word;
	False otherwise
	'''
	letter_found = False
	
	for char1 in secret_word:
		if char1 == guessed_letter:
			letter_found = True
	return letter_found

def get_guessed_word(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string, comprised of letters, underscores (_), and spaces that represents
	  which letters in secret_word have been guessed so far.
	'''
	num_of_letters = 0
	letter_found = False
	return_string = ""
	
	for char1 in secret_word:
		for char2 in letters_guessed:
			if char1 == char2:
				letter_found = True
		if letter_found == True:
			return_string += char1
		else:
			return_string += "_ "
		letter_found = False
	return return_string

def get_available_letters(letters_guessed):
	'''
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string (of letters), comprised of letters that represents which letters have not
	  yet been guessed.
	'''
	english_alphabet = "abcdefghijklmnopqrstuvwxyz"
	letter_found = False
	return_string = ""
	
	for char1 in english_alphabet:
		for char2 in letters_guessed:
			if char1 == char2:
				letter_found = True
		if letter_found == False:
			return_string += char1
		letter_found = False
	return return_string

def is_guess_valid(guessed_letter, available_letters):
	'''
	guessed_letter: string, the last letter that was guessed.
	available_letters:string, the letters in the alphabet that has not been guessed yet.
	returns: boolean, True if the guessed letter is in the standard english alphabet, and not yet guessed before;
	False otherwise
	'''
	valid_guess = False
	for char in available_letters:
		if guessed_letter == char:
			valid_guess = True
	return valid_guess
	
	
	

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
	
	guesses_left = 6
	available_letters = "abcdefghijklmnopqrstuvwxyz"
	guessed_letters = list((""))
	secret_word = secret_word.lower()
	warnings_left = 3
	
	print("Welcome to the game Hangman!")
	print("I am thinking of a word with", len(secret_word), "letters.")
	print("You get 3 warnings, and 6 guesses")
	print("You have 3 warnings left")
	
	while True:
		print("----------------")
		print("You have", guesses_left, "guesses left.")
		print("Available letters:", get_available_letters(guessed_letters))
		guess = input("Please guess a letter from the avalable letters:")
		guess = guess.lower()
		guessed_letters.append(guess)
		if is_guess_valid(guess, available_letters):
			if is_guess_right(secret_word, guess):
				print("Good guess:", get_guessed_word(secret_word,guessed_letters))
			else:
				print("Oops! That letter is not in my word:", get_guessed_word(secret_word,guessed_letters))
				guesses_left -= 1
			available_letters = get_available_letters(guessed_letters)
		elif warnings_left > 0:
			warnings_left -= 1
			print("Warning! That is not a valid letter. You have", warnings_left, "warnings left.")
		else:
			print("Sorry, that was your last warning!")
			print("The word was:", secret_word)
			break
		if is_word_guessed(secret_word, guessed_letters):
			print("Congratulations! You Win!")
			input("Press Enter to exit.")
			break
		elif guesses_left == 0:
			print("Sorry! You are out of guesses.")
			print("The word was:", secret_word)
#			input("Press Enter to exit.")
			break




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
	pass



def show_possible_matches(my_word):
	'''
	my_word: string with _ characters, current guess of secret word
	returns: nothing, but should print out every word in wordlist that matches my_word
			 Keep in mind that in hangman when a letter is guessed, all the positions
			 at which that letter occurs in the secret word are revealed.
			 Therefore, the hidden letter(_ ) cannot be one of the letters in the word
			 that has already been revealed.

	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	pass



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
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
	# pass

	# To test part 2, comment out the pass line above and
	# uncomment the following two lines.
	
	secret_word = choose_word(wordlist)
	hangman(secret_word)

###############
	
	# To test part 3 re-comment out the above lines and 
	# uncomment the following two lines. 
	
	#secret_word = choose_word(wordlist)
	#hangman_with_hints(secret_word)
