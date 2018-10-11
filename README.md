# plagFinder
A python program to automate the plagiarism check for java code, expects a zip archive in and extract all files and then run jplag on that directory.

# HOW TO RUN
Dependencies to download:
* Java ( To run the Jplag.jar )
* Python 3.x
* Pip 3 (if not downloaded with the python 3.x)

Example: download zip archive of submissions from moodle.

Clone this repository to your computer with:

``` $ git clone https://github.com/xoften/plagFinder.git ```

Then move to the cloned directory and run the requirment.txt to let python download any required modules.

``` 
$ cd /plagFinder 
$ pip3 install -r requirments.txt
```

After that, you have everything for running the application.
So run the application.


``` $ python3 plag_finder.py ```

This will open a dialogue box where you should choose the downloaded zip archive from moodle.
After this, the application starts extracting the java files and then checking them with jplag

The result from Jplag will be found under /result in the same folder that the python program is located at.

You can then open the /result/index.html to see the result from the scan.

In index.html you can see the similarities between the different codes, and it will also show how similar files are between different authors. 

To the see the code and to see what Jplag has found you click on one of the samples and it will colour code the similarities it found. 
