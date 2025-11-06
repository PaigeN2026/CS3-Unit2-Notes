import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

plt.style.use('dark_background')

# Read CSV file into Pandas DataFrame
cities = pd.read_csv('california_cities.csv')
print(cities.info()) # look at columns, dtypes, entries

# Extract data columns for our scatterplot
latitudes = cities['latd'] # y values
longitudes = cities['longd'] # x values
populations = cities['population_total'] # feature shown by COLORS
area = cities['area_total_sq_mi'] # feature shown by SIZE of dots
 
# Generate scatterplot (each city row is dot)
# plt.scatter(longitudes, latitudes)
plt.scatter(longitudes, latitudes, s=area, c=populations, cmap='Spectral', alpha=0.5)

# Customize the appearance of the plot
plt.title('California Cities')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal') # useful for map data

plt.savefig('scatter-cities.png')
plt.close()

# Load Iris flower dataset (from sklearn  package)
iris = load_iris()
# print(iris) # 'feature_names': ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
features = iris.data.T # transpose the data (switch rows & cols)
plt.scatter(features[0], features[1], s=features[3]*100, c=iris.target, cmap='viridis', alpha=0.5)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.savefig('iris-scatter.png')