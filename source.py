#!/usr/bin/env python
# coding: utf-8

# # Poverty in Developing Countries📝
# 
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# I am trying to address (Rural) Poverty in Developing Countries

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->

# In[ ]:


# The questions are;

# What are the primary causes of rural poverty in developing countries?
# How does rural poverty vary across different regions and countries?
# What specific challenges do rural populations face, such as lack of infrastructure, access to education, and healthcare?
# What interventions and policies have proven effective in reducing rural poverty?
# What are the short-term and long-term consequences of rural poverty on individuals and communities?


# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->

# In[ ]:


# My answer is to show the poverty rate in developing countries and how they can be managed. 


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

# I plan to clean and preprocess the data, to address missing values and outliers.
# I will conduct statistical analyses to identify correlations and trends related to rural poverty.
# I will utilize regression analysis to model factors contributing to rural poverty and forecast future trends.
# I also plan to implement clustering algorithms to categorize rural areas based on poverty levels and related factors.


# In[31]:


import pandas as pd

# Path to your CSV file
file_path = r'C:List of Developing Countries.csv'

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(file_path)

# Display the contents of the CSV file
print(data)


# In[32]:


import pandas as pd

# Path to your CSV file
file_path = r'C:List of Developing Countries.csv'

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(file_path)

# Get the number of countries
num_countries = len(data)

# Display the number of countries
print(f"Total number of countries: {num_countries}")


# In[33]:


import pandas as pd

# Path to your CSV file
file_path = r'C:List of Developing Countries.csv'

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(file_path)

# Clean the 'Human Asset Index' column to convert string values to numeric values
data['Human Asset Index'] = pd.to_numeric(data['Human Asset Index'], errors='coerce')

# Calculate the average Human Asset Index
average_human_asset_index = data['Human Asset Index'].mean()

# Display the average Human Asset Index
print(f"Average Human Asset Index: {average_human_asset_index:.2f}")


# In[34]:


import pandas as pd

# Path to your CSV file
file_path = r'C:List of Developing Countries.csv'

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(file_path)

# Clean the 'GNI per capita' column to convert string values to numeric values
data['GNI per capita'] = data['GNI per capita'].str.replace('USD', '').str.replace(',', '').astype(float)

# Calculate the average GNI per capita
average_gni_per_capita = data['GNI per capita'].mean()

# Display the average GNI per capita
print(f"Average GNI per capita: {average_gni_per_capita:.2f} USD")


# In[25]:


# Sort the data by GNI per capita and select the top 10 countries
top_countries = data.nlargest(10, 'GNI per capita')

# Plotting the bar chart for the top countries with highest GNI per capita
plt.figure(figsize=(10, 6))
plt.bar(top_countries['Country'], top_countries['GNI per capita'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('GNI per capita (USD)')
plt.title('Top 10 Countries with Highest Gross National Income (GNI) per Capita')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[26]:


# Select the bottom 10 countries with lowest GNI per capita
bottom_countries = data.nsmallest(10, 'GNI per capita')

# Plotting the bar chart for the bottom countries with lowest GNI per capita
plt.figure(figsize=(10, 6))
plt.bar(bottom_countries['Country'], bottom_countries['GNI per capita'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('GNI per capita (USD)')
plt.title('Top 10 Countries with Lowest Gross National Income (GNI) per Capita')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[35]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your CSV file
file_path = r'C:List of Developing Countries.csv'

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(file_path)

# Clean the 'Human Development Index' column to convert it to numeric values
data['Human Development Index'] = pd.to_numeric(data['Human Development Index'], errors='coerce')

# Plotting the density plot for HDI analysis
plt.figure(figsize=(10, 6))
sns.kdeplot(data['Human Development Index'], fill=True, color='skyblue')
plt.xlabel('Human Development Index (HDI)')
plt.ylabel('Density')
plt.title('Human Development Index (HDI) Distribution among Countries')
plt.grid(True)
plt.show()


# In[36]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your CSV file
file_path = r'C:List of Developing Countries.csv'

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(file_path)

# Clean 'GNI per capita' column to convert string values to numeric
data['GNI per capita'] = data['GNI per capita'].str.replace(',', '').str.replace(' USD', '').astype(float)

# Clean 'Human Development Index' column to convert string values to numeric
data['Human Development Index'] = pd.to_numeric(data['Human Development Index'], errors='coerce')

# Plotting the scatter plot for GNI per Capita vs. HDI
plt.figure(figsize=(10, 6))
sns.scatterplot(x='GNI per capita', y='Human Development Index', data=data, color='skyblue')
plt.xlabel('GNI per Capita (USD)')
plt.ylabel('Human Development Index (HDI)')
plt.title('Relationship between GNI per Capita and HDI')
plt.grid(True)
plt.show()


# In[28]:


# Select the top 10 countries with the highest HDI
top_countries_hdi = data.nlargest(10, 'Human Development Index')

# Plotting the bar chart for the top 10 countries with highest HDI
plt.figure(figsize=(10, 6))
plt.bar(top_countries_hdi['Country'], top_countries_hdi['Human Development Index'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Human Development Index')
plt.title('Top 10 Countries with Highest Human Development Index')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[29]:


# Select the lowest 10 countries with the lowest HDI
lowest_countries_hdi = data.nsmallest(10, 'Human Development Index')

# Plotting the bar chart for the lowest 10 countries with lowest HDI
plt.figure(figsize=(10, 6))
plt.bar(lowest_countries_hdi['Country'], lowest_countries_hdi['Human Development Index'], color='salmon')
plt.xlabel('Country')
plt.ylabel('Human Development Index')
plt.title('Lowest 10 Countries with Lowest Human Development Index')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[23]:


# Identifying top and bottom countries based on HDI
top_countries_hdi = data.nlargest(5, 'Human Development Index')  # Change '5' to the number of top countries you want to visualize
bottom_countries_hdi = data.nsmallest(5, 'Human Development Index')  # Change '5' to the number of bottom countries you want to visualize

# Visualizing top and bottom countries based on HDI
plt.figure(figsize=(12, 6))

# Top countries based on HDI
plt.subplot(1, 2, 1)
sns.barplot(x='Human Development Index', y='Country', data=top_countries_hdi, palette='viridis')
plt.title('Top Countries based on HDI')
plt.xlabel('Human Development Index')
plt.ylabel('Country')

# Bottom countries based on HDI
plt.subplot(1, 2, 2)
sns.barplot(x='Human Development Index', y='Country', data=bottom_countries_hdi, palette='magma')
plt.title('Bottom Countries based on HDI')
plt.xlabel('Human Development Index')
plt.ylabel('Country')

plt.tight_layout()
plt.show()


# In[27]:


# Data 2

import pandas as pd

# Read the CSV file directly using its path
data = pd.read_csv(r"C:Country Development.csv")

# Display the first few rows of the dataset
print(data.head())


# In[30]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
file_path = pd.read_csv(r"C:Country Development.csv")
data = pd.read_csv(r"C:Country Development.csv")

# Set the 'Region' column as the index for easy filtering
data.set_index('Region', inplace=True)

# Select columns representing years between 2010 and 2018
years = [str(year) for year in range(2010, 2019)]
available_years = [col for col in data.columns if col in years]

# Plotting the trend of poverty rates for each region
plt.figure(figsize=(12, 8))

for region in data.index:
    plt.plot(available_years, data.loc[region, available_years], label=region)

plt.xlabel('Year')
plt.ylabel('Poverty Rate (%)')
plt.title('Poverty Rates Over Time (2010 to 2018) in Different Regions')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()

plt.show()


# In[32]:


# Comparing Poverty Rates between Categories (e.g., Least developed, Landlocked, Small island developing States):

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
file_path = r"C:Country Development.csv"
data = pd.read_csv(r"C:Country Development.csv")

# Set the 'Region' column as the index for easy filtering
data.set_index('Region', inplace=True)

# Select columns representing categories for comparison
categories = ['Least developed countries', 'Landlocked developing countries', 'Small island developing States']

# Filter data for the selected categories
category_data = data.loc[categories]

# Transpose the filtered DataFrame for easier plotting
category_data_transposed = category_data.T

# Plotting the poverty rates for different categories
plt.figure(figsize=(12, 8))

for category in category_data_transposed.columns:
    plt.bar(category_data_transposed.index, category_data_transposed[category], label=category)

plt.xlabel('Year')
plt.ylabel('Poverty Rate (%)')
plt.title('Comparison of Poverty Rates Between Different Categories of Countries')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# In[33]:


# 3.	Top and Bottom Performers in Poverty Reduction:

# Which regions or categories have shown the most significant decrease or increase in poverty rates?

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
file_path = r"C:Country Development.csv"
data = pd.read_csv(r"C:Country Development.csv")

# Set the 'Region' column as the index for easy filtering
data.set_index('Region', inplace=True)

# Select columns representing years 2010 and 2018
years = ['2010', '2018']

# Filter data for the selected years
year_data = data[years]

# Calculate the change in poverty rates from 2010 to 2018
year_data['Change'] = year_data['2018'] - year_data['2010']

# Sort the data based on change in poverty rates
sorted_data = year_data['Change'].sort_values()

# Plotting the change in poverty rates
plt.figure(figsize=(10, 8))

bar_colors = ['red' if c < 0 else 'green' for c in sorted_data]
sorted_data.plot(kind='bar', color=bar_colors)

plt.xlabel('Region or Category')
plt.ylabel('Change in Poverty Rate (%)')
plt.title('Change in Poverty Rates (2010 to 2018) by Region or Category')
plt.grid(axis='y')
plt.axhline(0, color='black', linewidth=0.5)  # Add a horizontal line at 0 for reference
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()



# In[34]:


# 4.	Global vs. Regional Poverty Trends:

# How do poverty rates in specific regions compare to the global average?

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
file_path = r"C:Country Development.csv"
data = pd.read_csv(r"C:Country Development.csv")

# Set the 'Region' column as the index for easy filtering
data.set_index('Region', inplace=True)

# Calculate the global average poverty rate for each year
global_average = data.mean(axis=0)

# Select specific regions for comparison
regions_to_compare = ['Sub-Saharan Africa', 'Central and Southern Asia', 'Latin America and the Caribbean']

# Plotting comparison of poverty rates in specific regions to global average
plt.figure(figsize=(10, 6))

for region in regions_to_compare:
    plt.plot(data.columns, data.loc[region], label=region)

plt.plot(data.columns, global_average, label='Global Average', linestyle='--', color='black')

plt.xlabel('Year')
plt.ylabel('Poverty Rate (%)')
plt.title('Comparison of Poverty Rates in Specific Regions to Global Average')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()



# In[35]:


# 6.	Regional Distribution of Poverty in a Specific Year (e.g., 2018):
# Choropleth map showing the percentage of population in poverty by region.

import pandas as pd
import plotly.express as px

# Read the GeoJSON file or shapefile containing geographical boundaries
# Replace 'geojson_file_path' with the path to your GeoJSON file or shapefile
# Example:
# geojson_file_path = 'path/to/your/geojson_or_shapefile'

# Read the dataset containing poverty rates by region for the year 2018
file_path = r"C:Country Development.csv"
data = pd.read_csv(r"C:Country Development.csv")

# Filter the data for the year 2018
data_2018 = data[['Region', '2018']]  # Assuming the column name for poverty rates in 2018 is '2018'

# Assuming the GeoJSON file or shapefile contains a column named 'Region' to match the regions in your dataset
# Merge the GeoJSON data and the poverty rates data based on the 'Region' column
# merged_data = geojson_data.merge(data_2018, on='Region', how='left')

# For demonstration purposes, create a sample DataFrame simulating merged data with a few regions and poverty rates
merged_data = pd.DataFrame({
    'Region': ['Region A', 'Region B', 'Region C'],  # Example regions from the GeoJSON file
    '2018': [15.6, 8.9, 12.3]  # Example poverty rates for the year 2018
})

# Create a choropleth map using Plotly Express
fig = px.choropleth(
    merged_data,
    locations='Region',  # Column in the GeoJSON/shapefile containing region/country names or codes
    locationmode='country names',  # Use 'ISO-3' for country codes
    color='2018',  # Column in the DataFrame containing the data to be visualized (poverty rates)
    color_continuous_scale='Viridis',  # Choose a color scale
    labels={'2018': 'Poverty Rate (%)'},  # Label for the color bar
    title='Poverty Rate by Region in 2018'  # Title of the choropleth map
)

# Show the interactive map
fig.show()


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[2]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

