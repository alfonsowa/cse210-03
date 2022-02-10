class Display:
    """ A service that handles terminal operations.
    
    The responsibility of display the letters and
    the parachute man drawing.

    Attributes:
    word: stored the word for the jumper game
    player: variable for stored sequence of player. 
    letters: list of letters.
    """

    def __init__(self, word, player):
        """Constructs a new Display.
        Args:
            self(Display): An instance of Display
        """
        self.word = word
        self.player = player
        self.letters = []

    def display_word(self):
        """condition to track and find the letter in the word
         otherwise print '_' .

         Args:
            self(Display): An instance of Display.
         """

        print(" ".join([letter if letter in self.letters else "_" for letter in self.word]))
        # Equivalent to:
        # for letter in self.word:
        #     if letter in self.letters:

        #         print(letter+ " ", end = "",flush = True)
        #     else:
        #         print("_ ", end = "", flush = True)
        # print()
     
    def display_person(self):
        """ conditions to track the lves and drawing the 
        parachute man updates
        
        Args:
            self(Display): An instance of Display.
        """
        print()
        if self.player.get_lives() > 4:
            
            print("  _===_  ")

        if self.player.get_lives() > 3:
            print(" //_ __\ ")

        if self.player.get_lives() > 2:
            print(" \\  |  / ")

        if self.player.get_lives() > 1:
            print("  \\ I / ")
            
        if self.player.get_lives() > 0:
            print("    O  ")

        if self.player.lives == 0:
            print("    X  ")

        print("   /|\ ")
        print("   / \ ")
        print("  *   *")
        print("\n^^^^^^^^^^^^^")    

    def foundLetter(self, letter):
        """Letter append to a new list with the secret word
        
        Args:
            self(Display): An instance of Display.
             """
        self.letters.append(letter)