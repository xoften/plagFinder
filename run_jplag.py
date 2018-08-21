import subprocess
import os

JPLAG_FILEPATH = os.path.dirname(__file__) + "\jplag.jar"
def run_jplag(submission_directory):
    comparison_directory = input("Input filepath to comparison directory (example compare this submission to other years) "
                                 "\n to only compare this submission just press enter!: ")

    if len(comparison_directory) == 0:
        subprocess.run(['java', '-jar', JPLAG_FILEPATH, '-l', 'java17', '-s', submission_directory])
    else:
        subprocess.call(['java', '-jar', JPLAG_FILEPATH, '-l', 'java17', '-s', '-c',
                         comparison_directory, submission_directory])

    print("done")