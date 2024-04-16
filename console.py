#!/usr/bin/python3
"""
This module defines the HBNBCommand class, which extends the functionality of the cmd module
to create a command interpreter for managing the AirBnB clone objects
"""

import cmd
from datetime import datetime

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter that manages the AirBnB clone objects
    """

    prompt = "(hbnb) "  # Command prompt
    all_classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']  # List of valid classes

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        End of file command to exit the program
        """
        return True

    def help_quit(self):
        """
        Display the help for the quit command
        """
        print("Quit command to exit the program\n")

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

    def do_create(self, args):
        """
        Create a new instance of BaseModel, saves it (to the JSON file) and print the id
        """
        arguments_list = args.split()

        if len(arguments_list) == 0:
            print('** class name missing **')
            return

        try:
            dummy = eval(arguments_list[0] + '()')
            dummy.save()
            print(dummy.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Print the string representation of an instance based on the class name and id
        """

        arguments_list = args.split()

        if validate(arguments_list):
            instance_key = validate(arguments_list)
            all_instances = models.storage.all()

            if instance_key in all_instances.keys():
                reference = all_instances[instance_key]
                print(reference)

            else:
                print("** no instance found **")
                return

    def do_destroy(self, args):
        """
        Delete an instance based on the class name and id (save the change into the JSON file)
        """

        arguments_list = args.split()

        if validate(arguments_list):
            obj_reference = validate(arguments_list)
            all_instances = models.storage.all()

            if obj_reference in all_instances.keys():
                del all_instances[obj_reference]
                models.storage.save()

            else:
                print("** no instance found **")
                return

    def do_all(self, args):
        """
        Print all string representation of all instances based or not on the class name
        """

        instances = models.storage.all()

        if args:
            arg_list = args.split()

            if arg_list[0] not in self.all_classes:
                print("** class doesn't exist **")

            else:
                new_list = [str(instances[obj]) for obj in instances.keys()
                            if arg_list[0] in obj]
                print(new_list)

        else:
            new_list = [str(instances[obj]) for obj in instances.keys()]
            print(new_list)

    def do_update(self, args):
        """
        Update an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file)
        """

        arguments_list = args.split()

        if validate(arguments_list):
            instance_key = validate(arguments_list)
            all_instances = models.storage.all()

            if instance_key in all_instances.keys():
                obj = all_instances[instance_key]
                len_arg_list = len(arguments_list)

                if len_arg_list < 3:
                    print("** attribute name missing **")
                    return

                elif len_arg_list < 4:
                    print("** value missing **")
                    return

                else:
                    try:
                        value = int(arguments_list[3].replace('"', ""))

                    except ValueError:
                        try:
                            value = float(arguments_list[3].replace('"', ""))

                        except ValueError:
                            try:
                                value = str(arguments_list[3].replace('"', ""))

                            except:
                                pass

                    obj.__dict__[arguments_list[2]] = value
                    models.storage.save()
                    return

            else:
                print("** no instance found **")
                return


def validate(list_args):
    """
    Validate the arguments list for some commands and return the object reference if valid
    """
    if list:
        len_list = len(list_args)

        if len_list < 1:
            print("** class name missing **")
            return None

        if list_args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return None

        if len_list < 2:
            print("** instance id missing **")
            return None

        obj_reference = list_args[0] + '.' + list_args[1]
        return obj_reference


if __name__ == '__main__':
    HBNBCommand().cmdloop()
