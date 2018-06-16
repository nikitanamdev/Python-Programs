a=[]
b=int(input())
while(b!=0):
  a.append(b)
  b=int(input())

a.sort()
n=len(a)
print(a[n-2])