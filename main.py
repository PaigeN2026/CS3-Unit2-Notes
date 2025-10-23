import numpy as np
import pandas as pd

# Series object is a 1D array of indexed data
# Like a COLUMN (one category)
month = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
print(month)

print(" ")
# Series have attributes values & index
print(month.values) # looks like a list
print(month.index) # shows the range of nums

print(" ")

# You can set the index explicitly! 
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
better_month = pd.Series(month_list, index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(better_month)

print(" ")

# Access value at index 
print(f' My birthday is in {better_month[2]}')

print(" ")

# Can also think of Series like a simple dictionary with key:value pairs 
birth_months = {'Kevin': 'Mar',
                'Jackson': 'Aug',
                'Finny': 'Jul',
                'Bryce': 'Nov',
                'Natalie': 'Mar',
                'Paige': 'Feb',
                'Maia': 'Apr'}
birth_series = pd.Series(birth_months)
print(birth_series)

print(" ")

# Create a DataFrame from a dictionary
df = pd.DataFrame(birth_series, columns=['Birth Month'])
print(df) # DataFrame objects have column headers!

print(" ")

# Load tabular data from a CSV file into a DataFrame
pokemon_df = pd.read_csv('pokemon_data.csv')
print(pokemon_df) # [800 rows x 12 cols]
print(pokemon_df.columns) # display col headers

print(" ")

# Column headers can be used to access individual columns 
print(pokemon_df['Name'])

print(" ")

# Shortcut using DOT OPERATOR notation
print(pokemon_df.HP)

print(" ")

# Shortcut does not work for all column names...
# print(pokemon_df.Type 1) 
print(pokemon_df['Type 1'])

print(" ")

# Add a new column 
pokemon_df['Attack Ration'] = pokemon_df['Attack'] / pokemon_df['Sp. Atk']

# Examples of getting info about a DataFrame
print(pokemon_df.head(10)) # show first n rows

print(" ")

print(pokemon_df.sample(3)) # show random sample of n rows 

print(" ")

print(pokemon_df.shape) # returns a tuple (rows, cols)

print(" ")

print(pokemon_df.columns) # returns a list of column headers

print(" ")

print(pokemon_df.info()) # shows non-null count & dtypes 

print(" ")

print(pokemon_df.describe()) # mean, std, min, max

print(" ")

print(pokemon_df['Defense'].describe()) # stats for a specific col

print(" ")

print(pokemon_df['Type 1'].value_counts()) # frequency of value counts 

print(" ")

# How to locate specific rows
print(pokemon_df.loc[4]) # gives you charmander

print(" ")

# groupby function helps you isolate groups of entries
print(pokemon_df.groupby('Type 1')[['HP', 'Speed']].mean())

print(" ")

# Similar to value_counts
print(pokemon_df.groupby('Type 1').size().sort_values(ascending=False)) 

print(" ")

# Average combined stats by generation
pokemon_df['Total'] = pokemon_df[['HP', 'Attack', 'Defense', 'Speed']].sum(axis=1)
print(pokemon_df['Total'])

print(" ")

#Which generation has the strongest pokemon?
print(pokemon_df.groupby('Generation')['Total'].mean()) 

print(" ")

# Copare legendary pokemon to non-legendary
print(pokemon_df.groupby('Legendary')['Total'].mean())

print(" ")

# CONDITIONAL FILTERING

# Select Pokemon with HP greater than 100
# Pulling ROWS (entries) where the value in the 'HP' COLUMN > 100
subset1 = pokemon_df[pokemon_df['HP'] > 100]

# Select Poison-type
subset2 = pokemon_df[pokemon_df['Type 1'] == 'Poison']
print(subset2)

print(" ")

# Compound operators -> and is &, or is | for Pandas
# First condition: poisin pokemon that are not also flying type
# Second condition: AND before gen 5
subset3 = subset2[(subset2['Type 2'] != 'Flying') & (subset2['Generation'] < 5)]
print(subset3)

print(" ")

# Select pokemon whose name contains 'Mega
subset4 = pokemon_df[pokemon_df['Name'].str.contains('Mega')]
print(subset4)

# Exclude Legendary Pokemon
subset5 = pokemon_df[pokemon_df['Legendary'] == False]
# OR you could do the same thing like this:
subset6 = pokemon_df[~pokemon_df['Legendary']]