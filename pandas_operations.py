#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


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


# # Mardzin framow

# In[10]:


df_all=pd.concat([df_old, df_new], ignore_index=True)


# In[11]:


df_all


# In[12]:


# Produktuy


# In[13]:


df_produkty=df_all[['name','url']].drop_duplicates()
df_produkty


# # Pivoty

# In[14]:


piv=df_old.pivot_table(index=(df_all.date.dt.year,df_all.date.dt.month,df_all.date.dt.day),columns='name',values='price',aggfunc=min)


# In[15]:


piv


# In[16]:


filtr1=piv.diff().ne(0).any(1)


# In[17]:


filtr2=piv.diff().any(1)


# In[18]:


df_diff=piv[filtr1]


# # Ploty

# In[19]:


fig, axes = plt.subplots(piv.columns.size,1,figsize=(15,20),sharex=True)
fig.suptitle('Ceny', fontsize=22)
fig.tight_layout()
fig.subplots_adjust(top=0.95)
for n,a in enumerate(axes.flat):
    piv.iloc[:,n].plot(ax=a,kind='bar',grid=True)
    a.set(xlabel=f'(Rok, Miesiąc, Dzien)', ylabel=f'Cena',title=f"{piv.columns[n]}")

plt.savefig('Fig/graph.png')
# plt.show()


# In[ ]:




