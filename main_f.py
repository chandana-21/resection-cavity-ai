import os, shutil

dir_name1 = os.path.join(os.getcwd(), 'dataset/MRI_US_Brain/RESECT/NIFTI')
dir_name2 = os.path.join(os.getcwd(), 'dataset/main')



#for folder1, folder2 in zip(sorted(os.listdir(dir_name1)), sorted(os.listdir(dir_name2))):
files = os.listdir(dir_name1) #os.listdir(os.path.join(dir_name1, folder1)) #
for file in files:
  # print(file)
  if file.startswith('Case'):

    # os.mkdir(os.path.join(dir_name2, f'{file}'))

# for i, file in enumerate(files):
    shutil.copy(os.path.join(dir_name1, f'{file}/US/{file}-US-after.nii.gz'), os.path.join(dir_name2 , f'{file}-US-after.nii.gz'))

