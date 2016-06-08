# GitBackup

Script to backup all bare git repositories in a given source directory. The
script searches for immediate subdirectories which name ends with ".git" and
clones them into a destination directory.

Example usage:

    gitbackup.py -zip /files/gitrepos /backup/gitrepos

This will clone all bare repositories in /files/gitrepos to a temporary working
directory and then create zipfiles in /backup/gitrepos.

It's also possible to use a mount point on Linux (defined in /etc/fstab) to
temporarily mount a backup share from another server.

The script works fine on Windows too, but without the mount point support.
