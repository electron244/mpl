import matplotlib.pyplot as plt

marks = [34,53,55,34,23,67,87,76,87,65,89,90,99,54,33,44,12,6,76,54,43,79]
plt.hist(marks,bins=6,color='orange',edgecolor='white')
plt.xlabel('Marks Range')
plt.ylabel('Number of Students')
plt.title('Student Marks Distribution')
plt.show()