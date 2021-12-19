
# check palindrome
mastring = input('give me a string ! :')
def isitrev(strng):
    i = 1 
    for k in strng : 
        if(k==strng[len(strng)-i]): 
            #print(strng[len(strng)-i])
            i+=1
    if(i-1== len(strng)): print('it is a palindrome!')
    else : print('it is not a  palindrome :(')

isitrev(mastring)

#check prime numbr
yournumber = input('give me a number:')
def isitprime (numbr):
    if(numbr>1 and ((numbr-1)%6==0)or((numbr+1)%6==0)): print(numbr,'is a prime number')
    else : print('it is not prime')

isitprime(yournumber)

#range of number
ffrom = input('enter the begining of the range :')
tto = input('enter the end of te range :')
givenrangenumber = input ('enter a number : ')
def isnmbrinrange (f,t,number):
    therange = range(f,t)
    if number in therange : print ('Yes this number is included here ! ')
    else: print('this number is not included !')

isnmbrinrange(int(ffrom),int(tto),int(givenrangenumber))

#factorial of a number 
manumber = input('inter a number :')
def letsmultiply (number):
    a = 1
    n = number
    b = number
    while(n>1):
        a = b*(n-1)
        n = n - 1 
        b = a 
    print(b)

letsmultiply(abs(int(manumber)))

# reverse a string 
norstring = input('enter a string here : ')
def reversestring (strng) : 
    wordlist = strng.split() 
    wordlist.reverse()
    print(' '.join(wordlist))

def reversestring2 (strng) : 
   worldlist = strng[::-1]
   print(worldlist)

reversestring(norstring)
reversestring2(norstring)
#sum numbers in a list 

urnumber = input('enter numbers separeted by a space :')
listofnumbers = []
def sumofnumbers (nmbr) :
    ie = nmbr.split()
    print(ie)

sumofnumbers(urnumber)

# finding the max between 3 numbers 
number3 = input('give me 3 numbers separated by a space :')
newnumber3 = number3.split(' ')
def whatismax(n):
    print(max(n))

whatismax(newnumber3)

