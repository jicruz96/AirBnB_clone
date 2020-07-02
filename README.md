# AirBnB_clone
The AirBnB clone utilizes higher level programming skills to deploy a copy of the AirBnB website.

## Console
The console is a command interpreter that manages all AirBnB objects.

### Using the Console
Run `./console.py`to begin a session. A prompt should appear as such:
```
(hbnb) 
```
Write `help` to get the list of available commands. 
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
Typing `help <command>` or `?<command>` will print information on how to utilize each command.

Below is a brief description of each command:
|                    command                    |                                                description                                                | example |
|:---------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:-------:|
|                `all [class]`             | Prints all existing objects.  If class_name is specified, prints all existing objects of type object_name |   '      |
|              `create <class>`              |                                    Creates a new instance of class_name                                   |         |
|         `show <class> <id>`         |                            Prints the instance of class_name with ID object_id                            |         |
| `update <class> <id> <attr_name> <attr_val>` |          Update the attribute attr_name with value attr_val for instance of class_name with ID id         |         |
|            `destroy <cls_name> <id>`            |                                   Delete instance of cls_name with ID id                                  |         |
|                      `quit`                     |                                              Exit the console                                             |         |
|                      `EOF`                      |                                              Exit the console                                             |         |

### Available Classes
```
User
Review
City
Place
State
Amenity
```
Honestly, you can't do anything valuable with these yet.
