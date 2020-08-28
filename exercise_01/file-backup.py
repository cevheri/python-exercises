##
# Script to copy files and compress them and put them in a separate location
# Amit Sengupta, Sep 2015, HYD
# Written in Python 2.7
###

import os
import zipfile
import shutil


# copy files and folder and compress into a zip file
def doprocess(source_folder, target_zip):
    zipf = zipfile.ZipFile(target_zip, "w")
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            print
            os.path.join(subdir, file)
            zipf.write(os.path.join(subdir, file))

    print("Created ", target_zip)


# copy files to a target folder
def docopy(source_folder, target_folder):
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            print
            os.path.join(subdir, file)
            shutil.copy2(os.path.join(subdir, file), target_folder)


if __name__ == '__main__':
    print('Starting execution')

    # compress to zip
    source_folder = 'D:\\projects\\dummydata'
    target_zip = 'e:\\backups\\dummydata.zip'
    doprocess(source_folder, target_zip)

    # copy to backup folder
    source_folder = 'D:\\data\\mp3files'
    target_folder = 'e:\\backups\\mp3backup'
    docopy(source_folder, target_folder)

    print('Ending execution')
