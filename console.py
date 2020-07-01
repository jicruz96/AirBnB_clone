#!/usr/bin/python3
"""
Creating command interpreter
"""
import cmd
import sys
from models.engine.known_objects import classes
from models import storage


# Ensure it works in both interactive and non-interactive mode
class HBNBCommand(cmd.Cmd):
    """ Uses cmd methods to control command interpreter """
    # custom prompt:
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        if sys.stdin.isatty() is False:
            print("")
        return True

    def emptyline(self):
        """ Does nothing, re-prompts """
        pass

    def do_create(self, arguments):
        """
        Creates a new instance of a class
        saves it (to the JSON file)
        and prints the id.
            Ex: $ create BaseModel
        """
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        cls = classes[args["cls_name"]]
        new_obj = cls()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arguments):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        print(__objects[key])

    def do_destroy(self, arguments):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        del __objects[key]
        storage.save()

    def do_all(self, arguments):
        """
        Prints all string representation of all instances
        based on the class name or not.
        Ex: $ all BaseModel or $ all.
        """
        args = self.arg_string_parse(arguments)
        __objects = storage.all()
        print_list = []
        if args["cls_name"] is None:
            for obj in __objects:
                print_string = "{}".format(__objects[obj].__str__())
                print_list.append(print_string)
        else:
            if self.not_a_class(args["cls_name"]):
                return
            for obj in __objects:
                if obj.split(".")[0] == args["cls_name"]:
                    print_string = "{}".format(__objects[obj].__str__())
                    print_list.append(print_string)
        print(print_list)

    def do_update(self, arguments):
        """
        Updates an instance based on the class name and id
        adds or updates attribute and saves the change into the JSON file
        Ex: update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        if self.not_an_attribute(args["attr_name"]):
            return
        if self.not_a_value(args["attr_value"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        setattr(__objects[key], args["attr_name"], args["attr_value"])

    @staticmethod
    def arg_string_parse(arguments):
        """
        Splits input string of arguments
        arg order determines type of argument
        and arguments are space delimited

        Expected order:
        0. class name
        1. instance id
        2. attribute name
        3. attribute value
        """
        arg_list = arguments.split()
        args = {}
        if len(arg_list) >= 1:
            args["cls_name"] = arg_list[0]
        else:
            args["cls_name"] = None
        if len(arg_list) >= 2:
            args["inst_id"] = arg_list[1]
        else:
            args["inst_id"] = None
        if len(arg_list) >= 3:
            args["attr_name"] = arg_list[2]
        else:
            args["attr_name"] = None
        if len(arg_list) >= 4:
            args["attr_value"] = arg_list[3]
        else:
            args["attr_value"] = None
        return args

    @staticmethod
    def not_a_class(cls_name):
        """
        Checks if given valid class name argument
        Prints error message if missing or invalid
        """
        if cls_name is None:
            print("** class name missing **")
            return True
        if cls_name not in classes:
            print("** class doesn't exist **")
            return True
        return False

    @staticmethod
    def not_an_instance(cls_name, inst_id):
        """
        Checks if given valid instance id argument
        Prints error message if missing or invalid
        """
        if inst_id is None:
            print("** instance id missing **")
            return True
        key = "{}.{}".format(cls_name, inst_id)
        __objects = storage.all()
        if key not in __objects:
            print("** no instance found **")
            return True
        return False

    @staticmethod
    def not_an_attribute(attr_name):
        """
        Checks if given attribute name argument
        Prints error message if missing
        If exists, attr_name is assumed to be valid
            for this model
        """
        if attr_name is None:
            print("** attribute name missing **")
            return True
        return False

    @staticmethod
    def not_a_value(attr_value):
        """
        Checks if given attribute value argument
        Prints error message if missing
        If exists, attr_valid is assumed to be valid
            for this model, but may require type casting
        """
        if attr_value is None:
            print("** value missing **")
            return True
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
