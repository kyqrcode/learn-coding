#from Codecademy
#learn modules

import seaborn
import random
from matplotlib import pyplot as plt
# Add your code below:
x_values = range(1, 13)
y_values = list(random.sample(range(1000), 12))

plt.plot(x_values, y_values)
plt.show()