# to make sure both exceptions are excuted i added another variable 
try:
  a =  12.5
  b = 12
  s = "hello"
  print(a+s+b)

except TypeError : 
    if (type(b) == int or type(a) == int):
        a = str(a)
        b = str(b)
        print(a+s+b)
    else :
      print(a,s,b)
# or another shorter way
try:
  o = 12
  i = "hello"
  print(i+o)

except TypeError : 
    if (type(o) != str ):
        o = str(o)
        print(i,o) # print(i+o)
 



