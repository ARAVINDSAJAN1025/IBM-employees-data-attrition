#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data_set = pd.read_csv('IBM Attrition Data.csv')
data_set


# In[3]:


data_set.head()


# In[4]:


data_set.info()


# In[5]:


data_set.describe()


# In[6]:


## data analysis


# In[7]:


education = data_set.Education.value_counts()
education


# In[8]:


education = data_set.Education.value_counts()
education_labels = {1: 'Below College', 2: 'College',3: 'Bachelors', 4: 'Masters', 5: 'Doctors'}


# In[9]:


education.index.to_list()
education[1]


# In[10]:


plt.figure(figsize = (7,7))
plt.title("Educational Qualification of Employees")
plt.pie(education, labels = [education_labels[index] for index in education.index.to_list()],autopct='%.2f%%')
plt.show()


# In[11]:


job_satisfaction =data_set.JobSatisfaction.value_counts()
satisfaction_labels = {1: 'Low',2: 'Medium',3: 'High',4: 'Very High'}


# In[12]:


plt.figure(figsize = (7,7))
plt.title("Job Satisfaction of Employees")
plt.pie(job_satisfaction, labels = [satisfaction_labels[index] for index in job_satisfaction.index.to_list()],autopct='%.2f%%')
plt.show()


# In[13]:


environment_satisfaction = data_set.EnvironmentSatisfaction.value_counts()


# In[14]:


plt.figure(figsize = (7,7))
plt.title('Environment Satisfaction of Employees')
plt.pie(environment_satisfaction, labels = [satisfaction_labels[index] for index in environment_satisfaction.index.tolist()],autopct= '%.2f%%')
plt.show()


# In[15]:


ages_count = data_set['Age'].value_counts()


# In[16]:


plt.figure(figsize= (15,8))
plt.title("Age Distribution of Employees")
plt.bar(ages_count.index,ages_count)
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.show()


# In[17]:


data_set["Attrition"].unique()


# In[18]:


attrition_yes = data_set[data_set["Attrition"] == "Yes"]
attrition_no = data_set[data_set["Attrition"] == "No"]


# In[19]:


attrition_yes_by_age = attrition_yes['Age'].value_counts()
attrition_no_by_age = attrition_no['Age'].value_counts()


# In[20]:


attrition_yes_by_age


# In[21]:


plt.figure(figsize=(15,8))
plt.title('Employees who left in IBM By Age')
plt.bar(attrition_yes_by_age.index, height=attrition_yes_by_age)
plt.yticks(range(0,max(attrition_yes_by_age)+1))
plt.show()


# In[22]:


plt.figure(figsize=(15,8))
plt.title('Attribution currently working in IBM by Age')
plt.bar(attrition_no_by_age.index, height=attrition_no_by_age)
plt.yticks(range(0,max(attrition_no_by_age)+1,5))
plt.show()


# In[23]:


employees_leaving_percent = pd.Series([attrition_yes_by_age.get(index,default=0)/ages_count.get(index,default=0)*100 for index in range(18,61)],index= range(18,61))


# In[24]:


plt.figure(figsize = (15,8))
plt.bar(employees_leaving_percent.index, employees_leaving_percent)
plt.title("Percent of Employees leaving by age")
plt.xlabel("Age")
plt.ylabel('Percent')
plt.show()


# In[25]:


employees_leaving_percent


# In[26]:


age_work_life_balance = data_set[['Age', 'WorkLifeBalance']]


# In[ ]:


# explore data of left employees


# In[27]:


left_employees_data_set = data_set[data_set["Attrition"] == 'Yes']


# In[28]:


left_employees_data_set.describe()


# In[29]:


# environment satisfation of left employees


# In[30]:


env_satis_of_left_emp = left_employees_data_set.EnvironmentSatisfaction.value_counts()


# In[31]:


plt.figure(figsize=(7,7))
plt.title('Environment Satisfaction of left Employees')
plt.pie(env_satis_of_left_emp, labels = [satisfaction_labels[index] for index in env_satis_of_left_emp.index.tolist()], autopct='%.2f%%')
plt.show()


# In[32]:


job_satis_of_left_emp = left_employees_data_set.JobSatisfaction.value_counts()


# In[33]:


plt.figure(figsize=(7,7))
plt.title('Job Satisfaction of left Employees')
plt.pie(job_satis_of_left_emp, labels = [satisfaction_labels[index] for index in job_satis_of_left_emp.index.tolist()], autopct='%.2f%%')
plt.show()


# In[ ]:




