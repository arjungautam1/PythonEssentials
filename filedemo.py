from pathlib import Path

fle = Path('/Users/arjuncodes/Desktop/data1.py')
if fle.exists():
    print("File already exists")
else:
    fle.touch(exist_ok=True)
    print("File created success.")
    
