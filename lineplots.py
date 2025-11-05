import matplotlib.pyplot as plt
import numpy as np

# Set the style for plots 
plt.style.use('tableau-colorblind10')
print(plt.style.available)

# Use Numpy to generate a sample array of data
x_vals = np.linspace(0, 10, 100)

# LINE PLOTS work well when graphing FUNCTIONS
# for example, y = f(x) or sin/cos/tan
plt.plot(x_vals, np.sin(x_vals), label='y = sin(x)')
plt.plot(x_vals, np.cos(x_vals), label='y = cos(x)')
plt.legend()

# Show figure in the dev enviroment
# plt.show()

# Save figure in a PNG file
plt.legend()
plt.savefig('lineplot.png')
plt.close() # clear the figure before making another 

# Demo on customization
# Function below: y = mx + b
m = 2 # slope(rise / run)
b = 10 # y-intercept 
plt.plot(x_vals, (m * x_vals + b), label='y=2x+10', color='g')
plt.plot(x_vals, 3 * x_vals, label='y=3x', color='#689e85')
plt.plot(x_vals, (0.5 * x_vals + 2), label='y=1/2x+2', linestyle='dashed', color='#789e68')
plt.plot(x_vals, (6 * x_vals + 7), label='y=6x+7', linestyle='dashdot', color='#caf5b8')
plt.plot(x_vals, (4 * x_vals + 1 ), label='y=4x+1', linestyle='dotted', color='#5d803e')

# Add titles, labels, and legend
plt.title('Linear Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend() # not as helpful if you only have one line

plt.savefig('lineplot2.png')
plt.close()