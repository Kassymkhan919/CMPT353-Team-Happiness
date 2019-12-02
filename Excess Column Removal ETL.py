#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import difflib as dl


# In[2]:


borders = pd.read_csv('GEODATASOURCE-COUNTRY-BORDERS.csv')
data15 = pd.read_csv('2015.csv')
data16 = pd.read_csv('2016.csv')
data17 = pd.read_csv('2017.csv')
data17 = data17.rename(columns = {'Happiness.Score': 'Happiness Score'})


# In[3]:


borders = borders[['country_name', 'country_border_name']]
borders = borders[borders['country_border_name'].notnull()]
data15 = data15[['Country', 'Happiness Score']]
data16 = data16[['Country', 'Happiness Score']]
data17 = data17[['Country', 'Happiness Score']]


# In[4]:


names = pd.concat(
    [data15['Country'], data16['Country']], ignore_index=True
         ).drop_duplicates().reset_index(drop=True)
names = pd.concat(
    [names, data17['Country']], ignore_index=True
         ).drop_duplicates().reset_index(drop=True)
names = pd.DataFrame(names, columns=['Country'])


# In[5]:


names.to_csv('names.csv', index=False)


# In[6]:


borders.to_csv('borders.csv', index=False)


# In[7]:


data15.to_csv('2015-happiness-only.csv', index=False)
data16.to_csv('2016-happiness-only.csv', index=False)
data17.to_csv('2017-happiness-only.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




