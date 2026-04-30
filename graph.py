import matplotlib.pyplot as plt
import random
import numpy as  np
import sys
matplotlib.use('agg')
# pyplot is collection of continuse that make maplotlib work like MATLAB
# # data
# x = [1,2,3,4,5]
# y = [10,20,25,30,45]

# plt.plot(x, y)  # line chart
# plt.show()      # <- parentheses required

# ========costomize chart =================
# x = [1,2,3,4,5]
# y = [10,20,25,30,45]
# plt.figure(figsize=(4,3))# it will give the figure size of the chart
# plt.plot(x,y, color = "red", marker = "o", linestyle = "dashed", linewidth =2, markersize = 12)
# plt. title ("the title is: Dhurander sale 2026")
# plt.xlabel("x-Axix lable is here")
# plt.ylabel("y-Axix label here")
# plt.show() 

# x= [1,2,3,4,5]
# y1 = [10,20,25,35,45]
# y2 = [20,30,35,45,55]

# plt.plot(x, y1, label = 'sales 2024')
# plt.plot(x, y2, label = 'sales 2025')
# plt.title("Dhurander sales comparision 2024 & 2025")
# plt.xlabel("month")
# plt.ylabel("sales")
# plt.legend()
# plt.show()

# subject = ["Hindi", "Englis","Math","gk","sicnce","s.s.t"]
# Student1=[45,56,58,67,89,98]
# Student2 =[20,45,56,78,89,87]
# plt.plot(subject, Student1, label = 'sales 2024')
# plt.plot(subject, Student2, label = 'sales 2025')
# plt.title("marksheet comparision 2024 & 2025")
# plt.xlabel("subject")
# plt.ylabel("Student")
# plt.legend()
# plt.show()
#==============bar chart ==============/
# x = [1,2,3,4,5]
# y = [10,20,25,35,45]
# plt.bar(x,y, color = "green",width = 0.5)
# plt.title("Bar chart ")
# plt.show()
# sahi nahi hai=========
# student = ["jk","versha","bavishya","ayush","menu","deepak","sonkika","simran","manu","shivani"]
# Marks = [50, 60, 90, 45, 35, 55, 65,75,70,40, ]
# color = ["red","orange","green","pink","yellow","black","pink","gray","white","red"]
# plt.bar(student, Marks, label = 'sales 2024')
# # plt.bar( label = 'sales 2025')
# plt.title("marksheet comparision 2024 & 2025")
# plt.label("subject")
# plt.ylabel("Student")
# plt.legend()
# plt.show()


# sahi hai
# data = [random.randint(1,100) for i in range(100)]
# plt.hist(data,bins = 5)
# plt.title("Histogrme Example")
# plt.show()

# pie chart ========

# catogories = ['A','B','C','D','E']

# sales = [10,20,55,35,45]
# plt.pie(sales, labels = catogories, autopct = '%1.1') 
# plt.title("pie chart example")
# plt.show()


# scatter plot==========
# y1 = [10,20,25,35,45]
# y2 = [20,20,35,45,55]

# plt.scatter(y1,y2)
# plt.title("scatter plot example")
# plt.show()

# sub plots====used to show multiple chart in one figure
#data - 1
# catogories = ['Mon','Tue','Wed','Thur','Fri']
# sales = [10,20,55,35,45]

# #dat - 2
# y1 = [ 10,20,25,35,45]
# y2 = [20,30,35,45,55]
# plt.figure(figsize=(4, 6))
# #first plot - bar chart 
# plt.subplot(1,2,1) #row, columan, postion

# plt.bar(catogories,sales)
# plt.title("Daily sales")
# plt.xlabel("Week Day")
# plt.ylabel("sales")

# #second plot -scatter chart
# plt.subplot(1,2,2)
# plt.scatter(y1,y2)
# plt.title("User Example")
# plt.xlabel("User 1")
# plt.ylabel("User 2")
# plt.show()

# introucing the grides

# x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# y = np.array([10,15,20,25,30,35,40, 45,50,55,60,65,70,75,80])
# plt.title("West Bengal Vs Tamil nadu polls")
# plt.xlabel("Month")
# plt.ylabel("polls")
# plt.plot(x, y, marker = "o",linestyle = "dashed",color = "purple", linewidth = 2, markersize =5)
# plt.grid(axis = "y") # it will show the grid in the chart
# plt.show()
# x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# y = np.array([10,15,20,25,30,35,40, 45,50,55,60,65,70,75,80])
# plt.title("West Bengal Vs Tamil nadu polls")
# plt.xlabel("Month")
# plt.ylabel("polls")
# plt.plot(x, y, marker = "o",linestyle = "dashed",color = "purple", linewidth = 2, markersize =5)
# plt.grid(color = "green", linestyle = '--', linewidth = 0.5) # it will show the grid in the chart
# plt.show()


#day one, the agg and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


