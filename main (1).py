# Read an integer:
# a = int(input())
# Print a value:
# print(a)
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a+b)%2==0:
  if(c+d)%2==0:
    print("YES")
  else:
    print("NO")

elif (a+b)%2!=0:
    if(c+d)%2!=0:
      print("YES")
    else:
      print("NO")
    
else:
  print("NO")
