import subprocess
import os

JPLAG_FILEPATH = os.path.dirname(__file__) + "\jplag.jar"
def run_jplag(submission_directory):

    subprocess.call(['java', '-jar', JPLAG_FILEPATH, '-l', 'java17', '-s',
                     submission_directory], stderr=subprocess.DEVNULL)
