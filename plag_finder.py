import sys
import os
import decompress_files
import run_jplag
import time
import tkinter
from tkinter import filedialog


def __main__():
    relative_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))

    root = tkinter.Tk()
    filename = filedialog.askopenfilename(initialdir = "/",
                title="Select zipped submission file downloaded from moodle",
                filetypes=(("zip files", "*.zip"), ("all files", "*.*")))
    if not filename:
        print("No file chosen, exiting...")
        sys.exit(1)

    root.destroy()
    assignment_directory = decompress_files.decompress_one(filename, relative_dir)

    failed = decompress_files.decompress_assignments(assignment_directory)

    run_jplag.run_jplag(assignment_directory)

    #os.system('cls' if os.name == 'nt' else 'clear')
    print("Plagirsm check done!\n"
        "Results can be found inside index.html in the result folder\n"
        "Application failed to open %d number of archives" % failed )


__main__()
