# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:22:35 2023

@author: vasth
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import stats as st

def read_world_bank_csv(filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename, header=2)
    df = df.drop(['Indicator Code', 'Country Code', 'Indicator Name'], axis=1)
    df.dropna()
    df.dropna(how='all', axis=1, inplace=True)

    df2 = df.transpose()
    df2.columns = df2.iloc[0]  # Set the first row as the column names
    df = df.set_index('Country Name')
    #df2 = df2.set_index(('Country Name', ''), append=True)
    #df2 = df2.rename_axis('Year')
    df2 = df2.rename_axis(columns='Country Name', index='Year')
    df = df.rename_axis(index='Country Name', columns='Year')

    df2 = df2.iloc[1:]  # Drop the first row
    return df, df2

def group_years_by_count(df):
    # Create dataframe with non-null count and year columns
    fda_df = df.notnull().sum().sort_values(ascending=False).to_frame().reset_index()
    fda_df.columns = ['Year', 'Non-null Count']

    # Calculate median non-null count
    median_count = fda_df['Non-null Count'].median()

    # Group years based on non-null count above or below median
    fda_groups = fda_df.groupby(fda_df['Non-null Count'] > median_count).apply(lambda x: x['Year'].tolist())

    # Print groups with messages indicating count
    result = []
    result.append(f"Years with non-null count above the median count ({median_count}):")
    result.append(str(fda_groups[True]))
    result.append("")
    result.append(f"Years with non-null count less than or equal to the median count ({median_count}):")
    result.append(str(fda_groups[False]))
    return '\n'.join(result)

    
# Indicator : Access to Electricity(% of Population)

data, area = read_world_bank_csv('Access to Electricity(% of Population).csv')
print(data.head())
print(area.head())

# Select the 10 countres_list to plot in order of the GDP list
countres_list = ['United States', 'China', 'Japan', 'Germany',  'India', 
             'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada']

# Get the data for these countres_list
data_countres_list = data.loc[countres_list]

# Plot the data
plt.figure() # Set the size of the figure
for country in countres_list:
    plt.plot(data.columns, data_countres_list.loc[country], label=country)
plt.xlabel('Year') # Set the label for the x-axis
plt.xlim(min(data.columns), max(data.columns))
plt.xticks(np.arange(0, len(data.columns)+1, 5), rotation = 90)
plt.ylabel('% of population with access to electricity') # Set the label for the y-axis
plt.title('Access to Electricity by Country') # Set the title for the plot
plt.legend( bbox_to_anchor=(1.05, 1)) # Show the legend

# Indicator : Urban population

up, up_t = read_world_bank_csv('Urban population.csv')


# Get the data for these countres_list
up_countres_list = up.loc[countres_list]

# Plot the data
plt.figure() # Set the size of the figure
for country in countres_list:
    plt.plot(up.columns, up_countres_list.loc[country], label=country)
plt.xlabel('Year') # Set the label for the x-axis
plt.xlim(min(up.columns), max(up.columns))
plt.ylabel('Urban population') # Set the label for the y-axis
plt.xticks(np.arange(0, len(up.columns)+1, 5), rotation = 90)
#plt.xticks(rotation = 90)
plt.title('Population') # Set the title for the plot

plt.legend(bbox_to_anchor=(1.05, 1)) # Show the legend
#plt.xticks(np.arange(up.columns,10)) 


# Indicator : Methane emissions (kt of CO2 equivalent)

methane, methane_t = read_world_bank_csv('Methane emissions (kt of CO2 equivalent).csv')


# Extract the data for the 5 countres_list
#countres_list = ['China', 'United States', 'India', 'Canada', 'Japan']
years = ['2015', '2016', '2017', '2018', '2019']
usage = methane.loc[countres_list, years]
plt.figure()
# Plot the bar plot
usage.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Electricity usage')
plt.title('Electricity usage in 5 countres_list')


print(methane.describe())
print(usage)


# Indicator name: Forest area (% of land area)

forest_area, forestarea_t = read_world_bank_csv('Forest area (% of land area).csv')

less_forest = forest_area.loc[countres_list, years]
print(group_years_by_count(forest_area))


# Plot the bar plot
plt.figure()
less_forest.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Forest less usage')
plt.title('Forest usage in 5 countres_list from 2014 to 2019')
plt.legend(loc='upper right')

# Indicator name: GDP growth(annual %)

GDP, GDP_t = read_world_bank_csv('GDP growth(annual %).csv')

gdp_growth = GDP.loc[countres_list, years]
plt.figure()
gdp_growth.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('GDP')
plt.title('GDP growth for 5 years')
plt.legend(loc='upper right')

#Indicator name: CO2 emmisons(kt))
co2, c02_t = read_world_bank_csv('CO2 emmisons(kt).csv')

co2_growth = co2.loc[countres_list, years]
plt.figure()
co2_growth.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Co2')
plt.title('CO2 emmisons(kt)')
plt.legend(loc='upper right')


#Indiacator Name: Agricultural land (% of land area)

Ag, ad_t = read_world_bank_csv('Agricultural land (% of land area).csv')
ag_countres_list = Ag.loc[countres_list, years]
plt.figure()
ag_countres_list.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Agri land')
plt.title('Agricultural land (% of land area)')
plt.legend(loc='upper right')


#Indiacator Name: Electric power consumption (kWh per capita)
ec, ec_t = read_world_bank_csv('Electric power consumption (kWh per capita).csv')
# Get the data for these countres_list
ec_countres_list = ec.loc[countres_list]

# Plot the data
plt.figure() # Set the size of the figure
for country in countres_list:
    plt.plot(ec.columns, ec_countres_list.loc[country], label=country)
plt.xlabel('Year') # Set the label for the x-axis
plt.xlim(min(ec.columns), max(ec.columns))
plt.ylabel('Electric power consumption (kWh per capita)') # Set the label for the y-axis
plt.xticks(np.arange(0, len(ec.columns)+1, 5), rotation = 90)
#plt.xticks(rotation = 90)
plt.title('Electric power consumption (kWh per capita)') # Set the title for the plot

plt.legend(bbox_to_anchor=(1.05, 1))


# Correlation map with all indicators for the year 2014

fd = pd.merge(data['2014'], up['2014'], left_index=True, right_index=True)
fd = pd.merge(fd, methane['2014'], left_index=True, right_index=True)
fd = pd.merge(fd, forest_area['2014'], left_index=True, right_index=True)
fd = pd.merge(fd, GDP['2014'], left_index=True, right_index=True)
fd = pd.merge(fd, Ag['2014'], left_index=True, right_index=True)
fd = pd.merge(fd, co2['2014'], left_index=True, right_index=True)
fd = pd.merge(fd, ec['2014'], left_index=True, right_index=True)
fd.columns = ['Electricity', 'Urban_pop', 'Methane', 'Forest', 'GDP', 'Agri land', 'C02', 'ECP']

plt.figure()

# Calculate the correlation matrix
corr_matrix = fd.corr()

# Create a figure and axis object
fig, ax = plt.subplots()

# Create a heatmap
im = ax.imshow(corr_matrix, cmap='coolwarm')

# Set the ticks and tick labels
ax.set_xticks(range(len(fd.columns)))
ax.set_yticks(range(len(fd.columns)))
ax.set_xticklabels(fd.columns)
ax.set_yticklabels(fd.columns)

# Rotate the tick labels and set them at the center
plt.setp(ax.get_xticklabels(), rotation=45, ha='right',
         rotation_mode='anchor')

# Add the correlation values inside the heatmap
for i in range(len(fd.columns)):
    for j in range(len(fd.columns)):
        text = ax.text(j, i, round(corr_matrix.iloc[i, j], 2),
                       ha="center", va="center", color="w")

# Add a colorbar
cbar = ax.figure.colorbar(im, ax=ax)

# Set the title and show the plot
ax.set_title("Correlation Heatmap")
plt.tight_layout()



plt.show()
