import subprocess

# Mount point helper class
class MountPoint:
    
    def __init__(self, directory: str):
        self.directory = directory
        
    def do_mount(self) -> bool:
        result = subprocess.call(["mount", self.directory])
        return result == 0
        
    def do_unmount(self) -> bool:
        result = subprocess.call(["unmount", self.directory])
        return result == 0

        