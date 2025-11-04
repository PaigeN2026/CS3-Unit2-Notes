import matplotlib.pyplot as plt
import numpy as np

# Set the style for plots 
plt.style.use('tableau-colorblind10')
print(plt.style.available)

# Use Numpy to generate a sample array of data
x_vals = np.linspace(0, 10, 100)

# LINE PLOTS work well when graphing FUNCTIONS
# for example, y = f(x) or sin/cos/tan
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))
plt.legend()

# Show figure in the dev enviroment
# plt.show()

# Save figure in a PNG file
plt.savefig('lineplot.png')
plt.close() # clear the figure before making another 

# Demo on customization
# Function below: y = 2x
plt.plot(x_vals, 2 * x_vals, '-m')

# Add titles, labels, and legend
plt.title('A Simple Line: y = 2x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend() # not as helpful if you only have one line

plt.savefig('lineplot2.png')
plt.close()