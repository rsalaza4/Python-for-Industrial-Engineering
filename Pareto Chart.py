### PARETO CHART ###

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Build data frame
df = pd.DataFrame({"error": [92, 83, 76, 59, 53, 27, 16, 9, 7, 4, 3, 1]})

# Reset the indexes
df.index = ["Dose missed", "Wrong time", "Wrong drug", "Over dose", "Wrong patient", "Wrong route", "Wrong calculation", "Duplicated drugs", "Under dose", "Wrong IV rate", "Technique error", "Unauthorized drug"]

# Sort values in descending order
df = df.sort_values(by='error', ascending=False)

# Add cumulative percentage column
df["cum_percentage"] = round(df["error"].cumsum()/df["error"].sum()*100,2)

# Set figure and axis
fig, ax = plt.subplots(figsize=(22,10))

# Plot bars (i.e. frequencies)
ax.bar(df.index, df["error"])
ax.set_title("Pareto Chart")
ax.set_xlabel("Medication Error")
ax.set_ylabel("Frequency");

# Second y axis (i.e. cumulative percentage)
ax2 = ax.twinx()
ax2.plot(df.index, df["cum_percentage"], color="red", marker="D", ms=7)
ax2.axhline(80, color="orange", linestyle="dashed")
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.set_ylabel("Cumulative Percentage");

# Display data frame
df
