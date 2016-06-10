#!/usr/bin/env python3
#
# Script to backup all git repositories in a given source directory.

import sys
import os
import shutil

from arghelper import ArgHelper
from githelper import GitHelper
from mountpoint import MountPoint

print ("Git Backup - by M. Schlechter\n")

ah = ArgHelper(sys.argv)
gh = GitHelper(ah)
 
print("Source directory      : " + gh.source_dir)
print("Destination directory : " + gh.destination_dir)
print("Temporary directory   : " + gh.temp_dir)
print("Create zip archives   : " + str(gh.zip))
print("Create tar archives   : " + str(gh.tar))
print("Verbose               : " + str(gh.verbose))

if gh.mountpoint:
    print("Temporary mountpoint  : " + gh.mountpoint)

gh.clone_repositories()
