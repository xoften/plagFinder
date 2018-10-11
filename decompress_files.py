import zipfile
import os
import shutil
import patoolib
import datetime

def decompress_one(filename, root_directory):
    #Gets todays date to add it to the filename to make it easier to see which is which
    today = str(datetime.date.today())

    save_directory = os.path.join(root_directory, "deflated_files_" + today)

    #Sees if the directory already exits and the deletes it to save room if we do alot of runs
    if os.path.exists(save_directory):
        shutil.rmtree(save_directory)

    os.makedirs(save_directory)

    #Unzips the moodle file and returns the directory name as reference
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall(save_directory)

    return save_directory

def decompress_assignments(assignment_directory):

    #Counts how many of the compressed files that are of unknown file type.
    failed_counter = 0

    #Used as a counter
    file_counter = 0
    max_files = len(os.listdir(assignment_directory))

    #Goes through all the directories and files extract every compressed encounter
    for root, dirs, files in os.walk(assignment_directory):

        for file in files:
            file_counter += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(file_counter , " / ", max_files, " done!")
            print(file)

            if file.endswith(".zip"):
                file_path = os.path.join(root, file)
                with zipfile.ZipFile(file_path, "r") as zip_ref:
                    zip_ref.extractall(root)
                os.remove(file_path)

            elif file.endswith(".rar"):
                file_path = os.path.join(root, file)
                patoolib.extract_archive(file_path, outdir=root)
                os.remove(file_path)

            elif file.endswith(".7z"):
                file_path = os.path.join(root, file)
                patoolib.extract_archive(file_path, outdir=root)
                os.remove(file_path)

            else:
                failed_counter += 1

    return failed_counter
