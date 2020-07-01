### Z-bar chart and W chart ###

# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import statistics

# Set random seed
np.random.seed(42)

# Define sample number
sample = pd.Series(np.arange(0,12))

# Set part number
part = pd.Series(np.repeat([1,2],6))

# Set readings for parts 1
reading_part_1_x1 = pd.Series(np.random.normal(loc=5, scale=1, size=6))
reading_part_1_x2 = pd.Series(np.random.normal(loc=5, scale=1, size=6))
reading_part_1_x3 = pd.Series(np.random.normal(loc=5, scale=1, size=6))

# Set readings for parts 2
reading_part_2_x1 = pd.Series(np.random.normal(loc=7, scale=1, size=6))
reading_part_2_x2 = pd.Series(np.random.normal(loc=7, scale=1, size=6))
reading_part_2_x3 = pd.Series(np.random.normal(loc=7, scale=1, size=6))

# Concatenate readings for each trial 
x1 = pd.concat([reading_part_1_x1, reading_part_2_x1], ignore_index=True)
x2 = pd.concat([reading_part_1_x2, reading_part_2_x2], ignore_index=True)
x3 = pd.concat([reading_part_1_x3, reading_part_2_x3], ignore_index=True)

# Define the target for each part
target = pd.Series(np.repeat([5,7],6))

# Create a data frame with the sample number, part, target and readings for each trial
df = pd.DataFrame({'sample':sample, 'part':part, 'target_Xbar2':target, 'x1':x1, 'x2':x2, 'x3':x3})

# Obtain the X-bar
df['X-bar'] = df[['x1','x2','x3']].mean(axis=1)

# Obtain the sample range
range = []
for i in df['sample']:
    range.append(max(df['x1'][i],df['x2'][i],df['x3'][i]) - min(df['x1'][i],df['x2'][i],df['x3'][i]))
df['R'] = range

# Define Upper Specification Limit for Part 1
USL_part_1 = 5.5

# Define Lower Specification Limit for Part 1
LSL_part_1 = 4.5

# Define process Cp for part 1
Cp_1 = 1

# Define Upper Specification Limit for Part 2
USL_part_2 = 7.5

# Define Lower Specification Limit for Part 2
LSL_part_2 = 6.5

# Define process Cp for part 2
Cp_2 = 1

# Obtain the target Rbar
target_range_part_1 = pd.Series((np.repeat(1.693*((USL_part_1-LSL_part_1))/(6*Cp_1),6)))
target_range_part_2 = pd.Series((np.repeat(1.693*((USL_part_2-LSL_part_2))/(6*Cp_2),6)))
df['target_Rbar'] = pd.concat([target_range_part_1, target_range_part_2], ignore_index=True)

# Obtain the Z value
df['Z'] = ((df['X-bar']-df['target_Xbar2'])/df['target_Rbar'])

# Obtain the W value
df['W'] = df['target_Rbar']/df['R']

#Plot Zbar and W charts
fig, axs = plt.subplots(2, figsize=(15,15), sharex=True)

axs[0].plot(df['Z'], linestyle='-', marker='o', color='black')
axs[0].axhline(0, color='blue')
axs[0].axhline(1.023, color='red', linestyle='dashed')
axs[0].axhline(-1.023, color='red', linestyle='dashed')
axs[0].set_title('Z-bar Chart')
axs[0].set(xlabel='Sample', ylabel='Z')
axs[0].xaxis.set_major_locator(MaxNLocator(integer=True))
axs[0].yaxis.set_major_locator(MaxNLocator(integer=False))

axs[1].plot(df['W'], linestyle='-', marker='o', color='black')
axs[1].axhline(1, color='blue')
axs[1].axhline(2.574, color='red', linestyle='dashed')
axs[1].axhline(0, color='red', linestyle='dashed')
axs[1].set_title('W Chart')
axs[1].set(xlabel='Sample', ylabel='W')

# Validate points out of control limits on Z-bar chart
i = 0
control = True
for Z in df['Z']:
    if Z > 1.023 or Z < -1.023:
        print('Sample', i, 'out of cotrol limits!')
        control = False
    i += 1    
if control == True:
    print('All Z-bar points within control limits.')
    
# Validate points out of control limits on W chart
i = 0
control = True
for W in df['W']:
    if W > 2.574 or W < 0:
        print('Sample', i, 'out of cotrol limits!')
        control = False
    i += 1    
if control == True:
    print('All W points within control limits.')
