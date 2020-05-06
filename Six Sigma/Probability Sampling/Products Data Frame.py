# Import required libraries
import numpy as np
import pandas as pd

# Set random seed
np.random.seed(42)

# Define total number of products
number_of_products = 10

# Create data dictionary
data = {'product_id':np.arange(1, number_of_products+1).tolist(),
       'measure':np.round(np.random.normal(loc=10, scale=0.5, size=number_of_products),3)}

# Transform dictionary into a data frame
df = pd.DataFrame(data)

# Store the real mean in a separate variable
real_mean = round(df['measure'].mean(),3)

# View data frame
df