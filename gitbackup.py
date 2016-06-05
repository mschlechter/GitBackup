#!/usr/bin/env python
#
# Simple script to backup all git repositories in a given
# source directory.
#
# TODO:
# Error handling
# Silent git execution
# Better arg parsing
# Support for mountpoints (allowing CIFS destination)
#   Make sure can mount /mnt/backup easily in Linux with multiple users
#   (/etc/fstab) and let this script just mount the mountpoint and check it

import sys
import os
import shutil

# Get immediate subdirectories which name ends with .git
def get_git_subdirectories(parent_dir):
    return sorted([
        name for name in os.listdir(parent_dir)
        if os.path.isdir(os.path.join(parent_dir, name))
        and name.endswith(".git")
    ])

# Create a bare git clone in the destination
def create_git_clone(parent_dir, git_dir, dest_dir):
    dest_git_dir = os.path.join(dest_dir, git_dir)
    if os.path.exists(dest_git_dir):
        print "Removing " + dest_git_dir
        shutil.rmtree(dest_git_dir)
    print "Creating clone for " + git_dir
    # git clone --bare parent_dir+git_dir
    cmd = "git clone --bare " + os.path.join(parent_dir, git_dir)
    os.system(cmd)

print "Git Backup 0.1 - by M. Schlechter\n"

if len(sys.argv) != 3:
    print "Correct syntax is:\n"
    print "gitbackup SOURCE_DIRECTORY DESTINATION_DIRECTORY"
    sys.exit(1)

cur_dir = os.path.abspath(os.path.curdir)

source_dir = os.path.join(cur_dir, sys.argv[1])
dest_dir = os.path.join(cur_dir, sys.argv[2])
 
print "Source directory      : " + source_dir
print "Destination directory : " + dest_dir

if not os.path.exists(source_dir):
    print "\nERROR : Source directory does not exist!"
    sys.exit(1)

if not os.path.exists(dest_dir):
    print "\nERROR : Destination directory does not exist!"
    sys.exit(1)

print "\nCreating bare git clones...\n"

git_directories = get_git_subdirectories(source_dir)

os.chdir(dest_dir)

for git_dir in git_directories:
    create_git_clone(source_dir, git_dir, dest_dir)

os.chdir(cur_dir)
