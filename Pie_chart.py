import matplotlib.pyplot as plt

product= ['India','Pakistan','China','America','Russia']
sales =  [1000,1500,600,1000,122]

plt.pie(sales,labels=product,autopct='%1.1f%%' )
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title("Sales Graph")

plt.show()