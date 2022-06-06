import random
n=[]

for i in range(0,4):
  n= n+ [chr(random.randint(ord('a'), ord('z')))]

for i in range(0,10):
  l=[]
  p=str(input(" guess key:"))
  for j in p:
    if j not in n:
         print("B")
         break
    elif j in n:
      l=l+[j]
  if l==n:
   print("R")
   break
  elif len(l)==len(n):
      print("Y")