from pathlib import Path

base=Path.home() #method returns the users home folder route
guide=Path('Barcelona','Sagrada_flia') #method creates a relative route using the input strings
print(base)
print(guide)

guide_two=Path(base,'Europa','Espana',Path('Barcelona','Sagrada_familia.txt')) #Path constructor allows Path objects itself
print(guide_two)

guide_three=guide_two.with_name('La_pedrera.txt')
print(guide_three)

print(guide_three.parent) #parent function allows to acces the file route
print(guide_three.parent.parent) #parent can be stack and will return a higher level each time

home=Path.cwd() #.cwd is the current working directory

guide=Path(home,'europa')
for txt in guide.glob('**/*.txt'): #.glob method allows to iterate inside a path and returns the paths for all matching the input condition
    print(txt)

guide=Path('Europa','Espana','Barcelona','Sagrada_Familia.txt')
in_europe= guide.relative_to(Path('Europa'))
in_spain= guide.relative_to(Path('Europa','Espana'))
print(in_europe)
print(in_spain)
