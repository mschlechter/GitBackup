import os
import shutil
import subprocess

class GitHelper:
    
    # Source and destination directory are required
    def __init__(self, source_dir: str, destination_dir: str):
        self.cur_dir = os.path.abspath(os.path.curdir)
        self.source_dir = os.path.realpath(source_dir)
        self.destination_dir = os.path.realpath(destination_dir)
    
    # Get immediate subdirectories which name ends with .git
    def get_git_subdirectories(self):
        return sorted([
            name for name in os.listdir(self.source_dir)
            if os.path.isdir(os.path.join(self.source_dir, name))
            and name.endswith(".git")
        ])
        
    # Create a bare git clone in the destination
    def create_git_clone(self, git_dir: str) -> bool:
        dest_git_dir = os.path.join(self.destination_dir, git_dir)
        if os.path.exists(dest_git_dir):
            print ("Removing " + dest_git_dir)
            shutil.rmtree(dest_git_dir)
        print ("Creating clone for " + git_dir)
        # git clone --bare parent_dir+git_dir
        args = ["git", "clone", "--bare", os.path.join(self.source_dir, git_dir)]
        return subprocess.call(args) == 0

    # Clone all git repositories from the source directory
    def clone_repositories(self):
        
        git_directories = self.get_git_subdirectories()

        os.chdir(self.destination_dir)

        for git_dir in git_directories:
            if not self.create_git_clone(git_dir):
                sys.exit(1) # Cloning failed

        os.chdir(self.cur_dir)

        
        