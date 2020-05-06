# Import StratifiedShuffleSplit
from sklearn.model_selection import StratifiedShuffleSplit

# Set the split criteria
split = StratifiedShuffleSplit(n_splits=1, test_size=4)

# Perform data frame split
for x, y in split.split(df, df['product_strata']):
    stratified_random_sample = df.iloc[y].sort_values(by='product_id')

# View sampled data frame
stratified_random_sample

# Obtain the sample mean for each group
stratified_random_sample.groupby('product_strata').mean().drop(['product_id'],axis=1)