
# AirBnB_clone Console
This project begins the Console for an AirBnB clone. The console can manipulate and store (in memory and in storage using JSON) BaseModels that will be used in later expansions upon this project.

## The console will handle the following tasks:
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

## Files and Directories:
- console
runs the console for the project. 
- models 
directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
 -	tests 
directory will contain all unit tests.
- console.py 
  file is the entry point of our command interpreter.
- models
	- base_model.py 
	  file is the base class of all our models. It contains common elements:
	   attributes: id, created_at and updated_at
	- User
		 Class for User. Contains email, password, first_name, and last_name attributes
	- State:
		Class for State. Contains name attribute
	- City:
	 Class for City. Contains state_id and name attributes
	- Amenity:
	Class for Amenitiy. Contains name attribute
	- Place:
	Class for Place. Contains city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, amenity_ids, latitude, and longitude attributes
	- Review:
		Class for Review. Contains place_id, user_id, and text attributes
	- engine 		
	  directory will contain all storage classes (using the same prototype). For the moment you will have only one: 
		-	file_storage.py
		 methods and files for file storage in the project

# Execution:
**Interactive Mode:**
```
$ ./console.py
(hbnb) help

Documented commands (type help \<topic\>):
========================================

EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
**Non-Interactive Mode:**
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Important concepts
Key takeaways/topics from project.
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is args and how to use it
* What is kwargs and how to use it
* How to handle named arguments in a function

## Tasks
List of tasks with brief descriptions of each task.
### 0. README, AUTHORS
README and AUTHORS files exist and explain the project

---
### 1. Be PEP8 compliant!

code is PEP8 / pycodestyle compliant

---

### 2. UnitTesting

each part of code is thoroughly unit tested

---

### 3. BaseModel

write BaseModel class that defines all common attributes/methods for other classes

---

### 4. Create BaseModel from dictionary

implement BaseModel method to convert a BaseModel to a dictionary Python object

---

### 5. Store first object

Objects are stored in using the following framework:

**class 'BaseModel' 
-> 
to_dict() 
-> 
class 'dict' 
-> 
JSON dump 
-> 
class 'str' 
-> 
FILE 
-> 
class 'str'
-> 
JSON load 
-> 
class 'dict'
-> 
class 'BaseModel'**


---

### 6. Console 0.0.1

Objects are stored in using the following framework:

# AirBnB_clone Console

(optional) This project begins the Console for an AirBnB clone. The console can manipulate and store (in memory and in storage using JSON) BaseModels that will be used in later expansions upon this project.
The console will handle the following tasks:
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

Files and Directories:
models 
  directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests 
  directory will contain all unit tests.
console.py 
  file is the entry point of our command interpreter.
models/base_model.py 
  file is the base class of all our models. It contains common elements:
    attributes: id, created_at and updated_at
methods: 
  save() and to_json()
models/engine 
  directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

Engine:
FileStorage:
Console:

Models:
BaseModel:
User:
State:
City:
Amenity:
Place:
Review:

Execution:
Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help \<topic\>):
========================================

EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
Non-interactive Mode:
  $ echo "help" | ./console.py
(hbnb)
```
```
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
___

## Important concepts
Key takeaways/topics from project.
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is args and how to use it
* What is kwargs and how to use it
* How to handle named arguments in a function

## Tasks
List of tasks with brief descriptions of each task.
### 0. README, AUTHORS
README and AUTHORS files exist and explain the project

---
### 1. Be PEP8 compliant!

code is PEP8 / pycodestyle compliant

---

### 2. UnitTesting

each part of code is thoroughly unit tested

---

### 3. BaseModel

write BaseModel class that defines all common attributes/methods for other classes

---

### 4. Create BaseModel from dictionary

implement BaseModel method to convert a BaseModel to a dictionary Python object

---

### 5. Store first object

Objects are stored in using the following framework:

**class 'BaseModel' 
-> 
to_dict() 
-> 
class 'dict' 
-> 
JSON dump 
-> 
class 'str' 
-> 
FILE 
-> 
class 'str'
-> 
JSON load 
-> 
class 'dict'
-> 
class 'BaseModel'**


---

### 6. Console 0.0.1

Write console with commands quit() and help()

---
### 7. Console 0.1

Update console with  create(), show(), destroy(), all(), and update() commands

---
### 8. First User
write class for User with attributes:
-   `email`: string - empty string
-   `password`: string - empty string
-   `first_name`: string - empty string
-   `last_name`: string - empty string

---
### 9. More classes!
Write classes that inherit from BaseModel:
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
---
### 10. Console 1.0
Update  `FileStorage`  to manage correctly serialization and deserialization of all classes:  `Place`,  `State`,  `City`,  `Amenity`  and  `Review`

Update command interpreter (`console.py`) to allow actions:  `show`,  `create`,  `destroy`,  `update`  and  `all`  with all classes created previously.

---
