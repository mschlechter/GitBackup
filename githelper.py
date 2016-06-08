import sys
import os
import shutil
import subprocess
import tempfile
import zipfile

import arghelper
import zipfunctions
import mountpoint

class GitHelper:
    
    # Source and destination directory are required
    def __init__(self, ah: arghelper.ArgHelper):
        self.cur_dir = os.path.abspath(os.path.curdir)
        self.source_dir = os.path.realpath(ah.source)
        self.destination_dir = os.path.realpath(ah.destination)
        self.temp_dir = tempfile.mkdtemp()

        self.zip = ah.zip
        self.verbose = ah.verbose
        self.mountpoint = ah.mountpoint
    
    # Get immediate subdirectories which name ends with .git
    def __get_git_subdirectories(self):
        return sorted([
            name for name in os.listdir(self.source_dir)
            if os.path.isdir(os.path.join(self.source_dir, name))
            and name.endswith(".git")
        ])
            
    # Handle access errors (on Windows platform) 
    def __handle_rmtree_error(self, func, path, exc_info):
        import stat
        if not os.access(path, os.W_OK):
            # Is the error an access error ?
            os.chmod(path, stat.S_IWUSR)
            func(path)
        else:
            raise

    # Create a bare git clone in the destination
    def __create_git_clone(self, git_dir: str) -> bool:
        temp_git_dir = os.path.join(self.temp_dir, git_dir)
        args = ["git", "clone", "--bare", os.path.join(self.source_dir, git_dir)]
        return subprocess.call(args) == 0

    # Check if directories exist
    def __check_directories(self):
        
        if not os.path.exists(self.source_dir):
            print ("\nERROR : Source directory does not exist!")
            sys.exit(1)

        if not os.path.exists(self.destination_dir):
            print ("\nERROR : Destination directory does not exist!")
            sys.exit(1)
    
        if self.mountpoint and not os.path.exists(self.mountpoint):
            print ("\nERROR : Mountpoint does not exist!")
            sys.exit(1)

    # Clone all git repositories from the source directory
    def clone_repositories(self):
        
        self.__check_directories()

        mount_point = None

        # Mount
        if self.mountpoint:
            mount_point = mountpoint.MountPoint(self.mountpoint)
            mount_point.do_mount()

        print ("\nCreating bare git clones...\n")

        git_directories = self.__get_git_subdirectories()

        # Work from temp dir
        os.chdir(self.temp_dir)

        for git_dir in git_directories:
            temp_git_dir = os.path.join(self.temp_dir, git_dir)
            dest_git_dir = os.path.join(self.destination_dir, git_dir)

            print("Creating clone for " + git_dir)
            print("Cloning into " + temp_git_dir)

            if not self.__create_git_clone(git_dir):
                sys.exit(1) # Cloning failed
            
            # Clean target dir
            if os.path.exists(dest_git_dir):
                print("Removing " + dest_git_dir)
                shutil.rmtree(dest_git_dir, onerror=self.__handle_rmtree_error)

            if self.zip:
                # Create zip archive
                zipfile = dest_git_dir + ".zip"
                print("Create zip archive " + zipfile)
                zipfunctions.create_zip(zipfile, temp_git_dir)
            else:
                # Copy to target
                print("Copying into " + dest_git_dir)
                shutil.copytree(temp_git_dir, dest_git_dir)

        # Change back to current dir
        os.chdir(self.cur_dir)

        # Remove temp dir
        print ("Removing " + self.temp_dir)
        shutil.rmtree(self.temp_dir, onerror=self.__handle_rmtree_error)

        # Unmount
        if self.mountpoint:
            mount_point.do_unmount()

        
        