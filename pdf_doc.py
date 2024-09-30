import os
import sys
import pathlib
from pdf2docx import Converter


def get_path(pth=""):
    start = "user path here"

    for dirpath, dirnames, filenames in os.walk(start):
        for dirname in dirnames:
            if dirname == pth:
                dirname = os.path.join(dirpath, dirname)
                print(dirname)
                return dirname
            
def get_files(directory):
    res=[]
    res2=[]
    for x in os.listdir(directory):
        if x.endswith('.pdf'):
            res.append(os.path.join(directory, x))
            res2.append(x[:-4])

    return res, res2



def main(args: list[str]):
    dirs = []

    for pth in args[1::]:
        dirs.append(get_path(pth))
    
    if not dirs:
        print('no directories found')
        exit(-1)

    for dir in dirs:
        if not dir:
            print('directory not found')
            continue

        new_dir = pathlib.Path(dir, 'pdf_to_doc')
        new_dir.mkdir(parents=True, exist_ok=True)
        files, filenames = get_files(dir)

        if not files:
            print('no odc files in this directory')
            continue
        i=0
        print(files)
        for file in files:
            cv = Converter(file)
            cv.convert(f'{new_dir}\\{filenames[i]}.docx', start=0, end=None)
            cv.close()
            i+=1
            if i >= len(files):
                break

main(sys.argv)