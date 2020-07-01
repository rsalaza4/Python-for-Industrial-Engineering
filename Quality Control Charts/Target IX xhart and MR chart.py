### Target IX chart and MR chart ###

# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import statistics

# Set random seed
np.random.seed(42)

# Define sample number
sample = pd.Series(np.arange(0,18))

# Set part number
part = pd.Series(np.repeat([1,2,3],6))

# Set readings for each part
reading_part_1 = pd.Series(np.random.normal(loc=150, scale=2, size=6))
reading_part_2 = pd.Series(np.random.normal(loc=200, scale=2, size=6))
reading_part_3 = pd.Series(np.random.normal(loc=348, scale=2, size=6))
reading = pd.concat([reading_part_1, reading_part_2, reading_part_3], ignore_index=True)

# Create a data frame with the sample number, part, and readings
df = pd.DataFrame({'sample':sample, 'part':part, 'reading':reading})

# Define the target for each part
df['target'] = pd.Series(np.repeat([150,200,350],6))

# Obtain the deviation from each sample
df['deviation'] = (df['reading'] - df['target'])

# Define list variable for moving ranges
MR = [np.nan]

# Obtain and append moving ranges
for i in range(1,len(df)):
    MR.append(abs(df['deviation'][i] - df['deviation'][i-1]))
    i += 1
df['MR'] = MR

#Plot Target IX and MR charts
fig, axs = plt.subplots(2, figsize=(15,15), sharex=True)

axs[0].plot(df['deviation'], linestyle='-', marker='o', color='black')
axs[0].axhline(0, color='grey')
axs[0].axhline(df['deviation'].mean(), color='blue')
axs[0].axhline(df['deviation'].mean()+(2.66*df['MR'].mean()), color='red', linestyle='dashed')
axs[0].axhline(df['deviation'].mean()-(2.66*df['MR'].mean()), color='red', linestyle='dashed')
axs[0].set_title('Target IX Chart')
axs[0].set(xlabel='Sample', ylabel='Target Deviation')
axs[0].xaxis.set_major_locator(MaxNLocator(integer=True))
axs[0].yaxis.set_major_locator(MaxNLocator(integer=False))

axs[1].plot(df['MR'], linestyle='-', marker='o', color='black')
axs[1].axhline(df['MR'].mean(), color='blue')
axs[1].axhline(df['MR'].mean()*3.267, color='red', linestyle='dashed')
axs[1].axhline(df['MR'].mean()*0, color='red', linestyle='dashed')
axs[1].set_title('MR Chart')
axs[1].set(xlabel='Sample', ylabel='Moving Range')
axs[1].yaxis.set_major_locator(MaxNLocator(integer=False))

# Validate points out of control limits on Target IX chart
i = 0
control = True
for deviation in df['deviation']:
    if deviation > df['deviation'].mean()+(2.66*df['MR'].mean()) or deviation < df['deviation'].mean()-(2.66*df['MR'].mean()):
        print('Sample', i, 'out of cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All Target IX points within control limits.')
    
# Validate points out of control limits on MR chart
i = 0
control = True
for MR in df['MR']:
    if MR > df['MR'].mean()*3.267 or MR < df['MR'].mean()*0:
        print('Sample', i, 'range out of cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All MR points within control limits.')
