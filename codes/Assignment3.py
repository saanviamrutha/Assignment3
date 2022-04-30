import numpy as np
import statistics as stat
#Substitute x = 63 in the given data. Then the data becomes: 29,32,48,50,63,65,72,78,84,95.
observations = np.array([29,32,48,50,63,65,72,78,84,95])
median = stat.median(observations)
#Printing the given median as output.
print(median)

