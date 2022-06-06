x=["NORTH" , "SOUTH", "SOUTH" , "EAST", "WEST" , "NORTH", "WEST"]

n=[]
for i in range(0,len(x)):
 for j in range(i+1,len(x)):

   if x[i]=="NORTH" and x[j]=="SOUTH":
     x[i]=0
     x[j]=0
 for j in range(i+1,len(x)):
     if x[i]=="SOUTH" and x[j]=="NORTH":
      x[i]=0
      x[j]=0
 for j in range(i+1,len(x)):
     if x[i]=="EAST" and x[j]=="WEST":
      x[i]=0
      x[j]=0     
 for j in range(i+1,len(x)):
     if x[i]=="WEST" and x[j]=="EAST":
      x[i]=0
      x[j]=0
for i in x:
    if i!=0:
        n=n+[i]
print(n)              
 

 

