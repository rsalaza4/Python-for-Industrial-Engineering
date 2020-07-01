### Z chart and MW chart ###

# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import statistics

# Set random seed
np.random.seed(42)

# Define sample number
sample = pd.Series(np.arange(0,16))

# Set readings
X = pd.Series(np.random.normal(loc=39, scale=1, size=16))

# Define the target Xbar
target_x = pd.Series(np.repeat(39,16))

# Define the target Rbar
target_R = pd.Series(np.repeat(0.6,16))

# Create a data frame with the sample number, readings, target Xbar and target Rbar
df = pd.DataFrame({'sample':sample, 'X':X, 'target_Xbar':target_x, 'target_Rbar':target_R})

# Obtain the Z values
df['Z'] = (df['X']-df['target_Xbar'])/df['target_Rbar']

# Define list variable for moving ranges
MW = [np.nan]

# Obtain and append moving ranges
i = 1
for data in range(1, len(df)):
    MW.append(abs(df['Z'][i] - df['Z'][i-1]))
    i += 1
df['MW'] = MW

#Plot Z and MW charts
fig, axs = plt.subplots(2, figsize=(15,15), sharex=True)

axs[0].plot(df['Z'], linestyle='-', marker='o', color='black')
axs[0].axhline(0, color='blue')
axs[0].axhline(2.66, color='red', linestyle='dashed')
axs[0].axhline(-2.66, color='red', linestyle='dashed')
axs[0].set_title('Z Chart')
axs[0].set(xlabel='Sample', ylabel='Z')
axs[0].xaxis.set_major_locator(MaxNLocator(integer=True))
axs[0].yaxis.set_major_locator(MaxNLocator(integer=False))

axs[1].plot(df['MW'], linestyle='-', marker='o', color='black')
axs[1].axhline(1, color='blue')
axs[1].axhline(3.27, color='red', linestyle='dashed')
axs[1].axhline(0, color='red', linestyle='dashed')
axs[1].set_title('MW Chart')
axs[1].set(xlabel='Sample', ylabel='W')

# Validate points out of control limits on Z chart
i = 0
control = True
for Z in df['Z']:
    if Z > 2.66 or Z < -2.66:
        print('Sample', i, 'out of cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All Z points within control limits.')
    
# Validate points out of control limits on MW chart
i = 0
control = True
for MW in df['MW']:
    if MW > 3.27 or MW < 0:
        print('Sample', i, 'out of cotrol limits!')
        control = False
    i += 1    
if control == True:
    print('All MW points within control limits.')
