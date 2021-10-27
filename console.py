#!/usr/bin/python3
"""Module for the console"""
import cmd
from models.base_model import BaseModel 
from models import storage

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
        #error handling
        if len(args) == 0:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            #creates a new base model
            b = BaseModel()
            #saves to json doc
            b.save()
            #prints ID
            print(b.id)

    def do_show(self, args):
        #array of words from args
        strArr = args.split(" ")
        #error handling
        if args == 0:
            print("** class name missing **")
        elif strArr[0] != "BaseModel":
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
        #array of words from args
        strArr = args.split(" ")
        #error handling
        if len(args) == 0:
            print("** class name missing **")
            return
        elif strArr[0] != "BaseModel":
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
            if strArr[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            else:
                #o is name in class.ID format
                for o in d:
                    #splits cls.ID into cls and ID
                    nameSplitArr = o.split(".")
                    #checks if class is recognized
                    if nameSplitArr[0] == "BaseModel":
                        #gets object for each name
                        item = d.get(o)
                        #adds str rep of each obj to list
                        l.append(str(item)) 
        #prints list of str formatted objects
        print(l)

    #Usage: update <class name> <id> <attribute name> "<attribute value>"
    def do_update(self, args):
        #dict of all obj in class.ID: obj format
        d = storage.all()        
        #if args is empty
        if len(args) == 0:
            print("** class name missing **")
            return
        #array of words from args
        strArr = args.split(" ")
        if len(strArr) == 1:
            if strArr[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
            return
        elif len(strArr) == 2:
            if strArr[0] != "BaseModel":
                print("** class doesn't exist **")
            elif d.get("BaseModel" + "." +  strArr[1]) == None:
                print("** no instance found **")
            else:
                print("** attribute name missing **") 
        elif len(strArr) == 3:
            if strArr[0] != "BaseModel":
                print("** class doesn't exist **")
            elif d.get("BaseModel" + "." +  strArr[1]) == None:
                print("** no instance found **")
            else: 
                print("** attribute name missing **")
        else:
            if strArr[0] != "BaseModel":
                print("** class doesn't exist **")
            elif d.get("BaseModel" + "." +  strArr[1]) == None:
                print("** no instance found **")
            try:
                #gets object
                obj = d.get("BaseModel" + "." +  strArr[1])
                setattr(obj, strArr[2], strArr[3])
                obj.save() 
            #attribute value doesen't exist:
            except Exception:
                print("** value missing **")

        #UPDATE UPDATEDAT



    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
