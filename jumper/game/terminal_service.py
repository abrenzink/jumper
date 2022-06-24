class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    def read_text(self, prompt):
        """Gets text input from the terminal and turn it to lowercase.
             Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
      
        return input(prompt).lower()
        
    def write_text(self, text, list=[]):
        """Displays the given text or list on the terminal or turns a list into a string
            before displaying it. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
            list (List[string]): The list to be joined and displayed.
        """
        if (len(list) > 0):
            print("".join(list))
        else:
            print(text)

    def draw(self, list):
        """Displays one item of a list at a time. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            list (List[string]): The list to have its items displayed one at a time.
        """
      
        for sprite in list:
            print(sprite)