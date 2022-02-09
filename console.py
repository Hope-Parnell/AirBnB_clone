#!/usr/bin/python3
"""Module for the console"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import dict_greyson, storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """class for the command console"""
    prompt = '(hbnb)'
    storage.reload()

    def emptyline(self):
        """behavior for an empty line"""
        pass

    def do_clear(self, args):
        """
        Clears the screen

        Usage:
            (hbnb)clear
        """
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_EOF(self, args):
        """
        Exits the console upon end of file input
        """
        return True

    def do_quit(self, args):
        """
        Exits the Console

        Usage:
            (hbnb)quit
        """
        return True

    def do_create(self, args):
        """
        Creates a new instance of a class
        and prints its id

        Usage:
            (hbnb)create <Class Name>
            (hbnb)<class name>.create()
            (hbnb)<class name>.create(<dictionary>)
        Ex:
            (hbnb)create BaseModel
            (hbnb)User.create()
            (hbnb)User.create({"email": "hello@test.com", "i": 0})
        """
        argList = args.split(" ")
        if len(argList[0]) == 0:
            print("** class name missing **")
        elif argList[0] not in dict_greyson.keys():
            print("** class doesn't exist **")
        else:
            objClass = dict_greyson[argList[0]]
            b = objClass()
            b.save()
            print(b.id)

    def do_show(self, args):
        """
        Prints the string representation of
        an instance

        Usage:
            (hbnb)show <class name> <id>
            (hbnb)<class name>.show(<id>)
        Ex:
            (hbnb)show BaseModel 1234-1234-1234
            (hbnb)User.show(1234-5678-9011)
        """
        strArr = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif strArr[0] not in dict_greyson.keys():
            print("** class doesn't exist **")
        elif len(strArr) < 2:
            print("** instance id missing **")
        else:
            #  name = cls.ID#
            name = strArr[0] + "." + strArr[1]
            #  dict of all obj in class.ID: obj format
            d = storage.all()
            #  gets object from dict based on name
            item = d.get(name)
            #  error handling
            if item is None:
                print("** no instance found **")
            #  prints object
            else:
                print(item)

    def do_destroy(self, args):
        """
        Deletes an instance

        Usage:
            (hbnb)destroy <class name> <id>
            (hbnb)<class name>.destoy(<id>)
        Ex:
            (hbnb)destroy BaseModel 1234-1234-1234
            (hbnb)User.destroy(12ab-12cd-12ef)
        """
        #  array of words from args
        strArr = args.split(" ")
        #  error handling
        if len(args) == 0:
            print("** class name missing **")
            return
        elif strArr[0] not in dict_greyson.keys():
            print("** class doesn't exist **")
            return
        elif len(strArr) < 2:
            print("** instance id missing **")
            return
        #  name = class.ID
        name = strArr[0] + "." + strArr[1]
        #  dict of all obj in class.ID: obj format
        d = storage.all()
        # gets object based on name
        item = d.get(name)
        #  error handling
        if item is None:
            print("** no instance found **")
        #  deletes object from dictionary
        else:
            del d[name]
            storage.save()

    def do_all(self, args):
        """
        Displays all istances of a given class
        or all instances if no class is specified

        Usage:
            (hbnb)all <class name>
            (hbnb)<class name>.all()
        Ex:
            (hbnb)all
            (hbnb)all BaseModel
            (hbnb)User.all()
        """
        #  dict of all obj in class.ID: obj format
        d = storage.all()
        #  final list
        objList = []
        #  Printing all objects
        if len(args) == 0:
            #  o is name in class.ID format
            for o in d:
                #  gets object for each name
                item = d.get(o)
                #  adds str rep of each obj to list
                objList.append(str(item))
        #  Printing only specified objects
        else:
            #  array of words from args
            strArr = args.split(" ")
            #  checks if word is a recognized type
            if strArr[0] not in dict_greyson.keys():
                print("** class doesn't exist **")
                return
            else:
                #  o is name in class.ID format
                for o in d:
                    if strArr[0] in o:
                        #  gets object for each name
                        item = d.get(o)
                        #  adds str rep of each obj to list
                        objList.append(str(item))
        #  prints list of str formatted objects
        print(objList)

    def do_update(self, args):
        """
        Updates an attribute of an instance
        Forbidden attributes:
            -id
            -created_at
            -updated at
            -private attributes(Anything starting with a double underscore)
        Usage:
            (hbnb)update <class name> <id> <attribute> "<attribute value>"
            (hbnb)<class name>.update(<id>, <attribute>, "<attribute value>")
            (hbnb)<class name>.update(<id>, <dictionary of attributes>)
        Ex:
            (hbnb)update BaseModel 1234-1234-1234 email "aibnb@mail.com"
            (hbnb)BaseModel.update(1234-1234-1234, email, "aibnb@mail.com")
            (hbnb)BaseModel.update(1234-1234-1234, {"a": "bust", "c": 0})
        """
        #  dict of all obj in class.ID: obj format
        d = storage.all()
        #  if args is empty
        if len(args) == 0:
            print("** class name missing **")
            return
        #  array of words from args
        strArr = args.split(" ", 3)
        if strArr[0] not in dict_greyson.keys():
            print("** class doesn't exist **")
            return
        if len(strArr) > 1:
            # gets object
            obj = d.get(strArr[0] + "." + strArr[1])
            if obj is None:
                print("** no instance found **")
                return
        if len(strArr) < 4:
            if len(strArr) == 1:
                print("** instance id missing **")
            elif len(strArr) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return
        else:
            try:
                if strArr[3][0] != '"':
                    print("** value must be in \"quotes\" **")
                    return
                for i in range(1, len(strArr[3])):
                    if strArr[3][i] == '"':
                        break
                if strArr[3][i] != '"':
                    print("** value must be in \"quotes\" **")
                    return
                else:
                    strArr[3] = strArr[3][1:i]
                    if strArr[2][0] == "_" and strArr[2][1] == "_":
                        print("** cannot update private attribute '{}' **".format(
                            strArr[2]))
                        return
                if strArr[2] in obj.__dict__:
                    attrType = type(getattr(obj, strArr[2]))
                    strArr[3] = attrType(strArr[3])
                if strArr[2] in type(obj).__dict__:
                    objClass = type(obj)
                    attrType = type(getattr(objClass, strArr[2]))
                    strArr[3] = attrType(strArr[3])
                setattr(obj, strArr[2], strArr[3])
                obj.save()
            except Exception:
                print("** {} is not a valid value for {} **".format(
                    strArr[3], strArr[2]))
                print("** {} must be a(n) {} **".format(
                    strArr[2], attrType.__name__))

    def do_count(self, args):
        """
        Counts objects of a specific class

        Usage:
            (hbnb)count <class name>
            (hbnb)<class name>.count()
        Ex:
            (hbnb)count User
            (hbnb)User.count()
        """
        args = args.split()
        args = args[0]
        count = 0
        d = storage.all()
        for key in d:
            dClass = key.split('.')
            if dClass[0] == args:
                count += 1
        print(count)

    def update(self, args):
        """updates an instance"""
        #try:
        objClass = args.split(" ", 1)
        objID = objClass[1].split(", ", 1)
        if objID[1][0] != '{':
            objAttr = objID[1].split(", ", 1)
            self.do_update("{} {} {} {}".format(
                    objClass[0], objID[0], objAttr[0], objAttr[1]))
        else:
            objAttr = objID[1]
            if objAttr[-1] == "}":
                forbidden = ["id", "created_at", "updated_at", "__class__"]
                attr_dict = json.loads(objAttr)
                for item in attr_dict:
                    if item not in forbidden:
                        self.do_update("{} {} {} {}".format(
                            objClass[0],
                            objID[0], item, '"' + str(attr_dict[item]) + '"'))
            else:
                raise TypeError("input must be dict")

    def do_save(self, args):
        """
        Saves all instances of a class to <filename>.
        Instances will be saved in JSON format.
        If no filename is given, it will be saved to
        "<class name>.json"
        <filename> should not contain whitespace.
        Use "ALL" as <class name> to save all.

        Usage:
            (hbnb)save <class name> "<filename>"
            (hbnb)<class name>.save("filename")
        Ex:
            (hbnb)save User "my_users"
            (hbnb)User.save("my_users")
            (hbnb)save ALL
            (hbnb)ALL.save()
        """
        cmdArgs = args.split()
        if len(cmdArgs) == 0:
            print("** class name missing **")
            return
        st = FileStorage()
        if len(cmdArgs) > 1:
            if cmdArgs[1][0] != '"' or cmdArgs[1][-1] != '"':
                print("** filename must be in \"quotes\" **")
                return
            st.file_path = cmdArgs[1][1:-1]
        else:
            st.file_path = cmdArgs[0] + ".json"
        d = storage.all()
        st.clear()
        for key in d:
            if cmdArgs[0] == "ALL" or cmdArgs[0] in key:
                st.new(d[key])
        st.save()

    def do_list(self, args):
        """
        Displays the number of instances of a class
        and lists them in <class name>.<id> format,
        one per line.
        if no class is specifed, lists all instances

        Usage: list <class name>
               <class name>.list()
        Ex:
            (hbnb)list User
            (hbnb)list
            (hbnb)Place.list()
        """
        d = storage.all()
        arr = args.split()
        c = []
        if len(arr) == 0:
            arr = ["instance"]
            for key in d:
                c.append(key)
        else:
            if arr[0] in dict_greyson:
                for key in d:
                    if arr[0] in key:
                        c.append(key)
            else:
                print("** class doesn't exist **")
                return
        if len(c) == 0:
            print("There are no {}s.".format(arr[0]))
        elif len(c) == 1:
            print("There is 1 {}:".format(arr[0]))
        else:
            print("There are {} {}s:".format(len(c), arr[0]))
        for item in sorted(c):
            print(item)

    def do_load(self, args):
        """
        Loads objects from a file
        and adds them to storage

        If no filename is specifed
        "file.json" will be used

        *<filename> should not contain
        whitespace

        Usage:
            (hbnb)load "<filename>"
        Ex:
            (hbnb)load "User.json"
        """
        st = FileStorage()
        filename = args.split()
        if len(filename) > 0:
            if filename[0][0] != '"' or filename[0][-1] != '"':
                print("** filename must be in \"quotes\" **")
                return
            else:
                st.file_path = filename[0][1:-1]
        st.reload()
        d = st.all()
        for key in d:
            storage.new(d[key])
        storage.save()

    def create(self, args):
        """creates a new object"""
        if "{" in args:
            oClass = args.split(" ", 1)
            if oClass[0] in dict_greyson:
                attr_dict = json.loads(oClass[1])
                if type(attr_dict) is not dict:
                    raise TypeError("input must be dictionary")
                else:
                    obj = dict_greyson[oClass[0]](**attr_dict)
                    print(obj.id)
                    obj.save()
            else:
                print("** class doesn't exist **")
        else:
            self.do_create(args)

    def default(self, line):
        """default behavior if command not found"""
        cmds = {"all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.update,
                "list": self.do_list,
                "save": self.do_save,
                "create": self.create}
        if '.' in line:
            cmdClass = line.split('.', 1)
        else:
            print("*** Unknown syntax: {}".format(line))
            return
        if '(' in cmdClass[1]:
            command = cmdClass[1].split('(', 1)
        else:
            print("*** Unknown syntax: {}".format(line))
            return
        if command[1][-1] == ')':
            args = command[1][0:-1]
        else:
            print("*** Unknown syntax: {}".format(line))
            return
        if command[0] in cmds:
            new_var = cmds[command[0]]("{} {}".format(cmdClass[0], args))
            new_var
        else:
            print("*** Unknown syntax: {}".format(line))
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
