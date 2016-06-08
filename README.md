# GitBackup

Script to backup all bare git repositories in a given source directory. The
script searches for immediate subdirectories which name ends with ".git" and
creates a backup in the destination directory.

Example usage:

    python gitbackup.py /files/gitrepos /backup/gitrepos

This will clone all bare repositories in /files/gitrepos to a temporary working
directory and then copy the clones to /backup/gitrepos.

    python gitbackup.py -zip /files/gitrepos /backup/gitrepos

This will clone all bare repositories in /files/gitrepos to a temporary working
directory and then create zipfiles in /backup/gitrepos.

It's also possible to use a mount point on Linux (defined in /etc/fstab) to
temporarily mount a backup share from another server.

    python gitbackup.py -mnt=/mnt/backup -zip /files/gitrepos /mnt/backup/gitrepos

This will first mount /mnt/backup, then clone all bare repositories in 
/files/gitrepos to a temporary working directory, then create zipfiles 
in /mnt/backup/gitrepos and finally unmount /mnt/backup again.

The script works fine on Windows too, but without the mount point support.
