#!/usr/bin/python
import os
import shutil
import random
import os.path

src_dir = '/config/data/pictures/from'
target_dir = '/config/data/pictures/to/1.jpg'
src_files = (os.listdir(src_dir))
def valid_path(dir_path, filename):
    full_path = os.path.join(dir_path, filename)
    return os.path.isfile(full_path)
files = [os.path.join(src_dir, f) for f in src_files if valid_path(src_dir, f)]
choices = random.sample(files, 1)
for files in choices:
    shutil.copy(files, target_dir)