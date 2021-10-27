#!/usr/bin/python3
"""Module for the console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import dict_greyson, storage

class HBNBCommand(cmd.Cmd):
    """class for the command console"""
    prompt = '(hbnb)'
    def emptyline(self):
        pass

    def do_EOF(self, args):
        """Exits the console"""
        return True

    def do_quit(self, args):
        """Exits the Console"""
        return True

    def do_create(self, args):
        """Creates a new instance of a class
        and prints its id

        usage: create <Class Name>
        Ex: create BaseModel
        """
        #error handling
        if len(args) == 0:
            print("** class name missing **")
        elif args not in dict_greyson.keys():
            print("** class doesn't exist **")
        else:
            objClass = dict_greyson[args]
            #creates a new base model
            b = objClass()
            #saves to json doc
            b.save()
            #prints ID
            print(b.id)

    def do_show(self, args):
        """prints the string representation of
        an instance

        usage: show <class name> <id>
        ex: show BaseModel 1234-1234-1234
        """
        #array of words from args
        strArr = args.split(" ")
        #error handling
        if args == 0:
            print("** class name missing **")
        elif strArr[0] not in dict_greyson.keys():
            print("** class doesn't exist **")
        elif len(strArr) < 2:
            print("** instance id missing **")
        else:
            #name = cls.ID
            name = strArr[0] + "." + strArr[1]
            #dict of all obj in class.ID: obj format
            d = storage.all()
            #gets object from dict based on name
            item = d.get(name)
            #error handling
            if item == None:
                print("** no instance found **")
            #prints object
            else:
                print(item)


    def do_destroy(self, args):
        """deletes an instance

        usage: destroy <class name> <id>
        Ex: destroy BaseModel 1234-1234-1234
        """
        #array of words from args
        strArr = args.split(" ")
        #error handling
        if len(args) == 0:
            print("** class name missing **")
            return
        elif strArr[0] not in dict_greyson.keys():
            print("** class doesn't exist **")
            return
        elif len(strArr) < 2:
            print("** instance id missing **")
            return
        #name = class.ID
        name = strArr[0] + "." + strArr[1]
        #dict of all obj in class.ID: obj format
        d = storage.all()
        #gets object based on name
        item = d.get(name)
        #error handling
        if item == None:
            print("** no instance found **")
        #deletes object from dictionary
        else:
            del d[name]
            storage.save()

    def do_all(self, args):
        """displays all istances of a given class
        or all instances if no class is specified

        usage: all <class name>
        Ex: all
            lists all instances
        Ex: all BaseModel
            lists all instances of BaseModel
        """
        #dict of all obj in class.ID: obj format
        d = storage.all()
        #final list
        l = []
        #Printing all objects
        if len(args) == 0:
            #o is name in class.ID format
            for o in d:
                #gets object for each name
                item = d.get(o)
                #adds str rep of each obj to list
                l.append(str(item))
        #Printing only specified objects
        else:
            #array of words from args
            strArr = args.split(" ")
            #checks if word is a recognized type
            if strArr[0] not in dict_greyson.keys():
                print("** class doesn't exist **")
                return
            else:
                #o is name in class.ID format
                for o in d:
                    #splits cls.ID into cls and ID
                    nameSplitArr = o.split(".")
                    #checks if class is recognized
                    if nameSplitArr[0] == strArr[0]:
                        #gets object for each name
                        item = d.get(o)
                        #adds str rep of each obj to list
                        l.append(str(item))
        #prints list of str formatted objects
        print(l)

    #Usage: update <class name> <id> <attribute name> "<attribute value>"
    def do_update(self, args):
        """updates an attribute of an instance

        usage: update <class name> <id> <attribute> "<attribute value>"
        Ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        #dict of all obj in class.ID: obj format
        d = storage.all()
        #if args is empty
        if len(args) == 0:
            print("** class name missing **")
            return
        #array of words from args
        strArr = args.split(" ")
        if len(strArr) < 4:
            if len(strArr) == 1:
                print("** instance id missing **")
                return
            elif len(strArr) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return
        else:
            if strArr[0] not in dict_greyson.keys():
                 print("** class doesn't exist **")
            else:
                obj = d.get(strArr[0] + "." +  strArr[1])
                if obj == None:
                    print("** no instance found **")
                    return
                try:
                    #gets object
                    setattr(obj, strArr[2], strArr[3])
                    obj.save()
                #attribute value doesen't exist:
                except Exception:
                    print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
