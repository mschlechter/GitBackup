import sys
import platform

from typing import Iterable

# For parsing commandline arguments
class ArgHelper:

    def __init__(self, args: Iterable[str]):
        self.args = args
        self.destination = ""
        self.source = ""
        self.zip = False
        self.verbose = False
        self.mountpoint = None
        self.tar = False

        self.__parse_arguments()

    def __platform_is_windows(self) -> bool:

        current_platform = platform.system()
        return current_platform.startswith("Windows") or current_platform.startswith("CYGWIN_NT")

    def __parse_arguments(self):
        argc = len(self.args)
        if argc < 3:
            self.__print_banner();
            sys.exit(1)
        
        # Set destination and source
        self.destination = self.args[argc-1]
        self.source = self.args[argc-2]

        # Set options
        for i in range(0, argc-2):
            currentarg = self.args[i]

            if currentarg == "-zip":
                self.zip = True

            if currentarg == "-tar":
                if self.__platform_is_windows():
                    print("Tar is not supported on Windows!")
                    sys.exit(1)
                self.tar = True

            if currentarg == "-verbose":
                self.verbose = True

            if currentarg.startswith("-mnt="):
                if self.__platform_is_windows():
                    print("Mount points are not supported on Windows!")
                    sys.exit(1)
                self.mountpoint = currentarg[5:]

    def __print_banner(self):

        print("Correct syntax is:\n")
        print("gitbackup.py <options> SOURCE_DIRECTORY DESTINATION_DIRECTORY")
        print("")
        print("Options can be:")
        print("-mnt=PATH   Mount and unmount PATH")
        print("-zip        Create zip archives")
        print("-tar        Create tar.gz archives")
        print("-verbose    Show git output")
        print("")
        print("Example usage:")
        print("")
        print("gitbackup.py -mnt=/backup -zip -verbose /files/gitrepos /backup/gitrepos")
