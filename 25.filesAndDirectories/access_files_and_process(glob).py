
from pathlib import Path

# Create a path oject from Path class to reference a directory from our computer, with or withot an argument
# Path() means pwd
path = Path('../')

'''
use glob with a search pattern to access the files in a specified dir
.glob('*'): To search for all files
.glob('*.*'): To search for all files
.glob('*.xls'): To search for all excell files
.glob('*.csv'): To search for all csv files
.glob('*.py'): To search for all python files
'''

# print(path.exists())
for file in path.glob('*.*'): #path.glob will output a generator object which will loop over
    print(file)
