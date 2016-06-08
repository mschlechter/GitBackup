import os
import zipfile

# Add directory to zip file
def add_dir_to_zip(path: str, ziphandle: zipfile.ZipFile):
    for root, dirs, files in os.walk(path):
        for file in files:
            absfilename = os.path.join(root, file)
            arcname = os.path.relpath(absfilename, path)
            ziphandle.write(absfilename, arcname)
        for dir in dirs:
            absfilename = os.path.join(root, dir)
            arcname = os.path.relpath(absfilename, path)
            ziphandle.write(absfilename, arcname)

# Create new zip file for directory
def create_zip(filename: str, archive_dir: str):
    zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    add_dir_to_zip(archive_dir, zipf)
    zipf.close()
