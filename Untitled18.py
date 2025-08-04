#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 1, 3]
plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()


# In[6]:


x = ['A', 'B', 'C']
y = [10, 5, 8]
plt.bar(x, y, color='magenta')
plt.title("Bar Chart")
plt.show()


# In[7]:


x = ['A', 'B', 'C']
y = [10, 5, 8]
plt.barh(x, y, color='orange')
plt.title("Horizontal Bar Chart")
plt.show()


# In[8]:


x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.show()


# In[9]:


import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue')
plt.title("Histogram")
plt.show()


# In[10]:


labels = ['Python', 'Java', 'C++']
sizes = [50, 30, 20]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")
plt.show()


# In[11]:


plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.bar([1, 2, 3], [3, 2, 5])
plt.title("Plot 2")

plt.tight_layout()
plt.show()


# In[12]:


import matplotlib.pyplot as plt

x = [1, 2, 3]
boys = [20, 35, 30]
girls = [25, 32, 34]

plt.bar(x, boys, label='Boys')
plt.bar(x, girls, bottom=boys, label='Girls')  # girls ki bars boys ke upar

plt.xlabel('Class')
plt.ylabel('Students Count')
plt.title('Stacked Bar Chart')
plt.legend()
plt.show()


# In[13]:


import matplotlib.pyplot as plt

data = [7, 15, 13, 21, 22, 19, 25, 30, 10, 9, 11]

plt.boxplot(data)
plt.title('Box Plot Example')
plt.show()


# In[14]:


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 3, 5]
y2 = [0.5, 1, 2, 2, 3]

plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.fill_between(x, y1, y2, color='skyblue', alpha=0.5)

plt.title('Fill Between Plot')
plt.legend()
plt.show()


# In[15]:


x = [1, 2, 3, 4]
y = [2, 3, 5, 4]
error = [0.3, 0.2, 0.4, 0.1]

plt.errorbar(x, y, yerr=error, fmt='o', capsize=5)
plt.title('Error Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




