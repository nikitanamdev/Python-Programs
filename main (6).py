a=[]
pos=0
b=int(input())
while(b!=0):
  a.append(b)
  b=int(input())
  
n=len(a)
#print(n)
i=int(0)
m=int(a[0])
for i in range(int(n)):
  if(m<a[i]):
    m=a[i]
    pos=int(i)
    
print(pos+1)
#print(m)