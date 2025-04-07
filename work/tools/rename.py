import os

folder_path = '/home/aistudio/dog_view_all/labels'

files = os.listdir(folder_path)

for filename in files:
    if ' ' in filename:
        new_filename = filename.replace(' ', '_')
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(old_file_path, '->', new_file_path)
