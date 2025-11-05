import pandas as pd
from matplotlib import pyplot as plt

# Read CSV file into Pandas DataFrame
cities = pd.read_csv('california_cities.csv')
print(cities.info()) # look at columns, dtypes, entries

# Extract data columns for our scatterplot
latitudes = cities['latd'] # y values
longitudes = cities['longd'] # x values
populations = cities['population_total']
area = cities['area_total_sq_mi']
 
 # Generate scatterplot (each city row is dot)
plt.scatter(longitudes, latitudes)
plt.savefig('scatter-cities.png')
plt.close()