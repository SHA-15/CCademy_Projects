# When we have a bunch of data, we like to perform aggregates (mean, median, standard deviation) over certain subsets of data.
# The method .groupby() allows us to identify certain subsets of data for which we can perform our aggregate calculations across a DataFrame
# The general syntax is, df.groupby('column1').column2.measurement()

import pandas as pd
import numpy as np 

orders = pd.read_csv('orders.csv')

# Identify the max price of the shoes by each shoe type

pricey_shoes = orders.groupby('shoe_type').price.max()

print(pricey_shoes)
#print(type(pricey_shoes))

# After using groupby, we often need to clean our data. As each groupby object creates a new Series, the indices of the Series were the groupby values (such as 'shoe_type') and price being our column of values
# To convert these indices into values, we can use reset_index(). This will transform the series into a DataFrame
# The syntax is, df.groupby(column1).column2.measurement().reset_index()

# Let us modify our previous example by including reset_index() in the calculation
reset_series_shoes = orders.groupby('shoe_type').price.max().reset_index()

print(reset_series_shoes)
#print(type(reset_series_shoes))

# Sometimes the calculation is more complicated than mean or count. We can use the apply() method and lambda functions. The input to a lambda function will always be a list of values


cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()

#print(cheap_shoes)

# Sometimes we want to group by more than one column. we can easily do this by passing a list of column names into the groupby method. 

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts.rename(columns={
    'id' : 'Articles Sold'
}, inplace = True)

#print(shoe_counts)

# PIVOT TABLES
# The DataFrame presented previously can be formatted to provide clarity on the data, this can be done by pivoting columns and values for better visualization.
# The syntax is pivot_df = df.pivot(columns = 'Column to Pivot', index = 'Index to Pivot', value = 'Values to Pivot').reset_index()

pivot_counts = shoe_counts.pivot(
    columns = 'shoe_color',
    index = 'shoe_type',
    # Values field changed due to renaming of column header
    values = 'Articles Sold'
).reset_index()

print(pivot_counts)
