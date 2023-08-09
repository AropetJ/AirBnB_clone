#!/usr/bin/python3
# console.py

import cmd
import os
import shlex
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """Exits the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, args):
        """Creates a new file with given name and content
        """
        if not args:
            print("** class name missing **")
            return

        if args:
            class_name = args.split()[0]
            if class_name not in ["BaseModel", "User", "Place", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
    
        new_instance = class_name()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id.
        """
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
    
        if args_list:
            class_name = args.split()[0]
            if class_name not in ["BaseModel", "User", "Place", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            if len(args_list) < 2:
                print("** instance id missing **")
                return
    
        instance = storage.all()
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"
        if key in instance:
            print(instance[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
        if args_list:
            class_name = args_list[0]
            if class_name not in ["BaseModel", "User", "Place", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            if len(args_list) < 2:
                print("** instance id missing **")
                return

        instance = storage.all()
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"
        if key in instance:
            instance.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name. """
        cls_name = args.split()[0] if args else None
        cls = None
        if cls_name:
            try:
                cls = eval(cls_name)
            except:
                print("** class doesn't exist **")
                return

        instances = storage.all().values()
        if cls:
            instances = [instance for instance in instances if isinstance(instance, cls)]
            print([str(instance) for instance in instances])

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        if not args:
            print("** class name missing **")
            return
        try:
            args_list = shlex.split(args)
            cls_name , obj_id = args_list[0], args_list[1]
            key = f"{cls_name}.{obj_id}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
                return
            if len(args_list) < 3:
                print("** attribute name missing **")
                return
            attr_name= args_list[2]
            if len(args_list) < 4:
                print("** value missing **")
                return
            new_value = args_list[3]
            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                setattr(obj, attr_name, attr_type(new_value))
                obj.save()
            else:
                print("** no attribute found **")

        except:
            print("** class does not exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()