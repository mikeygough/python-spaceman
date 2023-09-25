import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    
    is_guessed = True
    
    for letter in secret_word: # loop through secret_word letters
        if letter in letters_guessed:
            pass
        else: # if letter not in guesses, update is_guessed and break
            is_guessed = False
            break
    
    return is_guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    
    letters_and_underscores = ''

    for letter in secret_word:
        if letter in letters_guessed:
            letters_and_underscores += letter
        else:
            letters_and_underscores += '_'

    return letters_and_underscores

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    if guess in secret_word:
        return True
    else:
        return False

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    
    #TODO: show the player information about the game according to the project spec
    print('Welcome to Spaceman!')
    print(f'The secret word contains: {len(secret_word)} letters')
    
    # initialize game
    letters_guessed = []
    alphabet = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y',
                'z']
    strikes = 0
    playing = True
    
    while playing:
        
        #TODO: check if the game has been won
        if is_word_guessed(secret_word, letters_guessed):
            print('\nYou won!')
            break
        
        # check if the game has been won
        if strikes == 7:
            print('\nYou lose!')
            print(f'The secret word was {secret_word}')
            break
        
        # output strikes
        print(f'\nStrike Count: {strikes}')
        
        # calculating remaining letters.
        remaining_letters = [letter for letter in alphabet if letter not in letters_guessed]
        remaining_letters_output = 'Available Letters: '
        for letter in remaining_letters:
            remaining_letters_output += letter
        print(remaining_letters_output)
        
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = input('Guess a letter > ').lower()
        
        # check for valid guess
        while len(guess) != 1 or not guess.isalpha():
            print('Not a valid guess. Please guess a single letter.')
            guess = input('Guess a letter > ').lower()
            
        while guess in letters_guessed:
            print(f'You already guessed "{guess}"! Please guess again.')
            guess = input('Guess a letter > ').lower()
        
        letters_guessed.append(guess)

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print('Your guess appears in the word!')
        else:
            print('Sorry your guess does not appear in the word. Please try again!')
            strikes += 1

        #TODO: show the guessed word so far
        print(f'Guessed word so far: {get_guessed_word(secret_word, letters_guessed)}')

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)