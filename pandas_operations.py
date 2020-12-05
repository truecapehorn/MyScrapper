#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from glob import glob
import datetime
now = datetime.date.today() # data do pliku


# In[2]:


pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('colheader_justify', 'center')


# In[3]:


# import starych df
data_files = sorted(glob('Dane/dane*.csv'))
df_old=pd.concat((pd.read_csv(file) for file in data_files), ignore_index=True)
df_old['date']=pd.to_datetime(df_old['date'])


# In[4]:


df_old.dtypes


# In[5]:


df_old


# In[ ]:





# In[6]:


from data import dane


# In[7]:


df_new = pd.DataFrame(dane, columns=['date', 'name', 'url', 'price', 'currency'])


# In[8]:


df_new


# In[9]:


df_new.to_csv(f'Dane/dane{now}.csv')


# In[10]:


df_all=pd.concat([df_old, df_new], ignore_index=True)


# In[11]:


df_all


# In[ ]:





# In[12]:


piv=df_old.pivot_table(index=(df_all.date.dt.year,df_all.date.dt.month,df_all.date.dt.day),columns='name',values='price',aggfunc=min)


# In[13]:


piv.diff().ne(0)


# In[14]:


piv.plot(kind='bar')






