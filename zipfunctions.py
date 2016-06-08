import os
import zipfile

# Add directory to zip file
def add_dir_to_zip(zip_dir: str, zip_file: zipfile.ZipFile):
    for root, dirs, files in os.walk(zip_dir):
        for file in files:
            absfilename = os.path.join(root, file)
            arcname = os.path.relpath(absfilename, zip_dir)
            zip_file.write(absfilename, arcname)
        for dir in dirs:
            absfilename = os.path.join(root, dir)
            arcname = os.path.relpath(absfilename, zip_dir)
            zip_file.write(absfilename, arcname)

# Create new zip file for directory
def create_zip(filename: str, archive_dir: str):
    zip_file = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    add_dir_to_zip(archive_dir, zip_file)
    zip_file.close()
