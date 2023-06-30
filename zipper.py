import os
import shutil

folder_path: str = input("Enter the path of the folder to be ziped : ")
destination_path: str = input("Enter the destination path for the zip file : ")

zip_file = shutil.make_archive(destination_path, "zip", folder_path)

if os.path.exists(destination_path+".zip"):
    print(zip_file)
else:
    print("Failed to create zip file.")