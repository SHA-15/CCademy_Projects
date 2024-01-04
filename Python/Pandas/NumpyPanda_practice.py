import numpy as np
import pandas as pd

# The ndarray is a multi-dimensional array object that can store elements of the same data type. It is the core data structure of NumPy and is used for representing vectors, matrices, and higher-dimensional arrays. The dimensions of an array are called axes.

list1 = [1,2,3,4]
array1 = np.array(list1)
#print(array1)

# When creating 2 dimensional arrays, ndarrays provide a clearer demonstration of the dimensions of the array: 3 columns, 2 rows 

list2 = [[1,2,3], [4,5,6]]
array2 = np.array(list2)
#print(array2)

# Mathematical operations can be performed on all values in a ndarray at one time rather than having to loop through values, as is necessary with a python list. This is very helpful in many scenarios.

toyPrices = np.array([5,8,3,6])
#print("Updated Toy Prices: ", toyPrices + 2)



# Create a series using a NumPy array of ages with the default numerical indices
ages = np.array([13,25,19])
series1 = pd.Series(ages)
# print(series1)

# When printing a Series, the data type of its elements is also printed. To customize the indices of a Series object, use the index argument of the Series constructor

ages = np.array([13,25,19])
series1 = pd.Series(ages, index=["Emma", "Swetha", "Serajh"])
# print(series1)

# Another important object in the pandas library is the DataFrame. this object is similar to a matrix as it contains rows and columns. Both rows and columns can be indexed with integers or String names. A DataFrame can contain many different types of data types but within one column a data type must remain the same. 

# A column in a DataFrame is essentially a series. All columns must have the same number of elements. 

# There are different ways to fill a DataFrame such as with a CSV file, a SQL query, a python list, or a dictionary. 

dataf = pd.DataFrame([
["John Smith", "123 Main St", 34],
["Jane Doe", "456 Maple Ave", 28],
["Joe Schmo", "789 Broadway", 51]
], columns = ['name', 'address', 'age'])

# To set the names column as the indices for the DataFrame instead of number indices, the .sex_index() method is used. The method creates a new DataFrame object so use inplace argument to adjust the existing DataFrame object or reassign the variable.

dataf.set_index('name', inplace=True)


print(dataf)

