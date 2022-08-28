import os, shutil

dir_name1 = os.path.join(os.getcwd(), 'dataset/US_MASKS/RESECT_segmentation')
dir_name2 = os.path.join(os.getcwd(), 'dataset/masks')



#for folder1, folder2 in zip(sorted(os.listdir(dir_name1)), sorted(os.listdir(dir_name2))):
files = os.listdir(dir_name1) #os.listdir(os.path.join(dir_name1, folder1)) #
for file in files:
  # print(file)
  if file.startswith('Case'):

    # os.mkdir(os.path.join(dir_name2, f'{file}'))

# for i, file in enumerate(files):
    shutil.copy(os.path.join(dir_name1, f'{file}/{file}-US-after-resection.nii.gz'), os.path.join(dir_name2 , f'{file}-US-after.nii.gz'))

