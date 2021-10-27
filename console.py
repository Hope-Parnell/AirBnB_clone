#!/usr/bin/python3
"""Module for the console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for the command console"""
    prompt = '(hbnb)'
    def emptyline(self):
        pass

    def do_EOF(self, args):
        """Exits the console"""
        return True

    def do_quit(self, args):
        """Exits the Console"""
        print(args)
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
