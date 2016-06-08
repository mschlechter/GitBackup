import os
import zipfile

def _zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            absfilename = os.path.join(root, file)
            arcname = os.path.relpath(absfilename, path)
            #print(absfilename + " - " + arcname)
            ziph.write(absfilename, arcname)

def create_zip(filename, archive_dir):
    zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    _zipdir(archive_dir, zipf)
    zipf.close()
