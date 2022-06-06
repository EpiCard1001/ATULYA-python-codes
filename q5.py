def asd(l):
  k=len(l)
  n=[]

  for i in range(0,k):
 
    if l[i] not in n:

       for j in range(i+1,k):
           if l[i]==l[j]:
            n.append(l[i])
            break

  print(n)

l=[1,1,453,4362,123,13,235,63,634,53,523,445,43,74564,2342,5436,2343142,52,
153,5,451,414252,63,6474,73,52,41414,245,445,37,1,37,2424,263,24,37,7]
asd(l)

