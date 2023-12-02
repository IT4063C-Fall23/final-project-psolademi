#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# I am trying to address Rural Poverty in Developing Countries

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->

# In[ ]:


The questions are;

get_ipython().run_line_magic('pinfo', 'countries')
get_ipython().run_line_magic('pinfo', 'countries')
get_ipython().run_line_magic('pinfo', 'healthcare')
get_ipython().run_line_magic('pinfo', 'poverty')
get_ipython().run_line_magic('pinfo', 'communities')


# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->

# In[ ]:


The answer I am trying to give is why there are rural proverty in developing countries and ways to improve them to make the lives of people better


# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->

# In[ ]:


These are the data sources I am trying to use for this project
Khan, M. H. (n.d.).Finance and development. Finance and Development | F&D. https://www.imf.org/external/pubs/ft/fandd/2000/12/khan.htm 
World development indicators. DataBank. (n.d.). https://databank.worldbank.org/source/world-development-indicators
Khan. (2000).Rural Poverty in Developing Countries--Issues and Policies. International Monetary Fund.


# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->

# In[1]:


# Start your code here

Process, Analyze:

I plan to clean and preprocess the data, to address missing values and outliers.
I will conduct statistical analyses to identify correlations and trends related to rural poverty.
I will utilize regression analysis to model factors contributing to rural poverty and forecast future trends.
I also plan to implement clustering algorithms to categorize rural areas based on poverty levels and related factors.


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[2]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')


# In[1]:


import requests
import pandas as pd

# URL of the dataset
url = "https://data.apps.fao.org/catalog/dataset/6d4251eb-d44e-489d-82fb-31422c2b5b64/resource/01e5892d-fe1d-45de-b126-25a0deb35f81/download/si.pov.ruhc.csv"

# Fetch the data from the URL
response = requests.get(url)

if response.status_code == 200:
    # Read the content as a Pandas DataFrame
    data = pd.read_csv(url)

    # Display the first few rows of the dataset to verify
    print(data.head())
else:
    print("Failed to fetch the data. Status code:", response.status_code)

