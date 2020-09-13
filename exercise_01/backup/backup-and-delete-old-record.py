##
# Script to copy directory and delete old record (manuel backup and clean)
# cevheri, 20200829
# Written in Python 3.7
###
import datetime
import json
import logging
import os
import shutil
import sys

del_count = 3


# read config (source and target folder)
def read_config():
    try:
        with open("param.json") as config:
            data = json.load(config)
        src = data["source_folder"]
        dest = data["target_folder"]

        global del_count
        del_count = int(data["del_count"])
    except Exception as err:
        logging.error("Read Configuration Error:" + " " + str(type(err)) + ">" + str(err))
        sys.exit()

    add = "\\backup_{}".format(datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S'))
    docopy(src, dest + add)
    del_old_record(dest)


# copy directories (with subdirectories) to a target folder
def docopy(source_folder, target_folder):
    try:
        shutil.copytree(source_folder, target_folder)
        logging.info("Copied :> " + source_folder + " --> " + target_folder)
    except Exception as err:
        logging.error("Copy Error !!! :" + source_folder + " -x-> " + target_folder + " " + err)


# delete old record
def del_old_record(target_folder):
    count = 0
    for dir in sorted(os.listdir(target_folder), reverse=True):
        # if os.path.isdir(dir):
        path = os.path.join(target_folder, dir)
        count += 1
        if count > del_count:
            try:
                shutil.rmtree(path)
                logging.info("Deleted :> " + path)
            except Exception as err:
                logging.error("Delete Error !!! :" + path + " " + err)


if __name__ == '__main__':
    logging.basicConfig(filename='backup.log', level=logging.INFO)
    print('Starting execution')
    read_config()
    print('Ending execution')
