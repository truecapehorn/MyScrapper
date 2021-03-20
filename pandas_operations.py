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
df_old.drop('Unnamed: 0',axis=1,inplace=True,errors='ignore')


# In[4]:


from data import dane


# In[5]:


df_new = pd.DataFrame(dane, columns=['date', 'name', 'url', 'price', 'currency'])


# In[6]:


if f'Dane/dane{now}.csv' in data_files:
    df_new.to_csv(f'Dane/dane{now}.csv',mode='a', header=False)
else:
    df_new.to_csv(f'Dane/dane{now}.csv',mode='w', header=True)
    


# # Mardzin framow

# In[7]:


df_all=pd.concat([df_old, df_new], ignore_index=True)


# In[8]:


df_all.to_csv(f'Dane/all_data.csv')


# In[9]:


df_all.head()


# In[10]:


# Produktuy


# In[11]:


df_produkty=df_all[['name','url']].drop_duplicates()
# df_produkty.set_index('name',inplace=True)
df_produkty.reset_index(inplace=True,drop=True)
df_produkty


# # Pivoty

# In[12]:


piv=df_all.pivot_table(index=(df_all.date.dt.year,df_all.date.dt.month,df_all.date.dt.day),columns='name',values='price',aggfunc=min)


# In[13]:


piv.tail()


# In[14]:


filtr1=piv.diff().ne(0).any(1)


# In[15]:


filtr2=piv.diff().any(1)


# In[16]:


df_diff=piv[filtr1]


# # Ploty

# In[17]:


fig, axes = plt.subplots(int(np.ceil(piv.columns.size/2)),2,figsize=(15,20),sharex=True)
fig.suptitle('Ceny', fontsize=22)
fig.tight_layout()
fig.subplots_adjust(top=0.95)
for n,a in enumerate(axes.flat):
    if n < piv.columns.size:
        piv.iloc[:,n].plot(ax=a,kind='line',grid=True)
        a.set(xlabel=f'(Rok, Miesiąc, Dzien)', ylabel=f'Cena',title=f"{piv.columns[n]}")

plt.savefig('Fig/graph.png',transparent=False)
# plt.show()


# In[18]:


# testy


# In[ ]:




