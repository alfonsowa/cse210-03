class Player:
    """The controling status player (actor)
    
    The responsibility of counting live, attempts and
    correct or wrong guesses
    
    Attributes:
        lives: Times of lives to choice a letter.
        attempts: counter of answers.
        correct_counter: correct counter answers.
        guesses: list.
        """

    def __init__(self):
        """Constructs a new Player
        
        Args:
            self(Payer): An instance of a Player"""

        self.lives = 5
        self.attempts = 0
        self.correct_counter = 0
        self.guesses = []

    def wrong_attempt(self):
        """ Counter Acumulate number of attempts or lives.
        Args:
            self(Player): An instance of a Player
        
        """


        self.lives -= 1
        self.attempts += 1
    
    def get_lives(self):
        """ lives track method
        Args:
            self(Player): An instance of a Player
        
        Returns:
            Int: lives counting """
        return self.lives