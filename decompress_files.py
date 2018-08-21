import zipfile
import os
import shutil

#"F:\Downloads\18VT-1DV701-7,5hp-Växjö-50%-Assignment 3 TFTP Server-1755230.zip"

def decompress_one(filename, root_directory):

    save_directory = root_directory + "\\deflated_files\\"
    if os.path.exists(save_directory):
        print(save_directory)
        shutil.rmtree(save_directory)

    os.makedirs(save_directory)

    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall(save_directory)

    return save_directory

def decompress_assignments(assignment_directory):
    for root, dirs, files in os.walk(assignment_directory):
        for file in files:
            if file.endswith(".zip"):
                file_path = os.path.join(root,file)
                with zipfile.ZipFile(file_path, "r") as zip_ref:
                    zip_ref.extractall(root)
                os.remove(file_path)
