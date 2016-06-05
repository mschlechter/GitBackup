class MointPoint:
    
    def __init__(self, directory: str):
        self.directory = directory
        
    def do_mount(self) -> bool:
        return False
        
    def do_unmount(self) -> bool:
        return False
        