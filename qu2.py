def chupa(a): 
  x=str(a);
  n=len(x);
  b="" 
  for i in range (0,n): 
      if i<n-4: 
          b=b+"*"
      if i>=n-4:
         b=b+x[i]; 
  return b 
l=int(input("enter ur credit card number HEHE: ")); 
k=chupa(l) ;
print(k); 
