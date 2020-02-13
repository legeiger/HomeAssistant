#!/usr/bin/python
import os
import shutil
import random
import os.path

src_dir = '/usr/share/hassio/homeassistant/data/pictures/from'
target_dir = '/usr/share/hassio/homeassistant/data/pictures/to/1.jpg'
src_files = (os.listdir(src_dir))
def valid_path(dir_path, filename):
    full_path = os.path.join(dir_path, filename)
    return os.path.isfile(full_path)
files = [os.path.join(src_dir, f) for f in src_files if valid_path(src_dir, f)]
choices = random.sample(files, 1)
for files in choices:
    shutil.copy(files, target_dir)
    
# This file takes a random file from "src_dir" and copies it to "target_dir"
# When it copies, it renames the file to 1.jpg as that is the filename the morning briefing automation is looking for
