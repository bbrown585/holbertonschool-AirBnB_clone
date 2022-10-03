#!/usr/bin/python3
"""Holberton AirBnB Project for Holberton (Console)"""
import cmd
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class_keys = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
              "Place": Place, "Review": Review, "State": State, "User": User}


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
        elif len(arg) > 1:
            print("** Too many Arguments **")
            return False
        elif arg[0] not in class_keys:
            print("** class doesn't exist **")
            return False
        else:
            new_object = eval(str(args) + '()')
            new_object.save()
            print(new_object.id)

    def do_show(self, args):
        """Shows the attributes of object with a given ID """
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return False
        elif arg[0] not in class_keys:
            print("** class doesn't exist **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False
        elif len(arg) > 2:
            print("Too many Arguments")
            return False
        else:
            key = arg[0] + "." + arg[1]
            storage = models.storage.all()
            if key in storage:
                print(storage[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Destroys an Instance of an Object"""
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return False
        elif arg[0] not in class_keys:
            print("** class doesn't exist **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False
        elif len(arg) > 2:
            print("Too many Arguments")
            return False
        else:
            key = arg[0] + "." + arg[1]
            storage = models.storage.all()
            if key in storage:
                del(storage[key])
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints string representation of all instances of an Object"""
        arg = args.split()
        if len(arg) > 1:
            print("Too many Arguments")
            return False
        else:
            new_list = []
            storage = models.storage.all()
            if len(args) == 0:
                for key in storage:
                    new_list.append(str(storage[key]))
                print(new_list)
            else:
                if arg[0] not in class_keys:
                    print("** class doesn't exist **")
                    return False
                if arg[0] in class_keys:
                    for key in storage:
                        if arg[0] in key:
                            new_list.append(str(storage[key]))
                    print(new_list)

    def do_update(self, args):
        """Updates the Attribute of an Object Instance with given ID"""
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return False
        elif arg[0] not in class_keys:
            print("** class doesn't exist **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False
        elif len(arg) < 3:
            print("** attribute name missing **")
            return False
        elif len(arg) < 4:
            print("** value missing **")
            return False
        elif len(arg) > 4:
            print("Too many Arguments")
            return False
        else:
            key = arg[0] + "." + arg[1]
            storage = models.storage.all()
            if key in storage:
                    setattr(storage[key], arg[2], arg[3])
                    models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
