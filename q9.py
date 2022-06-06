
x="abcdojfer"

k=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l=[]
for i in range(0,len(x)):
    for j in range(0,len(k)):
        if x[i]==k[j]:
            l=l+[j]
for i in range(0,len(l)):

 for j in range(i+1,len(l)):
      if l[i]>l[j]:
          p=l[j]
          l[j]=l[i]
          l[i]=p
 m=""

for i in range(0,len(l)):


 m=m+k[l[i]]

print(m)
