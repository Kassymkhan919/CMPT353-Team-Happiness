#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import pandas as pd
import difflib as dl


# In[30]:


new_names = pd.read_csv('names.csv').values[:,0]
def nameReplace(oldName):
    newName = dl.get_close_matches(oldName, new_names)
    if not newName:
        return ''
    return newName[0]


# In[31]:


borders = pd.read_csv('borders.csv')
borders['country_name'] = borders['country_name'].apply(nameReplace)
borders['country_border_name'] = borders['country_border_name'].apply(nameReplace)
borders = borders[borders['country_name'] != '']
borders = borders[borders['country_border_name'] != '']
borders.to_csv('border-names.csv')


# In[32]:


data15 = pd.read_csv('2015-happiness-only.csv')
data16 = pd.read_csv('2016-happiness-only.csv')
data17 = pd.read_csv('2017-happiness-only.csv')
borders = borders.merge(data15, how='left', left_on='country_border_name', right_on='Country').rename(columns = {'Happiness Score': 'Happiness Score 2015'})
borders = borders.drop(['Country'], axis=1)
borders = borders.merge(data16, how='left', left_on='country_border_name', right_on='Country').rename(columns = {'Happiness Score': 'Happiness Score 2016'})
borders = borders.drop(['Country'], axis=1)
borders = borders.merge(data17, how='left', left_on='country_border_name', right_on='Country').rename(columns = {'Happiness Score': 'Happiness Score 2017'})
borders = borders.drop(['Country'], axis=1)
borders = borders.rename(columns = {'country_name': 'Country Name', 
                                    'country_border_name': 'Country Border Name'})


# In[33]:


borders.to_csv('Three-Year-Data.csv')


# In[ ]:





# In[ ]:




