import subprocess

# Mount point helper class
class MountPoint:
    
    def __init__(self, directory):
        self.directory = directory
        
    def do_mount(self):
        result = subprocess.call(["mount", self.directory])
        return result == 0
        
    def do_unmount(self):
        result = subprocess.call(["unmount", self.directory])
        return result == 0

        