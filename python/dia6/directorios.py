import os


route=os.getcwd() #getcurrent working directory

if route != '/mnt/e/code/python/dia6/alternativo':
    os.chdir('/mnt/e/code/python/dia6/alternativo') #chdir allows to change the working directory
    print(f'current directory changed to {os.getcwd()}')

try: #The os.makedirs() method returns an error if the route already exist
    os.makedirs('./test') #This method creates a directory in the specified route
except:
    pass

route='/mnt/e/code/python/dia6/alternativo/alternativo.txt'
print(f'The route is {route}')
elemento=os.path.basename(route)
directory=os.path.dirname(route)
elements=os.path.split(route)
print(f'Working in the {elemento} file located in the {directory} folder. Reference {elements}')

os.mkdir('./otra') #Creates a folder
print(os.listdir()) #prints the folders
os.rmdir('./otra') #Removes the folder
print(os.listdir())

from pathlib import Path #From the pathlib library we import the Path module
os.chdir('..')
route=Path(os.getcwd()+'/ealternativo') #Object Path allows to create a route from our working folder
print(route)
file=route / 'alternativo.txt'
my_file=open(file)
print(my_file.read())
my_file.close()






