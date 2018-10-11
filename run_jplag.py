import subprocess
import os


def run_jplag(submission_directory):
    JPLAG_FILEPATH = os.path.join(os.path.dirname(__file__), "jplag.jar")

    #Runing Jplag as a subprocess with no output (stdout adn error = DEVNULL)
    subprocess.call(['java', '-jar', JPLAG_FILEPATH, '-l', 'java17', '-s',
                     submission_directory], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
