import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[50,55,60,65,70,75,80,85]

plt.scatter(x,y,color='red',marker='^',label='A Class')
plt.scatter([1,2,3,4,5,6,7,8],[10,20,30,40,50,60,70,80],color='blue',marker='^',label='B Class')
plt.xlabel('Hours studied')
plt.ylabel('Score')
plt.legend()
plt.grid()
plt.show()