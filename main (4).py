n1=int(1)
n2=int(1)
n=int(input())
if (n==1) | (n==2):
  print(n1)
else:
  i=int(2)
  while(i<n):
    x=n1+n2
    n1=n2
    n2=x
    i=i+1
  print(x)
  
