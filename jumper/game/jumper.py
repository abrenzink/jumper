class Jumper:
    """The person wearing the parachute. 
    
    The responsibility of Jumper is to keep track of wrong hint and cut part of the parachute. 
    
    Attributes:
        _wrong_hints (int): Number of wrong guesses.
        _parachute (List[string]): Each part of the parachute.
    """
    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._parachute = [" ___ ","/___\\", "\   /"," \ / ","  0  "," /|\ "," / \ "]
        self._wrong_hints = 0

    def update_parachute(self):
        """Adds a wrong guess and removes part of the parachute.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._wrong_hints = self._wrong_hints + 1

        self._parachute[self._wrong_hints - 1] = "     "

    def get_parachute(self):
        """Gets the parts of the parachute.

        Args:
            self (Jumper): An instance of Jumper.
        
        Returns:
            List[string]: Parts of the parachute.
        """
        return self._parachute

    def reach_wrong_hints(self):
        """Says if the number of wrong hints is enought to kill the jumper.

        Args:
            self (Jumper): An instance of Jumper.
        
        Returns:
            boolean: False, informing the jumper still has a parachute.
        """
        return self._wrong_hints < 4