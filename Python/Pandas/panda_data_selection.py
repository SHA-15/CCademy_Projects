# Pandas is a python module for working with tabular data (i.e. data in a table with rows and columns)

# Pandas are imported under the alias pd
import pandas as pd

# The pd.set_option command prevents the terminal to truncate the results and outputs all columns and rows

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# A DataFrame is an object that stores data as rows and columns. You can manually create a DataFrame or fill it with data from a CSV, an Excel spreadsheet, or a SQL query.

# DataFrames can contain many different datatypes such as ints, floats, strings, tuples etc.

# You can a pass a dictionary to pd.DataFrame(). Each key in a dictionary is a column name, and each value is a list of column values.
# Each and every column value must be of the same length or an error will be generated.

df_dict = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})

#print(df_dict)

# A DataFrame can also be created using Lists
# A List of lists can be passed on, where each list acts as a row of data
# the keyword argument columns is passed to name the column headers

df_lists = pd.DataFrame([    
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns = ['name', 'address', 'age']
)

#print(df_lists)

# When you have data in a CSV, you can load it into a DataFrame in Pandas using .read_csv()

df_csv = pd.read_csv('read_csv.csv')
# print(df_csv)

# When loading a new DataFrame from a csv. To inspect a Larger DataFrame, it is better to inspect a few items, without having to look at the entire DataFrame

# the .head() method prints the first 5 rows of a DataFrame. If you want to see more rows, the argument (n) can provide a cutom number of rows to be displayed

df_imdb = pd.read_csv('imdb.csv')

#print(df_imdb.head())
#print(df_imdb)

# The method .info() provides statistics for the DataFrame and each column

#print(df_imdb.info())

# Having been able to create and load DataFrames, it is important to know how to select columns from a DataFrame to conduct analysis

# There are two possible methods:
#1. Select the column as if you were selecting dictionary values using a key: df_imdb['genre']
#2. If a column name follows the rules of the variable nomenclature: df_imdb.genre

df_columns = pd.DataFrame([
    ['January', 100, 100, 23, 100],
    ['February', 51, 45, 145, 45],
    ['March', 81, 96, 65, 96],
    ['April', 80, 80, 54, 180],
    ['May', 51, 54, 54, 154],
    ['June', 112, 109, 79, 129]
], columns=['month', 'clinic_east', 'clinic_north', 'clinic_south', 'clinic_west'])

# To select clinic_north columns all data values
clinic_north = df_columns.clinic_north

# To select clinic_east columns all data values
clinic_east = df_columns['clinic_east']

#print(type(clinic_north))
#print(type(clinic_east))
#print(clinic_north, clinic_east)

# With a Larger DataFrame you will want to select a few columns
# To Select two or more columns from a DataFrame, we use a list of column names
# But this method uses [[]] double brackets otherwise the command won't work!

shortened_df_columns = df_columns[['clinic_north', 'clinic_south']]

#print(shortened_df_columns)

# To select a particular row of data, we use the .iloc() method along with the index passed in as the argument. DataFrames are zero-indexed
# Note, when we select a single row, the result is a Series (just like when we select a single Column)

march_data = df_columns.iloc[2]
#print(march_data)

# To select multiple rows, iloc method offers row slicing mechanism to gather mutliple rows

april_may_june_data = df_columns.iloc[-3:]
#print(april_may_june_data)


#---------------------------- SELECT ROWS WITH LOGIC-------------------------------#

# Logical statements can be used to select a subsection of a DataFrame
# df[df.ColumnName == desired_column_value]

january_row = df_columns[df_columns.month == 'January']
#print(january_row)

# Multiple logic statements can also be combined with "and(&)" and "or (|)", as long as each statement is within their parentheses.

march_april_data = df_columns[(df_columns.month == 'March') | (df_columns.month == 'April')]
#print(march_april_data)

# Another method of selecting rows with logic is with the .isin() method applied on the column of the DataFrame

jan_feb_mar = df_columns[df_columns.month.isin(['January', 'February', 'March'])]
#print(jan_feb_mar)


# While working with large DataFrames and selecting a subset of the DataFrames, we end up with non-consecutive indices. This is inelegent and makes it hard to use .iloc[]

# The sub-set indices can be fixed with .reset_index() method. However the reset_index() method will produce a new DataFrame object with the old index as a separate column

# .loc[] method is a label-based indexing method

reset_index_column = df_columns.iloc[[1,3,5]]

# The reset_index produced a new DataFrame Object
reset_index_column_updated = reset_index_column.reset_index()

#print(reset_index_column)
#print(reset_index_column_updated)

# If we use the keyword argument drop=True , we will have removed the old index column in the reset_index DataFrame object
# If we use the keyword argument inplace0True, we will have no need for a new dataFrame object

reset_index_column.reset_index(inplace=True, drop=True)

#print(reset_index_column)

# In both cases, a new DataFrame index is introduced, but keyword arguments help to cleanup the new DF without having to use more memory and dealing with old indices.

# x-------------REVIEW---------------------x
#Load shoefly.csv in python file
orders = pd.read_csv('shoefly.csv')

#Inspect the first five lines of code
#print(orders.head())

# Select all the emails from the column emails
emails = orders.email

# Find Frances Palmer and her order 
frances_palmer = orders[(orders.first_name == "Frances") & (orders.last_name == "Palmer")]

# Select orders by shoe_type
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]

#print(comfy_shoes)
