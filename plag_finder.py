import os
import decompress_files
import run_jplag

def __main__():
    print("hi")
    relative_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    print(relative_dir)