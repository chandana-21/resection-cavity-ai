from genericpath import exists
import os, shutil

PATH = os.path.join(os.getcwd(), 'MaskImages')

files = os.listdir(PATH)

# for f in files:
#     if not os.path.exists(os.path.join(PATH, f.split('-')[0])):
#         os.mkdir(os.path.join(PATH , f.split('-')[0]))


for f in files:
    if f.endswith('jpg'):
        #shutil.copy(os.path.join(PATH, f), os.path.join(PATH , f.split('-')[0]))
        os.remove(os.path.join(PATH, f))

