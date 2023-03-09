#!/usr/bin/python3
"""Defines the console of the program"""

import cmd

class HBNBCommand(cmd.Cmd):
    """The class HBNB that builds a console"""

    prompt = "(hbnb)"

   # def do_create(self):

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, line):
        """Handle EOF"""

        return True

    def emptyline(self):
        """creates an empty line"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
