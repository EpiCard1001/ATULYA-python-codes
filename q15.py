y=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
x=["1","2","3","4","5","6","7","8","9","0"]
k=l=q=0
r="iauhfahda*#&kmvdfmvf123124"
for i in r:

    if i in x:
      k=k+1
    elif i in y:
       l=l+1
    else:

      q=q+1


print("alphabets=",l, "special characters=",q,"integers=",k)