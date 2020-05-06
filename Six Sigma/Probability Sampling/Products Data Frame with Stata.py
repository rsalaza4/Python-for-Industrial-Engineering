# Create data dictionary
data = {'product_id':np.arange(1, number_of_products+1).tolist(),
       'product_strata':np.repeat([1,2], number_of_products/2).tolist(),
       'measure':np.round(np.random.normal(loc=10, scale=0.5, size=number_of_products),3)}

# Transform dictionary into a data frame
df = pd.DataFrame(data)

# View data frame
df