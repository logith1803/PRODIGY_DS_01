#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

# Data
categories = ['Male', 'Female', 'Other']
counts = [350, 400, 50]  # These are hypothetical counts

# Plotting
plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color=['blue', 'pink', 'gray'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Genders in a Population')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[ ]:




