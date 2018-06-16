# Read an integer:
# a = int(input())
# Print a value:
# print(a)
a=int(input())
b=int(input())
c=int(input())
d=int(input())


if (a==c-1) & (b==d-1):
  print("YES")
elif (a==c+1) & (b==d+1):
  print("YES")
elif (a==c-1) & (b==d+1):
  print("YES")
elif (a==c+1) & (b==d-1):
  print("YES")  
elif (a==c) & (d==b-1) | (d==b+1):
  print("YES")
elif (d==b) & (a==c-1) | (a==c+1):
  print("YES")
else:
  print("NO")
