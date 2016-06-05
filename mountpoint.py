import os

class MountPoint:
    
    def __init__(self, directory):
        self.directory = directory
        
    def do_mount(self):
        cmd = "mount " + self.directory
        return os.system(cmd) == 0
        
    def do_unmount(self):
        cmd = "unmount " + self.directory
        return os.system(cmd) == 0

        