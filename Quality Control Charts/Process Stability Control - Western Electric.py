### PROCESS STABILITY CONTROL ###
                                                                                                         
# CONTROL CHART RULES:                                                                                    
                                                                                                       
#   Rule #1: Beyond limits - one or more points are beyond the control limits                                    
#   Rule #2: Zone A - 2 consecutive points in Zone A or beyond                                     
#   Rule #3: Zone B - 4 out of 5 consecutive points in Zone B or beyond                                       
#   Rule #4: Zone C - 8 or more consecutive points on one side of the center line (in Zone C or beyond)                                            

# Import required libraries
import numpy as np
import pandas as pd
import statistics
import hvplot
import hvplot.pandas

# Set a random seed
np.random.seed(42)

# Define sample size
sample_size=5

# Generate normal distributed measures
data = np.round(np.random.normal(loc=50, scale=25, size=100),2)

# Generate sample groups
sample_group = np.repeat(range(1,21),sample_size)

# Define data frame
df = pd.DataFrame({'data':data, 'sample_group':sample_group})
df.head()

# Group masures by sample groups (x_bar)
df_grouped = df.groupby('sample_group').mean()

# Rename x-bar column
df_grouped.columns = ['x_bar']
df_grouped.head()

# Add R (range) column
df_max = df.groupby('sample_group').max()
df_min = df.groupby('sample_group').min()
df_grouped['R'] = df_max['data'] - df_min['data']
df_grouped.head()

# Get control limits
df_grouped['x_bar_bar'] = statistics.mean(df_grouped['x_bar'])
df_grouped['UCL'] = statistics.mean(df_grouped['x_bar'])+(0.577*statistics.mean(df_grouped['R']))
df_grouped['+2s'] = (df_grouped['UCL']-df_grouped['x_bar_bar'])/3*2+df_grouped['x_bar_bar']
df_grouped['+1s'] = (df_grouped['UCL']-df_grouped['x_bar_bar'])/3*1+df_grouped['x_bar_bar']
df_grouped['-1s'] = df_grouped['x_bar_bar']-(df_grouped['UCL']-df_grouped['x_bar_bar'])/3*1
df_grouped['-2s'] = df_grouped['x_bar_bar']- (df_grouped['UCL']-df_grouped['x_bar_bar'])/3*2
df_grouped['LCL'] = statistics.mean(df_grouped['x_bar'])-(0.577*statistics.mean(df_grouped['R']))
df_grouped.head()

# Plot x-bar control chart

# Line chart
line_plot = df_grouped.hvplot.line(
x='sample_group',
y=['x_bar','UCL','+2s','+1s','x_bar_bar','-1s','-2s','LCL'],
xlabel="Sample Group",
title="x-bar chart",
height=500,
width=1000)

# Scatter plot
scatter_plot = df_grouped.hvplot.scatter(
x='sample_group',
y=['x_bar','UCL','+2s','+1s','x_bar_bar','-1s','-2s','LCL'],
xlabel="Sample Group",
title="x-bar chart",
height=500,
width=1000)

# Merge line chart and scatter plot into a single plot
x_bar_chart = line_plot*scatter_plot
x_bar_chart

# Control chart rules lists setup
R1_lower = []
R1_upper = []
R2_lower = ['-']
R2_upper = ['-']
R3_lower = ['-','-','-','-']
R3_upper = ['-','-','-','-']
R4_lower = ['-','-','-','-','-','-','-']
R4_upper = ['-','-','-','-','-','-','-']

# Rule 1 - Lower
for x in df_grouped['x_bar']:
    if x < df_grouped['LCL'][1]:
        R1_lower.append(False)
    else:
        R1_lower.append(True)
        
# Rule 1 - Upper
for x in df_grouped['x_bar']:
    if x > df_grouped['UCL'][1]:
        R1_upper.append(False)
    else:
        R1_upper.append(True)
        
# Rule 2 - Lower
for i in range(2,len(df_grouped)+1):
    if df_grouped["x_bar"][i] < df_grouped["-2s"][i] and df_grouped["x_bar"][i-1] < df_grouped["-2s"][i-1]:
        R2_lower.append(False)
    else:
        R2_lower.append(True)
        
# Rule 2 - Upper
for i in range(2,len(df_grouped)+1):
    if df_grouped["x_bar"][i] > df_grouped["+2s"][i] and df_grouped["x_bar"][i-1] > df_grouped["+2s"][i-1]:
        R2_upper.append(False)
    else:
        R2_upper.append(True)
        
# Rule 3 - Lower
for i in range(5, len(df_grouped['x_bar'])+1): 
    if((df_grouped['x_bar'][i-4] < df_grouped['-1s'][i-4] and df_grouped['x_bar'][i-3] < df_grouped['-1s'][i-3] and df_grouped['x_bar'][i-2] < df_grouped['-1s'][i-2] and df_grouped['x_bar'][i-1] < df_grouped['-1s'][i-1]) or
       (df_grouped['x_bar'][i-4] < df_grouped['-1s'][i-4] and df_grouped['x_bar'][i-3] < df_grouped['-1s'][i-3] and df_grouped['x_bar'][i-2] < df_grouped['-1s'][i-2] and df_grouped['x_bar'][i] < df_grouped['-1s'][i]) or
       (df_grouped['x_bar'][i-4] < df_grouped['-1s'][i-4] and df_grouped['x_bar'][i-2] < df_grouped['-1s'][i-2] and df_grouped['x_bar'][i-1] < df_grouped['-1s'][i-1] and df_grouped['x_bar'][i] < df_grouped['-1s'][i]) or
       (df_grouped['x_bar'][i-4] < df_grouped['-1s'][i-4] and df_grouped['x_bar'][i-3] < df_grouped['-1s'][i-3] and df_grouped['x_bar'][i-1] < df_grouped['-1s'][i-1] and df_grouped['x_bar'][i] < df_grouped['-1s'][i]) or
       (df_grouped['x_bar'][i-3] < df_grouped['-1s'][i-3] and df_grouped['x_bar'][i-2] < df_grouped['-1s'][i-2] and df_grouped['x_bar'][i-1] < df_grouped['-1s'][i-1] and df_grouped['x_bar'][i] < df_grouped['-1s'][i])):
        R3_lower.append(False)
    else:
        R3_lower.append(True)
    i+=1
    
# Rule 3 - Upper
for i in range(5, len(df_grouped['x_bar'])+1): 
    if((df_grouped['x_bar'][i-4] > df_grouped['+1s'][i-4] and df_grouped['x_bar'][i-3] > df_grouped['+1s'][i-3] and df_grouped['x_bar'][i-2] > df_grouped['+1s'][i-2] and df_grouped['x_bar'][i-1] > df_grouped['+1s'][i-1]) or
       (df_grouped['x_bar'][i-4] > df_grouped['+1s'][i-4] and df_grouped['x_bar'][i-3] > df_grouped['+1s'][i-3] and df_grouped['x_bar'][i-2] > df_grouped['+1s'][i-2] and df_grouped['x_bar'][i] > df_grouped['+1s'][i]) or
       (df_grouped['x_bar'][i-4] > df_grouped['+1s'][i-4] and df_grouped['x_bar'][i-2] > df_grouped['+1s'][i-2] and df_grouped['x_bar'][i-1] > df_grouped['+1s'][i-1] and df_grouped['x_bar'][i] > df_grouped['+1s'][i]) or
       (df_grouped['x_bar'][i-4] > df_grouped['+1s'][i-4] and df_grouped['x_bar'][i-3] > df_grouped['+1s'][i-3] and df_grouped['x_bar'][i-1] > df_grouped['+1s'][i-1] and df_grouped['x_bar'][i] > df_grouped['+1s'][i]) or
       (df_grouped['x_bar'][i-3] > df_grouped['+1s'][i-3] and df_grouped['x_bar'][i-2] > df_grouped['+1s'][i-2] and df_grouped['x_bar'][i-1] > df_grouped['+1s'][i-1] and df_grouped['x_bar'][i] > df_grouped['+1s'][i])):
        R3_upper.append(False)
    else:
        R3_upper.append(True)
    i+=1

# Rule 4 - Lower
for i in range(8,len(df_grouped)+1):
    if (df_grouped["x_bar"][i-8:i] < df_grouped["x_bar_bar"][1]).all():
        R4_lower.append(False)
    else:
        R4_lower.append(True)
        
# Rule 4 - Upper
for i in range(8,len(df_grouped)+1):
    if (df_grouped["x_bar"][i-8:i] > df_grouped["x_bar_bar"][1]).all():
        R4_upper.append(False)
    else:
        R4_upper.append(True)
        
# Define outcomes data frame
analysis = pd.DataFrame({'R1_lower':R1_lower,
                        'R1_upper':R1_upper,
                        'R2_lower':R2_lower,
                        'R2_upper':R2_upper,
                        'R3_lower':R3_lower,
                        'R3_upper':R3_upper,
                        'R4_lower':R4_lower,
                        'R4_upper':R4_upper})

analysis.index = df_grouped.index
analysis        

# Look for at least one False value in each of the control chart rules
analysis.all()
