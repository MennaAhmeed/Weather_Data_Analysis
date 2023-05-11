#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


data= pd.read_csv(r'C:\Users\Dell\Downloads\weather.csv')


# In[5]:


data


# In[6]:


data.head()


# In[9]:


data.shape


# In[10]:


data.index


# In[11]:


data.columns


# In[12]:


data.dtypes


# In[14]:


data['Weather'].unique()


# In[16]:


data.nunique()


# In[17]:


data.count()


# In[18]:


data.value_counts()


# In[19]:


data.info()


# In[20]:


#Q. 1)  Find all the unique 'Wind Speed' values in the data.


# In[21]:


data['Wind Speed_km/h'].unique()  #answer


# In[22]:


#Q. 2) Find the number of times when the 'Weather is exactly Clear'.


# In[25]:


data['Weather'].value_counts()
 


# In[29]:


data[data.Weather=='Clear']


# In[32]:


data.groupby('Weather').get_group('Clear')  #answer


# In[33]:


#Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.


# In[36]:


data['Wind Speed_km/h'].value_counts()


# In[39]:


data[data['Wind Speed_km/h']==4] #answer


# In[40]:


#Q. 4) Find out all the Null Values in the data.


# In[43]:


data.isnull().sum() #answer


# In[44]:


data.notnull().sum()


# In[45]:


#Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.


# In[49]:


data.rename(columns={'Weather':'Weather Condition'},inplace=True)  #answer


# In[50]:


data


# In[51]:


#Q. 6) What is the mean 'Visibility' ?


# In[54]:


data['Visibility_km'].mean()   #answer


# In[55]:


#Q. 7) What is the Standard Deviation of 'Pressure'  in this data?


# In[56]:


data['Press_kPa'].std()  #answer


# In[57]:


#Q. 8) What is the Variance of 'Relative Humidity' in this data ?


# In[58]:


data['Rel Hum_%'].var()   #answer


# In[59]:


#Q. 9) Find all instances when 'Snow' was recorded.


# In[60]:


data['Weather Condition'].value_counts()


# In[62]:


data[data['Weather Condition']=='Snow']


# In[76]:


data[data['Weather Condition'].str.contains('Snow')]  #answer


# In[78]:


#Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.


# In[81]:


data[(data['Wind Speed_km/h'] >24) &(data['Visibility_km']==25)]  #answer 


# In[82]:


#Q. 11) What is the Mean value of each column against each 'Weather Condition ?


# In[86]:


data.groupby('Weather Condition').mean() #answer 


# In[87]:


#Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?


# In[88]:


data.groupby('Weather Condition').max() #answer


# In[89]:


data.groupby('Weather Condition').min()  #answer


# In[91]:


#Q. 13) Show all the Records where Weather Condition is Fog.


# In[93]:


data[data['Weather Condition']=='Fog']  #answer 


# In[94]:


#Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.


# In[96]:


data[(data['Weather Condition']=='Clear') & (data['Visibility_km']>40)]  #answer


# In[97]:


#Q. 15) Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'


# In[100]:


data[(data['Weather Condition']=='Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)]   #answer


# In[ ]:




