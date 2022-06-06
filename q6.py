x=int(input("enter the starting integer of range")) 
y=int(input("enter the ending integer of range")) 
for i in range(x,y+1): 
     z=True 
     for j in range(2,i): 

       if i%j==0:
           z=False 
           break 
     if z==True: 
       print(i) 

