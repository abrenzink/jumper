from game.puzzle_word import PuzzleWord
from game.jumper import Jumper
from game.terminal_service import TerminalService


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word (PuzzleWord): The object responsible for any service related to the word.
        jumper (Jumper): The game's jumper.
        terminal_service: For getting and displaying information on the terminal.
        is_playing (boolean): Whether or not to keep playing.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self._word = PuzzleWord()
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        self._is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        self._word.random_word()
        self._terminal_service.write_text("\n------------------------------------------------------------------\n"
                                            "\nWelcome to the jumper game! Help the jumper to stay safe. \n"
                                            "A word was randomly chosen. Guess a letter and good luck! \n"
                                            "\n------------------------------------------------------------------\n")

        self._terminal_service.write_text(self._word.get_word_display())
        self._terminal_service.draw(self._jumper.get_parachute())

        while(self._is_playing):

            if self._word.correct_word_hint() or not self._jumper.reach_wrong_hints():
                self._is_playing = False

            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        if not self._jumper.reach_wrong_hints():
            self._terminal_service.write_text("\n------------------------------------------------------------------\n"
                                                "\nSorry, the game is over. See you next time! \n"
                                                "\n------------------------------------------------------------------\n")
        else:
            self._terminal_service.write_text("\n------------------------------------------------------------------\n"
                                                f"\nCongratulations! The word is *{self._word.get_secret_word()}*. Our jumper is safer now :)\n"
                                                "\n------------------------------------------------------------------\n")
    
    def _get_inputs(self):
        """Reads the player guess and say if it can be found in the secret word.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._terminal_service.read_text("\nEnter a letter [a-z]: ")
        self._word.last_hint_correct(letter)

    def _do_updates(self):
        """Cuts new part of the parachute if the last guess was wrong, or revels
        the letter correctly guessed.

        Args:
            self (Director): An instance of Director.
        """
        if (not self._word.get_last_hint()):
            self._jumper.update_parachute()

        if self._word.correct_word_hint() or not self._jumper.reach_wrong_hints():
            self._is_playing = False

    def _do_outputs(self):
        """Displays guessed letter in the word and the jumper's parachute.
            Informs if it was a good guess.

        Args:
            self (Director): An instance of Director.
        """
        
        self._terminal_service.write_text(self._word.get_word_display())
        self._terminal_service.draw(self._jumper.get_parachute())

        if(self._word.get_last_hint()):
            self._terminal_service.write_text("\nYeey! Right guess!")
        else:
            self._terminal_service.write_text("\nOh, no, wrong guess! You lost part of the parachute :(")