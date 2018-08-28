import os
import decompress_files
import run_jplag
from tkinter import filedialog


def __main__():
    print("hi")
    relative_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
    print(relative_dir)
    filename = filedialog.askopenfilename(title="Select zipped submission file "
                                                "downloaded from moodle",
                                          filetypes=(("zip files", "*.zip"),
                                                     ("all files", "*.*")))
    print(filename)
    assignment_directory = decompress_files.decompress_one(filename, relative_dir)

    decompress_files.decompress_assignments(assignment_directory)
    print(assignment_directory)
    run_jplag.run_jplag(assignment_directory)


__main__()
