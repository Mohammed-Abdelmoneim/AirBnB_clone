import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "

    def do_greet(self, line):
        """test"""
        print(f"hello {line}")

    def do_EOF(self, line):
        """to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
