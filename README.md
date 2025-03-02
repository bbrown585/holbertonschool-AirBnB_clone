# Welcome to the console
### How to start the console
 To begin the console, in the terminal window type.

    ./console
you will be greeted with this prompt.

    (hbnb) 
next type.

    help
this will bring up a list of possible commands.

    EOF  all  create  destroy  help  quit  show  update
using the help command with any command in the list will show a description of the commands function.

# basic console commands
## help
help is used to retrieve a description of a function
### ex.

    (hbnb) help all
    Prints string representation of all instances of an Object
## EOF
the EOF command is used to exit the command through the end of file method.
### ex.

    ctrl + D
## quit
the quit command exits the console.
### ex.

    (hbnb) quit
## empty line
The empty line command simply returns an empty line to the console by pressing the enter key.
### ex.

    (hbnb)
    (hbnb)
    (hbnb)


# Advanced console functions
## all
the all function can be used by simply typing

    all
this will list all current object instances regardless of class
### ex

    (hbnb)all
    ["[User] (adc84863-9891-4c99-b063-04c5483fc2b3) {'id': 'adc84863-9891-4c99-b063-04c5483fc2b3', 'created_at': datetime.datetime(2022, 10, 3, 14, 46, 36, 118633), 'updated_at': datetime.datetime(2022, 10, 3, 14, 46, 36, 118735)}", 
    "[BaseModel] (e34d988b-e3c3-41b1-ac1f-3cc283bc91c8) {'id': 'e34d988b-e3c3-41b1-ac1f-3cc283bc91c8', 'created_at': datetime.datetime(2022, 10, 7, 10, 22, 52, 660445), 'updated_at': datetime.datetime(2022, 10, 7, 10, 22, 52, 660498)}", 
    "[Place] (c8f4c5bd-4e72-411c-bb47-e7b101f3738b) {'id': 'c8f4c5bd-4e72-411c-bb47-e7b101f3738b', 'created_at': datetime.datetime(2022, 10, 7, 10, 23, 38, 127013), 'updated_at': datetime.datetime(2022, 10, 7, 10, 23, 38, 127036)}", 
    "[User] (a5d6285b-0014-4458-a00a-f92a11fc4493) {'id': 'a5d6285b-0014-4458-a00a-f92a11fc4493', 'created_at': datetime.datetime(2022, 10, 7, 10, 23, 51, 165427), 'updated_at': datetime.datetime(2022, 10, 7, 10, 23, 51, 165456)}"]
The user can also specify the Class the wish to view
### ex.

    (hbnb)all User
    ["[User] (adc84863-9891-4c99-b063-04c5483fc2b3) {'id': 'adc84863-9891-4c99-b063-04c5483fc2b3', 'created_at': datetime.datetime(2022, 10, 3, 14, 46, 36, 118633), 'updated_at': datetime.datetime(2022, 10, 3, 14, 46, 36, 118735)}", 
    "[User] (a5d6285b-0014-4458-a00a-f92a11fc4493) {'id': 'a5d6285b-0014-4458-a00a-f92a11fc4493', 'created_at': datetime.datetime(2022, 10, 7, 10, 23, 51, 165427), 'updated_at': datetime.datetime(2022, 10, 7, 10, 23, 51, 165456)}"]
## create
the create function is used to create a new object instance.
this command requires a Class name.
### ex.

    (hbnb)create Basemodel
    dcd56982-309a-4045-b337-b2e28a82e0c3
The unique instance id is the =n shown to the user as in the example above.

## destroy
the destroy command is used to destroy an instance of an object.
this command requires the Class name and instance id
### ex.

    (hbnb)destroy Basemodeldcd56982-309a-4045-b337-b2e28a82e0c3
    (hbnn)
At first it appears that nothing has happened, but using the all or show command will reveal the instance has been removed.
## show
The show command is use to show a specific instance of an object.
this command requires the Class name and instance id.
### ex.

    (hbnb) show BaseModel dcd56982-309a-4045-b337-b2e28a82e0c3
    [BaseModel] (dcd56982-309a-4045-b337-b2e28a82e0c3) {'id': 'dcd56982-309a-4045-b337-b2e28a82e0c3', 'created_at': datetime.datetime(2022, 10, 7, 10, 29, 55, 915062), 'updated_at': datetime.datetime(2022, 10, 7, 10, 29, 55, 915209)}
    (hbnb)
unlike the all command the show command only shows the specified instance of an object.
## update
The update command is used to update or add an attribute to an object instance.
This command take 4 parameters the class name, the instance id, the attribute name, and the attribute value
### ex.

    (hbnb) update BaseModel dcd56982-309a-4045-b337-b2e28a82e0c3 new_attribute 42
    (hbnb) show BaseModel dcd56982-309a-4045-b337-b2e28a82e0c3
    [BaseModel] (dcd56982-309a-4045-b337-b2e28a82e0c3) {'id': 'dcd56982-309a-4045-b337-b2e28a82e0c3', 'created_at': datetime.datetime(2022, 10, 7, 10, 29, 55, 915062), 'updated_at': datetime.datetime(2022, 10, 7, 10, 29, 55, 915209),
     'new_attribute': '42'
Using the show command we can see the "new_attribute" now equals 42.
    
    


# Holberton AirBnB Project Overview
## 0x00. AirBnB clone - The console
### 0. README, AUTHORS
-   Write a  `README.md`:
    -   description of the project
    -   description of the command interpreter:
        -   how to start it
        -   how to use it
        -   examples
-   You should have an  `AUTHORS`  file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference  [Docker’s AUTHORS page](https://intranet.hbtn.io/rltoken/2xQDLdT-lJsnNl3xSfTjgA "Docker's AUTHORS page")
-   You should use branches and pull requests on GitHub - it will help you as team to organize your work

### 1. Create a SSH RSA key pair
Read for this task:

-   [Linux and Mac OS users](https://intranet.hbtn.io/rltoken/65o9nqlAsknVpzPnfonnfg "Linux and Mac OS users")
-   [Windows users](https://intranet.hbtn.io/rltoken/aP8WbMiUfDQH854VICciDw "Windows users")

man:  `ssh-keygen`

You will soon have to manage your own  **servers**  concept page hosted on remote  [data centers](https://intranet.hbtn.io/rltoken/kYVyvQG9IAIzKEMY1I1IQQ "data centers"). We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:

-   Share your  **public key**  in your answer file  `0-RSA_public_key.pub`
-   Fill the  `SSH public key`  field of your  [intranet profile](https://intranet.hbtn.io/rltoken/ldYVdb7K0IZkw-IKVdmA_Q "intranet profile")  with the public key you just generated
-   **Keep the private key to yourself in a secure location**, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
-   If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

SSH and RSA keys will be covered in depth in a later project.

### 2. Be PEP8 compliant!
Write beautiful code that passes the PEP8 checks.

### 3. Unittests
All your files, classes, functions must be tested with unit tests

### 4. BaseModel
Write a class  `BaseModel`  that defines all common attributes/methods for other classes:

-   `models/base_model.py`
-   Public instance attributes:
    -   `id`: string - assign with an  `uuid`  when an instance is created:
        -   you can use  `uuid.uuid4()`  to generate unique  `id`  but don’t forget to convert to a string
        -   the goal is to have unique  `id`  for each  `BaseModel`
    -   `created_at`: datetime - assign with the current datetime when an instance is created
    -   `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
-   `__str__`: should print:  `[<class name>] (<self.id>) <self.__dict__>`
-   Public instance methods:
    -   `save(self)`: updates the public instance attribute  `updated_at`  with the current datetime
    -   `to_dict(self)`: returns a dictionary containing all keys/values of  `__dict__`  of the instance:
        -   by using  `self.__dict__`, only instance attributes set will be returned
        -   a key  `__class__`  must be added to this dictionary with the class name of the object
        -   `created_at`  and  `updated_at`  must be converted to string object in ISO format:
            -   format:  `%Y-%m-%dT%H:%M:%S.%f`  (ex:  `2017-06-14T22:31:03.285259`)
            -   you can use  `isoformat()`  of  `datetime`  object
        -   This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our  `BaseModel`

### 5. Create BaseModel from dictionary
Previously we created a method to generate a dictionary representation of an instance (method  `to_dict()`).

Now it’s time to re-create an instance with this dictionary representation.

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>

```

Update  `models/base_model.py`:

-   `__init__(self, *args, **kwargs)`:
    -   you will use  `*args, **kwargs`  arguments for the constructor of a  `BaseModel`. (more information inside the  **AirBnB clone**  concept page)
    -   `*args`  won’t be used
    -   if  `kwargs`  is not empty:
        -   each key of this dictionary is an attribute name (**Note**  `__class__`  from  `kwargs`  is the only one that should not be added as an attribute. See the example output, below)
        -   each value of this dictionary is the value of this attribute name
        -   **Warning**:  `created_at`  and  `updated_at`  are strings in this dictionary, but inside your  `BaseModel`  instance is working with  `datetime`  object. You have to convert these strings into  `datetime`  object. Tip: you know the string format of these datetime
    -   otherwise:
        -   create  `id`  and  `created_at`  as you did previously (new instance)

### 6. Store first object
Now we can recreate a  `BaseModel`  from another one by using a dictionary representation:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>

```

It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

-   Python doesn’t know how to convert a string to a dictionary (easily)
-   It’s not human readable
-   Using this file with another program in Python or other language will be hard.

So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>

```

Magic right?

Terms:

-   **simple Python data structure**: Dictionaries, arrays, number and string. ex:  `{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }`
-   **JSON string representation**: String representing a simple data structure in JSON format. ex:  `'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'`

Write a class  `FileStorage`  that serializes instances to a JSON file and deserializes JSON file to instances:

-   `models/engine/file_storage.py`
-   Private class attributes:
    -   `__file_path`: string - path to the JSON file (ex:  `file.json`)
    -   `__objects`: dictionary - empty but will store all objects by  `<class name>.id`  (ex: to store a  `BaseModel`  object with  `id=12121212`, the key will be  `BaseModel.12121212`)
-   Public instance methods:
    -   `all(self)`: returns the dictionary  `__objects`
    -   `new(self, obj)`: sets in  `__objects`  the  `obj`  with key  `<obj class name>.id`
    -   `save(self)`: serializes  `__objects`  to the JSON file (path:  `__file_path`)
    -   `reload(self)`: deserializes the JSON file to  `__objects`  (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

Update  `models/__init__.py`: to create a unique  `FileStorage`  instance for your application

-   import  `file_storage.py`
-   create the variable  `storage`, an instance of  `FileStorage`
-   call  `reload()`  method on this variable

Update  `models/base_model.py`: to link your  `BaseModel`  to  `FileStorage`  by using the variable  `storage`

-   import the variable  `storage`
-   in the method  `save(self)`:
    -   call  `save(self)`  method of  `storage`
-   `__init__(self, *args, **kwargs)`:
    -   if it’s a new instance (not from a dictionary representation), add a call to the method  `new(self)`  on  `storage`

### 7. Console 0.0.1
Write a program called  `console.py`  that contains the entry point of the command interpreter:

-   You must use the module  `cmd`
-   Your class definition must be:  `class HBNBCommand(cmd.Cmd):`
-   Your command interpreter should implement:
    -   `quit`  and  `EOF`  to exit the program
    -   `help`  (this action is provided by default by  `cmd`  but you should keep it updated and documented as you work through tasks)
    -   a custom prompt:  `(hbnb)`
    -   an empty line +  `ENTER`  shouldn’t execute anything
-   Your code should not be executed when imported

**Warning:**

You should end your file with:

```
if __name__ == '__main__':
    HBNBCommand().cmdloop()

```

to make your program executable except when imported. Please don’t add anything around - the Checker won’t like it otherwise

### 8. Console 0.1
Update your command interpreter (`console.py`) to have these commands:

-   `create`: Creates a new instance of  `BaseModel`, saves it (to the JSON file) and prints the  `id`. Ex:  `$ create BaseModel`
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ create`)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ create MyModel`)
-   `show`: Prints the string representation of an instance based on the class name and  `id`. Ex:  `$ show BaseModel 1234-1234-1234`.
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ show`)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ show MyModel`)
    -   If the  `id`  is missing, print  `** instance id missing **`  (ex:  `$ show BaseModel`)
    -   If the instance of the class name doesn’t exist for the  `id`, print  `** no instance found **`  (ex:  `$ show BaseModel 121212`)
-   `destroy`: Deletes an instance based on the class name and  `id`  (save the change into the JSON file). Ex:  `$ destroy BaseModel 1234-1234-1234`.
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ destroy`)
    -   If the class name doesn’t exist, print  `** class doesn't exist ** (ex:`$ destroy MyModel`)`
    -   If the  `id`  is missing, print  `** instance id missing **`  (ex:  `$ destroy BaseModel`)
    -   If the instance of the class name doesn’t exist for the  `id`, print  `** no instance found **`  (ex:  `$ destroy BaseModel 121212`)
-   `all`: Prints all string representation of all instances based or not on the class name. Ex:  `$ all BaseModel`  or  `$ all`.
    -   The printed result must be a list of strings (like the example below)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ all MyModel`)
-   `update`: Updates an instance based on the class name and  `id`  by adding or updating attribute (save the change into the JSON file). Ex:  `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
    -   Usage:  `update <class name> <id> <attribute name> "<attribute value>"`
    -   Only one attribute can be updated at the time
    -   You can assume the attribute name is valid (exists for this model)
    -   The attribute value must be casted to the attribute type
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ update`)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ update MyModel`)
    -   If the  `id`  is missing, print  `** instance id missing **`  (ex:  `$ update BaseModel`)
    -   If the instance of the class name doesn’t exist for the  `id`, print  `** no instance found **`  (ex:  `$ update BaseModel 121212`)
    -   If the attribute name is missing, print  `** attribute name missing **`  (ex:  `$ update BaseModel existing-id`)
    -   If the value for the attribute name doesn’t exist, print  `** value missing **`  (ex:  `$ update BaseModel existing-id first_name`)
    -   All other arguments should not be used (Ex:  `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"`  =  `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`)
    -   `id`,  `created_at`  and  `updated_at`  cant’ be updated. You can assume they won’t be passed in the  `update`  command
    -   Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime

Let’s add some rules:

-   You can assume arguments are always in the right order
-   Each arguments are separated by a space
-   A string argument with a space must be between double quote
-   The error management starts from the first argument to the last one

### 9. First User
Write a class  `User`  that inherits from  `BaseModel`:

-   `models/user.py`
-   Public class attributes:
    -   `email`: string - empty string
    -   `password`: string - empty string
    -   `first_name`: string - empty string
    -   `last_name`: string - empty string

Update  `FileStorage`  to manage correctly serialization and deserialization of  `User`.

Update your command interpreter (`console.py`) to allow  `show`,  `create`,  `destroy`,  `update`  and  `all`  used with  `User`.

### 10. More classes!
Write all those classes that inherit from  `BaseModel`:

-   `State`  (`models/state.py`):
    -   Public class attributes:
        -   `name`: string - empty string
-   `City`  (`models/city.py`):
    -   Public class attributes:
        -   `state_id`: string - empty string: it will be the  `State.id`
        -   `name`: string - empty string
-   `Amenity`  (`models/amenity.py`):
    -   Public class attributes:
        -   `name`: string - empty string
-   `Place`  (`models/place.py`):
    -   Public class attributes:
        -   `city_id`: string - empty string: it will be the  `City.id`
        -   `user_id`: string - empty string: it will be the  `User.id`
        -   `name`: string - empty string
        -   `description`: string - empty string
        -   `number_rooms`: integer - 0
        -   `number_bathrooms`: integer - 0
        -   `max_guest`: integer - 0
        -   `price_by_night`: integer - 0
        -   `latitude`: float - 0.0
        -   `longitude`: float - 0.0
        -   `amenity_ids`: list of string - empty list: it will be the list of  `Amenity.id`  later
-   `Review`  (`models/review.py`):
    -   Public class attributes:
        -   `place_id`: string - empty string: it will be the  `Place.id`
        -   `user_id`: string - empty string: it will be the  `User.id`
        -   `text`: string - empty string
