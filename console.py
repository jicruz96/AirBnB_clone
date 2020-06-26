#!/usr/bin/python3
"""
Creating command interpreter
"""
if __name__ == "__main__":
    import cmd

    class HBNBCommand(cmd.Cmd):
        """ Uses cmd methods to control command interpreter """
        # (hbnb) is our custom prompt
        # Ensure it works in both interactive and non-interactive mode

        # ensure this class uses 'quit' and 'EOF' to exit
        # ensure this class uses 'help'
        # ensure empty lines + ENTER don't do anything fishy

        def quit():
            """ Quit command to exit the program """

        def EOF():
            """ EOF command to exit the program """

        def help():
            """ HEEEELPP !!! """
