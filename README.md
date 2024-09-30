# pdftodoc-doctopdf
Scripts that help to batch convert pdf files to docx and the other way around


# There are a few a steps before using the batch files:

1. clone the repository (on command prompt: git clone https://github.com/Omarb2001/pdftodoc-doctopdf.git).
2. download all of the dependencies (in repository directory command prompt: pip freeze > requirements.txt).
3. on the .bat files, replace the placeholder string paths with their respective absolute paths as prompted.
4. To be able to run the .bat files from any directory on the command line, move the .bat files to C:\\Users\\<enter your user here> path.
5. On line 8 of each .py file, replace the text in the quotes with C:\\Users\\<enter your user here> path
6. Now to run the script:
    a. pdftodoc <name of directory where you want to convert pdfs to docx>
    b. doctopdf <name of directory where you want to convert pdfs to docx>

    The converted folders should be in a new directory under the working directory.