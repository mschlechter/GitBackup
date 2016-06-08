import sys
from typing import Iterable

class ArgHelper:

    def __init__(self, args: Iterable[str]):
        self.args = args
        self.__parse_arguments()

    def __parse_arguments(self):
        argc = len(self.args)
        if argc < 3:
            self.__print_banner();
            sys.exit(1)
        
        self.destination = self.args[argc-1]
        self.source = self.args[argc-2]

        # Set options
        self.zip = False
        self.verbose = False

        for i in range(0, argc-2):
            currentarg = self.args[i]

            if currentarg == "-zip":
                self.zip = True

            if currentarg == "-verbose":
                self.verbose = True

    def __print_banner(self):

        print("Correct syntax is:\n")
        print("gitbackup <options> SOURCE_DIRECTORY DESTINATION_DIRECTORY")
        print("")
        print("Options can be:")
        print("-zip     Create zip archives")
        print("-verbose Show git output")
        print("")
        print("Example usage:")
        print("")
        print("gitbackup -zip -verbose /files/gitrepos /backup/gitrepos")
