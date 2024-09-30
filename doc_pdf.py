import os
import sys
import pathlib
from docx2pdf import convert


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
        if x.endswith('.docx'):
            res.append(os.path.join(directory, x))
            res2.append(x[:-5])

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

        new_dir = pathlib.Path(dir, 'doc_to_pdf')
        new_dir.mkdir(parents=True, exist_ok=True)
        files, filenames = get_files(dir)

        if not files:
            print('no odc files in this directory')
            continue
        i=0
        print(files)
        for file in files:
            print(f'{new_dir}\\{filenames[i]}.pdf')
            convert(file,f'{new_dir}\\{filenames[i]}.pdf')
            i+=1
            if i >= len(files):
                break

main(sys.argv)