### RELIABILITY ANALYSIS - SERIAL SYSTEMS ###

# Import required libraries
import path
import numpy as np
import pandas as pd
import reliability
from reliability.Fitters import Fit_Everything

# Load data
Path = "failure_times.csv"
df = pd.read_csv(Path)
df.head()

# Get summary statistics
df.describe()

# Get the number of components in series to be analyzed
number_of_components = len(df.columns)
print(f"Number of components to be analyzed: {number_of_components}\n")

# Create a list to store the components individual reliabilities
reliabilities = []

# Create a list to store the reliabilities times of interest for each component
times = []

# Iterate over each component (i.e. column from the dataframe) and determine its realibility at time 't'
for i in range(len(df.columns)):
     
    # Data Validation
    # Validate that there are no negative failure times
    error = False
    for data_point in df.iloc[:,i]:
        if data_point < 0:
            error = True
    
    # Print error message if at least one negative failure time is present for the given component
    if error == True:
        print(f"Error: {df.columns[i]} has at least one negative failure time. Negative values are not accepted. The analysis cannot move forward.")
    
    # Perform reliability analysis
    if error == False:
        
        # Print component being analyzed
        print(f"Reliability analysis {df.columns[i]}:\n")
        
        # Fit all probability distributions available from 'reliability' library
        output = Fit_Everything(failures=df.iloc[:,i].dropna().tolist(), show_probability_plot=False, show_PP_plot=False)
        
        # Define the probability distribution that best fitted the failure times for the given component
        output.best_distribution.plot()
           
        # Define the desired time of failure 't'
        t = float(input("Type in the desired time before failure: "))
        
        # Time 't' validation
        # Validate that no negative time was inserted
        while t<0 :
            print("Error: negative value insterted. Please insert a positive value greater than 0:")
            t = float(input("Type in the desired time before failure: "))

        # If the best fitted distribution was Beta with 2 parameters, the time 't' cannot be greater than 1
        if output.best_distribution_name == 'Beta_2P':
            while t>1:
                print("Error: for Beta distributions the range of the values must be within 0 and 1.")
                t = float(input("Type in the desired time before failure: "))
        
        # Append failure time in times list
        times.append(t)
                
        # Get component reliability
        component_reliability = output.best_distribution.SF(t)
        
        # Append component reliability in reliabilities list
        reliabilities.append(component_reliability)
     
        print("\n--------------------------------------------------------------------------------------------------------------------\n")

# Calculate the system reliability
system_reliability = np.prod(reliabilities)

# Print system reliability result
print(f"RESULTS:\n\nSystem Reliability for {len(df.columns)} components in series: {round(system_reliability*100,2)}%")
print("")

# Print system components individual reliabilities
for i in range(len(reliabilities)):
    print(f"Reliability of {df.columns[i]} at time {times[i]}: {round(reliabilities[i]*100,2)}%")
