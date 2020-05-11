### c-chart ###

# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Set random seed
np.random.seed(42)

# Create dummy data
c = {'defects':np.random.randint(0,5,10).tolist(),
    'group_size':np.repeat(10,10).tolist()}

# Convert data to data frame
c = pd.DataFrame(c)

# Plot c-chart
plt.figure(figsize=(15,7.5))
plt.plot(c['defects'], linestyle='-', marker='o', color='black')
plt.axhline(statistics.mean(c['defects'])+3*np.sqrt(statistics.mean(c['defects'])), color='red', linestyle='dashed')
plt.axhline(statistics.mean(c['defects'])-3*np.sqrt(statistics.mean(c['defects'])), color='red', linestyle='dashed')
plt.axhline(statistics.mean(c['defects']), color='blue')
plt.ylim(bottom=0)
plt.title('c Chart')
plt.xlabel('Group')
plt.ylabel('Defect Count')

# Validate points out of control limits
i = 0
control = True
for group in c['defects']:
    if group > statistics.mean(c['defects'])+3*np.sqrt(statistics.mean(c['defects'])) or group < statistics.mean(c['defects'])-3*np.sqrt(statistics.mean(c['defects'])):
        print('Group', i, 'out of defects cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')
