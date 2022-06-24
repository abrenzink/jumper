import random

class PuzzleWord:
    """The person managing services related to the secret word. 
    
    The responsibility of a PuzzleWord is to randomly chose a secret word and inform if the letter
    guessed is found in the secrete word. Also alerts once the secret word is guessed.
    
    Attributes:
        _secret_word (List[int]): The randomly chosen word.
        _word_display (List[int]): The display of the guessed letters.
        _last_hint (boolean): Informs if the last hint was successful of not.
    """
    def __init__(self):
        """Constructs a new PuzzleWord.

        Args:
            self (PuzzleWord): An instance of PuzzleWord.
        """
        self._secret_word = []
        self._word_display = []
        self._last_hint = True

    def random_word(self):
        """Randomly choses a word from the WORDS list and separates it in letters.
         Prepares the display to give orientation to the player.
        
        Args:
            self (PuzzleWord): An instance of PuzzleWord.
        """
        WORDS = ["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
        self._secret_word = list(random.choice(WORDS))
        
        for i in range(len(self._secret_word)):
            self._word_display.append(" _ ")
    
    def last_hint_correct(self, letter):
        """Compares the secret word letter with the guessed letter. If the guessed letter
            is found, last hint was true. Otherwise, it was false.
        
        Args:
            self (PuzzleWord): An instance of PuzzleWord.
        """
        count = self._secret_word.count(letter)

        if (count == 0):
            self._last_hint = False
        else:
            self._last_hint = True
            self._update_word_display(letter)

    def _update_word_display(self, letter):
        """Reveals the position of the letter.
        
        Args:
            self (PuzzleWord): An instance of PuzzleWord.
            letter (string): The last guessed letter.
        """
        for i in range(len(self._secret_word)):
            if self._secret_word[i] == letter:
                self._word_display[i] = letter

    def get_word_display(self):
        """Gets the word to be displayed to the player, with the revealed letters.
        
        Args:
            self (Seeker): An instance of Seeker.

        Returns:
            string: The word display.
        """
        return " ".join(self._word_display)

    def get_secret_word(self):
        """Gets the secret word.
        
        Args:
            self (Seeker): An instance of Seeker.
            
        Returns:
            string: The secret word joined.
        """
        return "".join(self._secret_word)

    def get_last_hint(self):
        """Gets the last hint.
        
        Args:
            self (Seeker): An instance of Seeker.
            
        Returns:
            boolean: If the last hint was successful.
        """
        return self._last_hint

    def correct_word_hint(self):
        """Compares the displayed word and the secret word to inform if the game is over.
        
        Args:
            self (Seeker): An instance of Seeker.
            
        Returns:
            boolean: The secret word equals to the displayed word.
        """
        secret = "".join(self._secret_word)
        word = "".join(self._word_display)

        return secret == word
