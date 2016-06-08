#!/usr/bin/env python3
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
# Archive option which creates a zip file (and removes the target repository again)
# Use:

# import os
# import zipfile

# def zipdir(path, ziph):
#     # ziph is zipfile handle
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             ziph.write(os.path.join(root, file))

# if __name__ == '__main__':
#     zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
#     zipdir('tmp/', zipf)
#     zipf.close()

import sys
import os
import shutil

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

if len(sys.argv) != 3:
    print ("Correct syntax is:\n")
    print ("gitbackup SOURCE_DIRECTORY DESTINATION_DIRECTORY")
    sys.exit(1)

gh = GitHelper(sys.argv[1], sys.argv[2])
 
print ("Source directory      : " + gh.source_dir)
print ("Destination directory : " + gh.destination_dir)

gh.clone_repositories()
