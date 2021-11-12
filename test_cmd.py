import cmd

class HBTNcmd(cmd.Cmd):
    prompt = "(hbtn)"
    def do_print(self, arg):
        print("{}".format(arg))

    def emptyline(self):
        pass
    
    def do_quit(self, arg):
        return True
    
    def do_EOF(self, arg):
        print("")
        return True
    
if __name__ == "__main__":
    HBTNcmd().cmdloop()
