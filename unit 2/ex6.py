import numpy as n 
from numpy.linalg import norm
import copy
import PIL as p
from PIL import Image 



theImage = p.Image.open('fr.png')
arrayfi = n.asarray(theImage)
arrayfiT = arrayfi.T
# the array is too big to be a matrix so instead i will take just a part of it 
Matrixfi = arrayfi[9][4:8]
MatrixfiT = Matrixfi.T

# check if tha matrix is diagonal / identity / triangular(lower/upper)

def typeOfMatrix (mtrx):
    
    i = mtrx.shape
    if((n.zeros((i[0],i[1]),float) == mtrx).all()):
            print('this is a zero matix')
    elif((i[0]==mtrx.shape[1])) :
        identitym = n.identity(i[0])
        clone = copy.copy(mtrx)
        clone[n.diag_indices_from(clone)]= 0
        if((mtrx==identitym).all()):
            print('this is an identity matrix')
        elif((clone==n.zeros((i[0],i[1]),float)).all()):
          print('this is a diagonal matrix')         
        elif(i[0]==i[1]):
            trueHolder = []
            listofindex = list(range(1,i[0])) 
            for l in listofindex :
                k = l-1
                while(k>=0):
                    if(n.asarray(mtrx)[l][k]==0): 
                        k = k - 1 
                        trueHolder.append(True)
                    else : 
                        k = k - 1
                        trueHolder.append(False) 
            if(all(element == True for element in trueHolder)):
                print('this is a lower triangular matrix')       
            else :
              trueHolder = []
              listofindex = list(range(0,i[0]))
              for l in listofindex :
                   k = l + 1 
                   while( k < i[0]):
                       if(n.asarray(mtrx)[l][k]==0): 
                           k = k + 1 
                           trueHolder.append(True)
                       else : 
                            k = k + 1
                            trueHolder.append(False) 
              if(all(element == True for element in trueHolder)):
                  print('this is an upper triangular matrix')        
              else : 
                  print('just an ordinary matrix')
    else:
        print('just an ordinary matrix .')

typeOfMatrix(Matrixfi)

# norms 
vec = n.array([4,0,8])
l1 = norm(vec,1)
l2 = norm(vec)
print(l1,l2)
