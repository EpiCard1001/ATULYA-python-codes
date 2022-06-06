x="abc123udshfsiuf12909105jkralhfh814810492"
y=[1,2,3,4,5,6,7,8,9,0]
z=["1","2","3","4","5","6","7","8","9","0"]
k=0
for i in x:

  if i in z:

    for j in range(0,len(z)):
        if i==z[j]:
            k=k+y[j]
print(k)
