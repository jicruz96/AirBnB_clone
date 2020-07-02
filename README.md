# AirBnB_clone
The AirBnB clone utilizes higher level programming skills to deploy a copy of the AirBnB website.

## Console
The console is a command interpreter that manages all AirBnB objects.

### Using the Console

#### Interactive Mode
##### Starting on Interactive Mode
Run `./console.py`to begin a session. 

A prompt should appear where you can write commands.
Type `help` to get a list of available commands.
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit 
```

#### Non-Interactive Mode
You can also use the console non-interactively. 
#### Using "echo"
You can "pipe" an input into the command by using `echo`, as seen below:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
```
#### Using a file
You can also pipe in a file with one command per line, as seen below:
```
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```
### Tips
Typing `help <command>` or `?<command>` will print information on how to utilize each command.

Below is a brief description of each command:
|                    command                    |                                                description                                                |
|:---------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|                `all [class]`             | Prints all existing objects.  If class_name is specified, prints all existing objects of type object_name |
|              `create <class>`              |                                    Creates a new instance of class_name                                   |
|         `show <class> <id>`         |                            Prints the instance of class_name with ID object_id                            |
| `update <class> <id> <attr_name> <attr_val>` |          Update the attribute attr_name with value attr_val for instance of class_name with ID id         |
|            `destroy <cls_name> <id>`            |                                   Delete instance of cls_name with ID id                                  |
|                      `quit`                     |                                              Exit the console                                             |
|                      `EOF`                      |                                              Exit the console                                             |

### Available Classes
```
User
Review
City
Place
State
Amenity
```
Honestly, you can't do anything valuable with these yet. But have making them!

### Questions, Comments, Sugestions
If you have questions or suggestions, contact J.I. Cruz at ji@jicruz.com or Kelsie Merchant at eislek@gmail.com 
