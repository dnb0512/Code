import os
from pathlib import Path

folder=Path(os.getcwd()+'/prueba.txt') #Path creation to the file folder route

print(folder.read_text()) #Method .read_text allows to read the file conten easily 
#When using pathlib there is no need to close the file

print(folder.name) #This function returns the name of the file open
print(folder.suffix) #This funtion returns the name of the file extension
print(folder.stem) #Returns the file name without the extension

if not folder.exists():
    print('File does not exist')
else:
    print('File in folder')

from pathlib import PureWindowsPath 
windows_route=PureWindowsPath(folder)
print(f'Windows route is {windows_route}')