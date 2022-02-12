import pathlib

myfile = pathlib.Path('/Users/arjuncodes/Desktop/demo.py')
myfile.touch(exist_ok=True)
f = open(myfile)