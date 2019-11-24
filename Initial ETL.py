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


names = data15['Country'].values
def nameReplace(oldName):
    newName = dl.get_close_matches(oldName[:10], names)
    if not newName:
        return ''
    return newName[0]


# In[5]:


borders['country_name'] = borders['country_name'].apply(nameReplace)
borders['country_border_name'] = borders['country_border_name'].apply(nameReplace)
borders = borders[borders['country_name'] != '']
borders = borders[borders['country_border_name'] != '']


# In[6]:


borders = borders.merge(data15, how='left', left_on='country_border_name', right_on='Country').rename(columns = {'Happiness Score': 'Happiness Score 2015'})
borders = borders.drop(['Country'], axis=1)
borders = borders.merge(data16, how='left', left_on='country_border_name', right_on='Country').rename(columns = {'Happiness Score': 'Happiness Score 2016'})
borders = borders.drop(['Country'], axis=1)
borders = borders.merge(data17, how='left', left_on='country_border_name', right_on='Country').rename(columns = {'Happiness Score': 'Happiness Score 2017'})
borders = borders.drop(['Country'], axis=1)
borders = borders.rename(columns = {'country_name': 'Country Name', 
                                    'country_border_name': 'Country Border Name'})


# In[7]:


borders.to_csv('Three-Year-Data.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




