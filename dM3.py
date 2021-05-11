
# coding: utf-8

# In[83]:


USERNAME = "DM3"
PASSWORD = "DPHACK"
MDSS_SSID="AZK1"
DB2_SSID="DBBG"

#data['Annual CO2 emissions'].plot(kind='hist')

import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[84]:


import glob
print(glob.glob("*.csv"))


# In[85]:


print(glob.glob("annual-co2-emissions-per-country.csv"))


# In[86]:


data = pd.read_csv('annual-co2-emissions-per-country.csv')


# In[87]:


data.head(5)


# In[88]:


a = data.columns[0::2] 
b = data.columns[3::4]

c = a.append(b)

print(c)


# In[89]:


data.dtypes


# In[90]:


data.info()


# In[91]:


data[a].plot(kind='hist')


# In[92]:


data[a].plot(kind='hist')
plt.xlabel("Year", labelpad=14)
plt.ylabel("Annual CO2 emissions", labelpad=14)
plt.title("Annual CO2 emissions per year", y=1.015, fontsize=22);
# Data from: https://ourworldindata.org/grapher/annual-co2-emissions-per-country


# In[93]:


print(glob.glob("ocean-acidity_fig-1_clean3.csv"))


# In[94]:


data_ocean = pd.read_csv('ocean-acidity_fig-1_clean3.csv')


# In[95]:


data_ocean.head(10)


# In[96]:


HawaiiA = data_ocean.columns[1]
HawaiiB = data_ocean.columns[2]
#HawaiiC = data_ocean.columns[3]

HawaiiD = data_ocean.columns[5]
HawaiiE = data_ocean.columns[6]
#HawaiiF = data_ocean.columns[7]

HawaiiG = data_ocean.columns[9]
HawaiiH = data_ocean.columns[10]
#HawaiiI = data_ocean.columns[11]

Hawaii = [HawaiiA, HawaiiB, HawaiiD, HawaiiE, HawaiiG, HawaiiH]

print(Hawaii)


# In[97]:


data_ocean.plot(kind='hist')


# In[ ]:




