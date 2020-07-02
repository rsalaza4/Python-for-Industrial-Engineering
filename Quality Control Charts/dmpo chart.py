### dpmo chart ###

# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import statistics

# Set random seed
np.random.seed(42)

# Define sample size
sample_size = 10

# Set the opportunities for defects per unit
defects_opportunities = 2751

# Define sample number
sample = pd.Series(np.arange(0,40))

# Specify the number of defects found per sample
defects_found = pd.Series(np.random.randint(0,7,40))

# Obtain the defects per unit
dpu = defects_found/sample_size

# Obtain the defects per million opportunities
dpmo = (dpu/defects_opportunities)*1000000

# Create a data frame with the sample number, defects found, dpu and dpmo
df = pd.DataFrame({'sample_number':sample, 'defects_found':defects_found, 'dpu':dpu, 'dpmo':dpmo})

# Plot dpmo chart
plt.figure(figsize=(15,7.5))
plt.plot(df['dpmo'], linestyle='-', marker='o', color='black')
plt.axhline(statistics.mean(df['dpmo']), color='blue')
plt.axhline(statistics.mean(df['dpmo'])+3000*(np.sqrt((statistics.mean(df['dpmo']/(sample_size*defects_opportunities))))), color='red', linestyle='dashed')
plt.axhline(max(0,statistics.mean(df['dpmo'])-3000*(np.sqrt((statistics.mean(df['dpmo']/(sample_size*defects_opportunities)))))), color='red', linestyle='dashed')
plt.title('dpmo Chart')
plt.xlabel('Sample')
plt.ylabel('Defects per Million Opportunities')

# Validate points out of control limits
i = 0
control = True
for dpmo in df['dpmo']:
    if dpmo > statistics.mean(df['dpmo'])+3000*(np.sqrt((statistics.mean(df['dpmo']/(sample_size*defects_opportunities))))) or dpmo < max(0,statistics.mean(df['dpmo'])-3000*(np.sqrt((statistics.mean(df['dpmo']/(sample_size*defects_opportunities)))))):
        print('Sample', i, 'out of cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All dpmo points within control limits.')
