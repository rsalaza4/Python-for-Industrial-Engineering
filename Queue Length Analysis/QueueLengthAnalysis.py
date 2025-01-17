### QUEUE LENGTH ANALYSIS ###

# Import libraries and dependencies
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read csv file
df = pd.read_csv('orders.csv')

# Convert OrderCreatedLocalDateTime column to datetime type
df['OrderCreatedLocalDateTime'] = pd.to_datetime(df['OrderCreatedLocalDateTime'])

# Calculate TimeOutOfQueue column
OrderCreatedORSTTime_column = []
for i in range(len(df)):
    OrderCreatedORSTTime_column.append(df.iloc[i]['OrderCreatedLocalDateTime'] + datetime.timedelta(seconds=int(df.iloc[i]['OrderProcessingTime'])))
df['TimeOutOfQueue'] = OrderCreatedORSTTime_column

# Calculate timeframe from input file on a minute basis
# If the timespan from the source file is less than a day
if (pd.to_datetime(df.iloc[-1,0]) - pd.to_datetime(df.iloc[0,0])).days == 0:
    timeframe = pd.date_range(
        df.iloc[0,0], 
        periods=60*24, 
        freq='1min'
    )
# If the timespan from the source file is more than a day
else:
    timeframe = pd.date_range(
        df.iloc[0,0], 
        periods=(pd.to_datetime(df.iloc[-1,0]) - pd.to_datetime(df.iloc[0,0])).days*60*24, 
        freq='1min'
    )

# Create 'minutes' pandas data frame
minutes_df = pd.DataFrame({'Business Date':timeframe})

# Add Date column
minutes_df['Date'] = minutes_df['Business Date'].dt.date

# Add Time column
minutes_df['Time'] = minutes_df['Business Date'].dt.time

# Initialize date ranges list
date_ranges_list = []

# Loop through all the orders placed on the source file
for i, row in df.iterrows():

    # Get Start/End Time
    enter_t = row["OrderCreatedLocalDateTime"].replace(second=0, microsecond=0)
    exit_t = row["TimeOutOfQueue"].replace(second=0, microsecond=0)

    # Skip orders served within the same minute
    if enter_t == exit_t:
        continue

    # Get the date ranges in minutes between Enter/Exit
    date_range = pd.date_range(
        start=enter_t,
        end=exit_t,
        freq="1min",
        inclusive="right",
    ).tz_localize(None)

    # Append the list of date ranges
    date_ranges_list.append(pd.Series(date_range))

# Accumulate all date ranges
all_date_ranges = pd.concat(date_ranges_list)

# Count the number of occurences for a date/time
orders_counts = all_date_ranges.value_counts().sort_index().to_frame(name="Orders")

# Merge the orders count into the minutes table
minutes_df = pd.merge(
    minutes_df, 
    orders_counts, 
    how="left", 
    left_on="Business Date", 
    right_index=True
)

# Clear empty cells
minutes_df.fillna(0, inplace=True)

# Convert Orders column to int type
minutes_df['Orders'] = minutes_df['Orders'].astype('int')

# Create heatmap
sns.heatmap(minutes_df.groupby([minutes_df['Business Date'].dt.date, minutes_df['Business Date'].dt.strftime('%H:00')])
   ['Orders'].mean()
   .rename_axis(index=['Date','Hour'])
   .unstack(level=0),
    cmap='coolwarm'
)

# Add title
plt.title('Customers in Queue Over Time')

# Show figure
plt.show()
