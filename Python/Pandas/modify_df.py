# MODIFYING DATAFRAMES 

import pandas as pd

pd.set_option('display.max_columns', None)

# Let's start working with existing DataFrames to understand how to manipulate them.
# We can add columns to existing DataFrames of the same length. This might be to provide extra information or conduct calculations on the existing DataFrame

hardware_df = pd.DataFrame([
    [1, '3 inch screw', 0.5, 0.75],
    [2, '2 inch nail', 0.10, 0.25],
    [3, 'hammer', 3.00, 5.50],
    [4, 'screwdriver', 2.50, 3.00]
], columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price'])

# Add a new column to the existing hardware_df
hardware_df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']

#print(hardware_df)

# Sometimes we want the same value within the column for each row entry, we can achieve this by:

hardware_df['Is taxed?'] = True

#print(hardware_df)

# A column can also be added by performing a function on any column of the DataFrame

hardware_df['Margin'] = hardware_df['Price'] - hardware_df['Cost to Manufacture']

#print(hardware_df)

# The .apply() function allows us to apply a function to every value in a particular column. 

info_df = pd.DataFrame([
    ['JOHN SMITH', 'john.smith@gmail.com'],
    ['Jane Doe', 'jdoe@yahoo.com'],
    ['joe schmo', 'joeschmo@hotmail.com']
], columns=['Name', 'Email'])

# The .apply() function affects the Name column in the info_df DataFrame and str.lower is the string method to create a new column of Lowercase Name that turns all strings to lowercase

info_df['Lowercase Name'] = info_df.Name.apply(str.lower)

#print(info_df)

# In pandas, lambda functions are often introduced to perform calculations/operations on columns

# The .apply() function houses the lambda function. The lambda function returns the email provider from the email for each row entry

info_df['Email Provider'] = info_df['Email'].apply(
    lambda x: x.split('@')[1]
)

#print(info_df)

employee_df = pd.read_csv('employees.csv')

get_last_name = lambda x: x.split(' ')[1]
# Lambda function introduced within the apply() function to create new column
employee_df['last_name'] = employee_df.name.apply(get_last_name)

#print(employee_df.head())

# We can apply lambda functions to multiple columns or along a row
# If we use .apply() with keyword argument axis=1, the input to our lambda function will be an entire row.
# To access particular values of the row , we use row.column_name or row['column_name']

grocery_df = pd.DataFrame([
    ['Apple', 1.00, 'No'],
    ['Milk', 4.20, 'No'],
    ['Paper Towels', 5.00, 'Yes'],
    ['Light Bulbs', 3.75, 'Yes']
], columns=['Item', 'Price', 'Is taxed?'])

grocery_df['Total Price'] = grocery_df.apply(lambda x: x['Price'] * 1.075 if x['Is taxed?'] == 'Yes' else x['Price'], axis=1)

#print(grocery_df)

total_earned = lambda row: row.hourly_wage * (40 + (row.hours_worked - 40) * 1.5) if row.hours_worked > 40 else row.hourly_wage * row.hours_worked

employee_df['total_earned'] = employee_df.apply(total_earned, axis=1)

#print(employee_df.head())

# Sometimes we would like to change the name of the columns to better utilize functionality
# FOR EXAMPLE
name_df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})

name_df.columns = ['First Name', 'Age']

#print(name_df)

imdb_df = pd.read_csv('imdb.csv')
imdb_df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
# print(imdb_df.head())

# Renaming columns can also be done using the .rename() method by passing a dictionary of old and new column names to the columns argument

imdb_df.rename(columns = {
    'Title': 'Movie Title'
}, inplace=True)

#print(imdb_df)