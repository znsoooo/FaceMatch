import os
import random

folder = 'imgs'
files = os.listdir(folder)
length = len(str(len(files)))
random.shuffle(files)
for old_name in files:
    os.rename(f'{folder}/{old_name}', f'{folder}/{old_name}.tmp')
for n, old_name in enumerate(files, 1):
    ext = os.path.splitext(old_name)[1]
    new_name = str(n).zfill(length) + ext
    os.rename(f'{folder}/{old_name}.tmp', f'{folder}/{new_name}')
