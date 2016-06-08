# GitBackup

Script to backup all bare git repositories in a given source directory. The
script searches for immediate subdirectories which name ends with ".git" and
clones them into a destination directory.

Example usage:

    gitbackup.py -zip /files/gitrepos /backup/gitrepos

This will clone all bare repositories in /files/gitrepos to a temporary working
directory and then create zipfiles in /backup/gitrepos.

![screenshot image](screenshot.png "Screenshot running VsCode on Ubuntu")

TODO:

1. Add mountpoint support. Making it possible to mount a backup share on demand
   and unmount it when the script is done.
2. Improve command arguments parsing and add more options (verbosity, mountpoint,
   etc).
