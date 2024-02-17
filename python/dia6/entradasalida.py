
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
mi_archivo.write('Soy el nuevo texto') 
print(mi_archivo.read())




mi_archivo.close() #Use always that you call the open method



