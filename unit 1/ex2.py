# read & write 
from os import remove


file = open('./student_names.txt')
stnames = file.read()
print(stnames)
file = open('./student_names.txt','w')
namelist = ['name1','name2','name3','name4','name5']
for i in namelist:
 stnames = stnames + (i+'\n')
file.write(stnames)

# last & first line 
file = open('./student_names.txt')
print(file.readline())
print(file.readlines()[-1])

# checkes the name x 
if 'x' in stnames : print('true')

# generate 26 text file
for i in range(65,91):
    newfile = open(chr(i)+'.txt','x')
