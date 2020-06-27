#!/usr/bin/python3
"""
Creating command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Uses cmd methods to control command interpreter """
    # (hbnb) is our custom prompt
    prompt = '(hbnb) '

    # Ensure it works in both interactive and non-interactive mode
    # FIGURE OUT EXACTLY WHY THIS NEEDS TO BE THIS WAY
    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        # FIGURE THIS OUT
        if sys.stdout.isatty():
            print('')
        return True

    def emptyline(self):
        """ Does nothing, re-prompts """
        pass

    def do_create(self, cls_name=None):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file)
        and prints the id.
            Ex: $ create BaseModel
        """

        if self.not_a_class(cls_name):
            return

        # Create instance of class
        obj = cls_name()

        # Save to JSON File
        obj.save()

        # Print the ID
        print(obj.id)

    def do_show(self, cls_name=None, id=None):
        """
        Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        if self.not_a_class(cls_name) or self.not_an_instance(id):
            return
        # cls_name.id.__str__()

    def do_destroy(self, cls_name=None, id=None):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if self.not_a_class(cls_name) or self.not_an_instance(id):
            return
        # Use storage.something to delete
        # Make sure you "save changes" to JSON file

    def do_all(self, cls_name=None):
        """
        Prints all string representation of all instances based on the class name or not.
        Ex: $ all BaseModel or $ all.
        """
        if cls_name is None:
            pass
            # catch and print all - loop through all, printing __str__
        if not_a_class(cls_name):
            return
        # loop through all in class name, printing __str__

    @staticmethod
    def not_a_class(cls_name):
        if cls_name is None:
            print("** class name missing **")
            return True
        known_classes = ["BaseModel", "User", "State",
                         "City", "Place", "Amenity", "Review"]
        if cls_name not in known_classes:
            print("** class doesn't exist **")
            return True

        return False

    @staticmethod
    def not_an_instance(id):
        if id is None:
            print("** instance id missing **")
            return True
        # if instance doesn't exist:
            # print("** no instance found **")
            # return True
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
