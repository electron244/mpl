import matplotlib.pyplot as plt

product= [1,2,3,4,5]
sales =  [1000,1500,600,1000,122]

plt.plot(product,sales,marker='o',color='red')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title("Sales Graph")
# plt.grid()
plt.savefig('Data.png',dpi=300,bbox_inches='tight')
plt.show()