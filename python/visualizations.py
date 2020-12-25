from random import seed
from random import randint
from numpy.random import randn
from numpy import sin
import matplotlib.pyplot as plt

seed(1)

#### LINE PLOT ####

# Consistent interval for x-axis
x = [x * 0.1 for x in range(100)]

# Function of x for y-axis
y = sin(x)

# Create and Show Line Plot
plt.plot(x, y)
plt.show()

#### BAR CHART ####

# Names for categories
x = ['red', 'green', 'blue']

# Quantities for each category
y = [randint(0, 100), randint(0, 100), randint(0, 100)]

# Create and Show Bar Chart
plt.bar(x, y)
plt.show()

#### HISTOGRAM PLOT ####

# Random numbers drawn from a Gaussian distribution
x = randn(1000)

# Create and Show Histogram Plot
plt.hist(x, bins=100)
plt.show()

#### BOX AND WHISHER PLOT ####

# Random numbers drawn slightly different Gaussian distributions
x = [randn(1000), 5 * randn(1000), 10 * randn(1000)]

# Create and Show Box and Whisker Plot
plt.boxplot(x)
plt.show()

#### SCATTER PLOT ####

# First variable
x = 20 * randn(1000) + 100

# Second variable
y = x + (10 * randn(1000) + 50)

# Create and Show Scatter Plot
plt.scatter(x, y)
plt.show()
