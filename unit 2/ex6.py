import numpy as n 
from numpy.linalg import norm
import copy
import PIL as p
from PIL import Image 



theImage = p.Image.open('fr.png')
arrayfi = n.asarray(theImage)
##create the transpose of this array
arrayfiT = arrayfi.T
# the array is too big to be a matrix so instead i will take just a part of it , 17*48 image you can check it in the folder named unit 2 
Matrixfi = arrayfi[9][4:8]
#create the transpose of this matrix 
MatrixfiT = Matrixfi.T

# check if tha matrix is diagonal / identity / triangular(lower/upper)

def typeOfMatrix (mtrx):
    
    i = mtrx.shape
    # create a zero matrix with he same n of rows and columns as the input and comparing them
    if((n.zeros((i[0],i[1]),float) == mtrx).all()):
            print('this is a zero matix')
    elif((i[0]==mtrx.shape[1])) :
        identitym = n.identity(i[0])
        clone = copy.copy(mtrx)
        clone[n.diag_indices_from(clone)]= 0
     # create an identity matrix with he same n of rows and columns as the input and comparing them
        if((mtrx==identitym).all()):
            print('this is an identity matrix')
        elif((clone==n.zeros((i[0],i[1]),float)).all()):
      # create a clone of the input but the diagonal numbers are zeros and comparing it with  zero matrix with he same n of rows and columns as the input
    # if true that means that the input matrix numbers are all zeroes except the diagonal , it can not be null because we already checked that
          print('this is a diagonal matrix')         
        elif(i[0]==i[1]):
            trueHolder = []
            listofindex = list(range(1,i[0])) 
            # checking each row starting from the second that is being [1] represented by the variablr l 
            # and  including just the numbers below the diagonal ,that is  being the change in variable k
            # ex : if l=3 than k = 2 , k = 1 , k = 0 // if l = 1 than k = 0 ......ect
            # finally if all the appended values to the list named trueholder are true than this is a lower t m otherwise the execution continue
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
  # the same concept as the lower triangulat matrix 
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
    # if none than this is a normal matrix
    else:
        print('just an ordinary matrix .')

typeOfMatrix(Matrixfi)

# norms 
# a random column vector
vec = n.array([4,0,8])
#calculating the norms
l1 = norm(vec,1)
l2 = norm(vec)
print(l1,l2)
