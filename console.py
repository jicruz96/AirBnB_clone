#!/usr/bin/python3
"""
Creating command interpreter
"""
import cmd
import sys
from models.engine.known_objects import classes, console_methods
from models import storage


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

    def default(self, line):
        """
        Default behavior for unknown commands.
        Verifies if input is in the format:
            * <class name>.<console method>

        Note:
            If input doesn't fit the format, or the class and method don't
            exist, an error message is printed to the user
        """

        try:
            # Parse through input. If parsing fails, send error message

            # YOU WILL RUN INTO ERRORS HERE WHILE TRYING TO CODE FOR UPDATE
            # Since update takes in very complex arguments, such as a
            # dictionary representation, my split('.') trick is likely
            # to make a jarbled, useless list.
            # Keep that in mind.

            # input is a list of strings
            input = line.split('.')
            # input[0] is class name
            cls_name = input[0]
            # method and args are the rest of the input list
            # THIS SPLIT WILL ALSO MESS YOU UP IN UPDATE. BEWARE
            method_and_args = input[1].split('(')
            # store method in method_str
            method_str = method_and_args[0]
            # store arg strings in args_list
            args_list = method_and_args[1:]
            # create empty args_str string
            args_str = ''
            # append arg_list strings to args_str
            for arg in args_list:
                args_str += arg
            # remove the ')' from the end of args_str
            args_str = args_str[:-1]
        except:
            # If something failed, then fuck it, just print an error
            print("** Unknown syntax: " + line)
            return

        # validate cls_name
        if cls_name not in classes:
            print("** class doesn't exist **")
            return

        # validate method
        if method_str not in console_methods:
            print("** unsupported method: " + method_str + " **")
            return

        # get static method
        method = getattr(self, method_str)

        # execute
        method(cls_name, args_str)

    @staticmethod
    def all(cls_name, args):
        """ console method that returns all saved objects of type cls_name """

        list_of_instances_of_cls_name = []

        for key, instance in storage.all().items():
            # If the first part of the key is the same as cls_name
            #   append the instance to list_of_instances_of_cls_name
            if key.split('.')[0] == cls_name:
                list_of_instances_of_cls_name.append(instance)

        # Print instances
        print('[', end='')
        number_of_instances = len(list_of_instances_of_cls_name)
        index = 0
        for instance in list_of_instances_of_cls_name:
            print(instance, end='')
            if index + 1 != number_of_instances:
                print(', ', end='')
            index += 1
        print(']')

    @staticmethod
    def update(cls_name, args):
        """ Updates cls_name """
        # LOGIC

    @staticmethod
    def show(cls_name, id):
        """
        Prints string representation of instance of cls_name with unique ID id
        """

        key = "{}.{}".format(cls_name, id)

        try:
            print(storage.all()[key])
        except:
            print("** no instance found **")

    @staticmethod
    def count(cls_name, args):
        """ Returns the number of instances of cls_name """

        count = 0

        for id, instance in storage.all().items():
            if id.split('.')[0] == cls_name:
                count += 1

        print(count)

    @staticmethod
    def destroy(cls_name, id):
        """
        Destroys instance of cls_name with unique ID id
        """

        key = "{}.{}".format(cls_name, id)

        try:
            del storage.all()[key]
            storage.save()
        except:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
