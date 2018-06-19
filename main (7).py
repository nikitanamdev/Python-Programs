s = input()
k=s.count('f')
if(k==0):
  print(-1)
elif k==1:
  print(s.find('f'))
elif k>=2:
  print(s.find('f'),s.rfind('f'))