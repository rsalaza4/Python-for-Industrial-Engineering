# Obtain simple random sample
simple_random_sample = df.sample(n=4).sort_values(by='product_id')

# Save the sample mean in a separate variable
simple_random_mean = round(simple_random_sample['measure'].mean(),3)

# View sampled data frame
simple_random_sample