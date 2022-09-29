#!/usr/bin/python3
"""Holberton AirBnB Project for Holberton (Console)"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class for Console Commands"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exits the command line at the end of file"""
        return True

    def emptyline(self):
        """Does nothing when empty line is entered as input"""
        pass

    def do_create(self, args):
        """Creates a new Object and prints the object ID"""
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return False
        if len(arg) > 1:
            print("** Too many Arguments **")
            return False
        if arg[0] !=  "BaseModel":
            print("** class name missing **")
            return False
        new_object = eval(str(args) + '()')
        new_object.save()
        print(new_object.id)

    def do_show(self, args):
        """Shows the attributes of object with a given ID """
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return False
        if arg[0] !=  "BaseModel":
            print("** class name missing **")
            return False
        if len(arg) < 2:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            print("Too many Arguments")
            return False
        """
        Add show method code here
        """

    def do_destroy(self, args):
        """Destroys an Instance of an Object"""
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return False
        if arg[0] !=  "BaseModel":
            print("** class name missing **")
            return False
        if len(arg) < 2:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            print("Too many Arguments")
            return False
        """
        Add destroy method Code here
        """

    def do_all(self, args):
        """Prints string representation of all instances of an Object"""
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return False
        if arg[0] !=  "BaseModel":
            print("** class name missing **")
            return False
        if len(arg) < 2:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            print("Too many Arguments")
            return False
        """
        Add all method code here"""

    def do_update(self, args):
        """Updates the Attribute of an Object Instance with given ID"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] !=  "BaseModel":
            print("** class name missing **")
            return False
        if len(arg) < 2:
            print("** instance id missing **")
            return False
        if len(arg) < 3:
            print("** attribute name missing **")
            return False
        if len(arg) < 4:
            print("** value missing **")
            return False
        if len(arg) > 4:
            print("Too many Arguments")
            return False
        """
        Add update method code here
        """
if __name__ == '__main__':
    HBNBCommand().cmdloop()
