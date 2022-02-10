from game.word import Word
from game.player import Player
from game.display import Display

class Game:

    """ The Game Class is the director from the jumper Game,
    
     From here we will control the sequence from the game
     
     Atributes:
     
     still_playing (boolean): Whether or not to keep playing.
     player: Identify player.
     word: choice the word on a TXT file.
     secret_word: will put and hide the letters during the game.
     display: will display the letter and  lives from the parachute man drawing.
     """
    def __init__(self):
        """Construct a new jumper game.
     
        Args:
          self (game): an instance of game
        """

        self.still_playing: bool
        self.player = Player()
        self.word = Word()
        self.secret_word = self.word.get_word()
        self.display = Display(self.secret_word, self.player)

    def main(self):
        """Start the game , game loop
        
        Args:
             Self (game): an instance of game. """

        self.still_playing = True
        while self.player.lives > 0 and self.still_playing == True:
            guess = input("Guess a letter [A-Z] or type quit to quit: ")
            guess = guess.lower()
            if guess in ["quit", "exit"]:
                self.still_playing = False
                continue
            elif len(guess) != 1:
                print("Please only input one letter")
                continue

            print("You guessed: ", guess)
            if guess in self.secret_word:
                self.display.foundLetter(guess)
                print("You found a letter!")
            else:
              self.player.wrong_attempt()

            if set(self.display.letters) == set(self.secret_word):
                print("You won!")
                self.still_playing = False

            self.display.display_word()
            self.display.display_person()
        else:
            print("Game Over")
            print("The secret word is ", self.secret_word)
            


if __name__ == "__main__":
    game = Game()
    game.main()
