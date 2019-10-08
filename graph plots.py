
get_ipython().system('pip install networkx==2.3')


import matplotlib.pyplot as plt



x=[1,0.1,0.097,0.092203,0.092202,0.0921]



y=[254,255,255,309,1577,1577]


plt.plot(x,y)


x=[0.097,0.092203,0.092202,0.0921]


y=[255,309,1577,1577]


# naming the x axis 
plt.xlabel('x') 
# naming the y axis 
plt.ylabel('Y-Label') 
plt.title('Example')
plt.plot(x,y,color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12)



plt.xlabel('X') 
# naming the y axis 
plt.ylabel('Y-Label') 
plt.title('Markers Example')
plt.scatter(x,y, label= "stars", color= "green",marker= "*", s=30) 




