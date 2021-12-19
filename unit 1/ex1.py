mylist = []
issquared = []
for x in range(1,299):
  if x % 2 == 0: 
    mylist.append(x)
for el in mylist :
 issquared.append(el*el)

print(len(mylist) , *issquared,sep = '-')

if 57 in mylist : print('yes') 






