#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Height.csv')
dataset


# In[2]:


x= dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1].values


# In[3]:


x


# In[4]:


y


# In[5]:


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)


# In[6]:


plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg.predict(x), color = 'blue')
plt.title('Height (Linear Regression)')
plt.xlabel('Error in m')
plt.ylabel('Kp')
plt.show()


# In[10]:



p = 903.0329* np.exp(-0.0125*x)#e^-0.0125x


# In[11]:


plt.scatter(x, y, color = 'red')
plt.plot(x, p, color = 'blue')
plt.title('Height (Prajwal "Regression")')
plt.xlabel('Error in m')
plt.ylabel('Kp')
plt.savefig("Praj_reg.jpg")
plt.show()


# In[29]:


# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree =7)
x_poly = poly_reg.fit_transform(x)
poly_reg.fit(x_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)


# In[35]:


X_grid = np.arange(min(x), max(x), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)) - 20, color = 'blue')
plt.title('Height (Polynomial Regression)')
plt.xlabel('Error in m')
plt.ylabel('Kp')
plt.show()

lin_reg_2.predict(poly_reg.fit_transform([[15]]))


# In[37]:


import pickle


# In[38]:



filename = 'height_pid_regression.sav'
pickle.dump(lin_reg_2, open(filename, 'wb'))


# In[ ]:


loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)

