import os
import decompress_files
import run_jplag



def __main__():
    print("hi")
    relative_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"."))
    print(relative_dir)
    filename = input("Input absolute path of downloaded zip archive from moodle: ")
    print(filename)
    assignment_directory = decompress_files.decompress_one(filename, relative_dir)
    decompress_files.decompress_assignments(assignment_directory)


__main__()