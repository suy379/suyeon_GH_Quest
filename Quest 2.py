#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.optimize as op
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


def f2(x): 
    return (1-x[0])**2 + 100*(x[1]-x[0]**2)**2


# In[3]:


initial_guess = (1,1) # 임의의 parameter 추정 시작값: x값은 array로 1개
result = op.minimize(f2,initial_guess) # f2(2차원 cost function)을 minimize!
result 


# In[ ]:




