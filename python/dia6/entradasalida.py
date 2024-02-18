
'''
mi_archivo= open('prueba.txt')

print(mi_archivo.read()) #method read allows me to read and print the content to console



print(mi_archivo.readline()) #method to read the first line
#To read next lines you can use the consecutives readlines methods
print(mi_archivo.readline())
print(mi_archivo.readline())
#each line has a line break in the txt file
rstrip allows to remove the break

lines_list=mi_archivo.readlines()
print(lines_list)
'''

#mi_archivo=open('prueba.txt','r')
#mi_archivo=mi_archivo.write('Soy el nuevo texto') #Raises an error as 'r' doesnt allow writing

mi_archivo=open('prueba.txt','w')
mi_archivo.write('Soy el nuevo texto\n') #line breaks are not included with .write. If writing multiple lines make sure to include it
mi_archivo.write('Esta es la segunda linea\n')  
mi_archivo.writelines(['list','from','write','lines']) #This method takes strings in a list and writes them in a line continuosly
mi_archivo.writelines(['list\n','from\n','write\n','lines\n']) #line breakers can be added for conviniece
mi_archivo=open('prueba.txt') #After .write file needs to be reopen for updates
print(mi_archivo.read()) #line breakers can be added for conviniece

mi_archivo.close() #Use always that you call the open method

mi_archivo=open('prueba.txt','a') #the a parameter allows to add lines to the existing text
mi_archivo.write('Este texto fue incluido usando el parametro a en el metodo open')
mi_archivo=open('prueba.txt')
print(mi_archivo.read())
mi_archivo.close()







