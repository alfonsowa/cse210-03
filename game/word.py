import random

class Word:
    """ Extract the random word from the txt. file.
    
    The responsibility of the Word is to open the word_list.txt
    and choice and return the random word to a self.worlist
     """

    def __init__(self):
        """ Constructs a new Word
        
        Args:
            self (Word): An instance of Word 
        """

        with open("./game/word_list.txt", "r") as my_file:
            self.wordlist = my_file.readlines()

    def get_word(self):
        """ Gets a word for the game
        
        Args:
            self(Word): An instance of Word
            
        Returns:
            Random and choice the  word from the txt.file.    
         """
        return random.choice(self.wordlist).lower()
