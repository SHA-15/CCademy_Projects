# PANDAS COMMANDS TO WORK WITH MULTIPLE TABLES

import pandas as pd

# In order to efficiently store data, we often spread related information across multiple tables
# We will deep dive into Pandas commands that help us work with data stored in multiple tables

# The .merge() method looks for columns that are common between two DataFrames and then looks for rows where those column's values are the same. It then combines the matching rows into a single row in a new table
# new_df = pd.merge(first_df, second_df)

sales = pd.read_csv('sales.csv')
targets = pd.read_csv('targets.csv')

#print(sales)
#print(targets)

sales_v_targets = pd.merge(sales, targets)
#print(sales_v_targets)

exceeding_targets = sales_v_targets[sales_v_targets.revenue > sales_v_targets.target]
#print(exceeding_targets)

# In addition to pd.merge(), each DataFrame has its own .merge() method

men_women_sales = pd.read_csv('men_women_sales.csv')
#print(men_women_sales)

all_data = sales.merge(targets).merge(men_women_sales)
#print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]
#print(results)

# Merging while renaming columns

orders = pd.read_csv('merge_df/orders.csv')
products = pd.read_csv('merge_df/products.csv')

#print(orders)
#print(products)

order_products = pd.merge(orders, products.rename(
    columns={
        'id': 'product_id'
    }
)).reset_index(drop=True)

#print(order_products)

# Another way of merging columns is to specify which columns to merge on using left_on, right_on
# pd.merge(left_df, right_df, left_on = left_df_column, right_on = right_df_column)
# If we use this syntax, we will end up with two same named columns, Pandas hence changes them to column_x and column_y
# We can change the _x and _y by including a suffixes argument to reflect table names
# pd.merge(left_df, right_df, left_on = "left_df_column", right_on = "right_df_column", suffixes = ['_order', '_customer'])

order_products = pd.merge(
    orders,
    products,
    left_on = 'product_id',
    right_on = 'id',
    suffixes = ['_orders','_products']
)

#print(order_products)

# INNER MERGE is a type of merge where any mismatched data of DataFrames during the merge is excluded in the merged DataFrame
# OUTER JOIN includes all rows from both tables, even if they don't match. Any missing values are replaced with NaN or None
# pd.merge(df_A, df_B, how = 'outer')

store_a = pd.read_csv('merge_df/store_a.csv')
store_b = pd.read_csv('merge_df/store_b.csv')

# Store a and b outer merge
store_a_b = pd.merge(store_a, store_b, how='outer')
#print(store_a_b)

# LEFT MERGE: A left merge includes all rows from the first table, but only rows from the second table that match the first table
# RIGHT MERGE: A right merge is the complete opposite of a left merge. 

store_a_b_left = pd.merge(store_a, store_b, how='left')
#print(store_a_b_left)

store_a_b_right  = pd.merge(store_a, store_b, how='right')
#print(store_a_b_right)

# CONCATENATE DATAFRAMES: When a dataset is broken into multiple tables, we need to reconstruct a single dataframe from multiple dataframes. 
# pd.concat([df1, df2,...])