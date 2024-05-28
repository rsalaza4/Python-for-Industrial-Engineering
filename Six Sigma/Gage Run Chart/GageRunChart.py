### GAGE RUN CHART ###

# Import libraries and dependencies
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Open Excel file
data = pd.read_excel("msa_2_crossed.xlsx")

# Sort values by Part and Operator
data = data.sort_values(["Part","Operator"])

# Reset index
data.reset_index(inplace=True, drop=True)

# Display top rows
data.head()

# Add Replicate column
data["Replicate"] = list(np.arange(1, data["Part"].value_counts()[1]+1))*(int(len(data["Part"])/data["Part"].value_counts()[1]))

# Display top rows
data.head()

# Build seaborn replot
g = sns.relplot(
    data=data,
    x="Replicate",
    y="Value",
    hue="Operator",
    style="Operator",
    col="Part",
    col_wrap=5,
    aspect=0.7
)

# Add subtitle
g.fig.suptitle("Gage Run Chart by Part, Operator", fontsize=16)

# Add horizontal reference line, color, dashes style and axis labels
g.map(plt.axhline, y=data["Value"].mean(), color=".7", dashes=(2, 1), zorder=0).set_axis_labels("Operator", "Value")
