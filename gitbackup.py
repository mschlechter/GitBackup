#!/usr/bin/env python3
#
# Simple script to backup all git repositories in a given
# source directory.
#
# TODO:
# Silent git execution
# Support for mountpoints (allowing CIFS destination)
#   Make sure can mount /mnt/backup easily in Linux with multiple users
#   (/etc/fstab) and let this script just mount the mountpoint and check it

import sys
import os
import shutil

from arghelper import ArgHelper
from githelper import GitHelper
from mountpoint import MountPoint

# test mountpoint class 
# mp = MountPoint("/mnt/backup")
# r = mp.do_mount()
# if r:
#     print ("mount success")
# else:
#     print ("mount failure")

print ("Git Backup - by M. Schlechter\n")

ah = ArgHelper(sys.argv)
gh = GitHelper(ah.source, ah.destination, ah.zip, ah.verbose)
 
print("Source directory      : " + gh.source_dir)
print("Destination directory : " + gh.destination_dir)
print("Temporary directory   : " + gh.temp_dir)
print("Create zip archives   : " + str(gh.zip))
print("Verbose               : " + str(gh.verbose))

gh.clone_repositories()
