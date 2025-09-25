import matplotlib.pyplot as plt

product= [1,2,3,4,5]
sales =  [1000,1500,600,1000,122]

plt.bar(product,sales,color='orange')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title("Sales Graph")
plt.legend()
# plt.grid()
plt.show()