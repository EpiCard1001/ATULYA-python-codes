def orderlist(a,b):
 
 if b=="asc" :
  for i in range (0,len(a)): 
   for j in range(i,len(a)): 
     if a[i]>a[j] : 
       x=a[j]
       a[j]=a[i] 
       a[i]=x 
 if b=="desc" : 
    for i in range (0,len(a)): 
      for j in range(i,len(a)): 
          if a[i]<a[j] : 
             x=a[j]
             a[j]=a[i]
             a[i]=x 
 return a            
list=[1,24,435,21,364,123,4563,123,123,2] 
print(orderlist(list,"desc"))



