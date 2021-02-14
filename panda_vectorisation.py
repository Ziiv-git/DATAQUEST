# Because pandas is an extension of NumPy, it also supports vectorized operations.

Just like with NumPy, we can use any of the standard Python numeric operators with series, including:

series_a + series_b - Addition
series_a - series_b - Subtraction
series_a * series_b - Multiplication (this is unrelated to the multiplications used in linear algebra).
series_a / series_b - Division

rank_change = f500['previous_rank'] - f500['rank']
print(rank_change)

Like NumPy, pandas supports many descriptive stats methods that can help us answer these questions. Here are a few of the most useful ones (with links to documentation):

Series.max()
Series.min()
Series.mean()
Series.median()
Series.mode()
Series.sum()

rank_change =  f500["previous_rank"] - f500["rank"]
rank_change_max = rank_change.max()
print(rank_change_max)
rank_change_min = rank_change.min()
print(rank_change_min)

Next, we'll learn another method that can help us more quickly investigate this issue - the Series.describe() method.
This method tells us how many non-null values are contained in the series, along with the mean, minimum, maximum, and other
statistics we'll learn about later in this path.

country = f500["country"]
print(country.describe())

count     500
unique     34
top       USA
freq      132
Name: country, dtype: object

The first statistic, count, is the same as for numeric columns, showing us the number of non-null values. The other three statistics are new:

unique: Number of unique values in the series. In this case, it tells us that there are 34 different countries represented in the Fortune 500.
top: Most common value in the series. The USA is the country that headquarters the most Fortune 500 companies.
freq: Frequency of the most common value. Exactly 132 companies from the Fortune 500 are headquartered in the USA.


This is called method chaining — a way to combine multiple methods together in a single line.

# Use Series.value_counts() and Series.loc to return the number of companies with a value of 0 in the previous_rank column in the f500 dataframe. Assign the results to zero_previous_rank.
zero_previous_rank = f500['previous_rank'].value_counts().loc[0]
print(zero_previous_rank)


Because series and dataframes are two distinct objects, they have their own unique methods.
However, there are many times where both series and dataframe objects have a method of the same name that behaves in similar ways.
Below are some examples:

Series.max() and DataFrame.max()
Series.min() and DataFrame.min()
Series.mean() and DataFrame.mean()
Series.median() and DataFrame.median()
Series.mode() and DataFrame.mode()
Series.sum() and DataFrame.sum()

medians = f500[["revenues", "profits"]].median(axis=0)
# we could also use .median(axis="index")
print(medians)


# Use the DataFrame.max() method to find the maximum value for only the numeric columns from f500 (you may need to check the documentation). Assign the result to the variable max_f500.
max_f500 = f500.max(numeric_only=True)
print(max_f500)


# The company "Dow Chemical" has named a new CEO. Update the value where the row label is Dow Chemical and for the ceo column to Jim Fitterling in the f500 dataframe.
company_change = f500.loc['Dow Chemical', 'ceo'] = 'Jim Fitterling'

# Create a boolean series, motor_bool, that compares whether the values in the industry column from the f500 dataframe are equal to "Motor Vehicles and Parts".
# Use the motor_bool boolean series to index the country column. Assign the result to motor_countries.
motor_bool = f500['industry'] == 'Motor Vehicles and Parts'
motor_countries = f500.loc[motor_bool, 'country'] # way to search
print(motor_countries)

# modifying
ampersand_bool = f500["sector"] == "Motor Vehicles & Parts"
f500.loc[ampersand_bool,"sector"] = "Motor Vehicles and Parts"
#IN ONE line
f500.loc[f500["sector"] == "Motor Vehicles & Parts","sector"] = "Motor Vehicles and Parts"

import numpy as np
# This uses Series.value_counts() and Series.head() to display the 5 most common values in the previous_rank column,
but adds an additional dropna=False parameter, which stops the Series.value_counts() method from excluding null values when
it makes its calculation, as shown in the Series.value_counts()
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
f500.loc[f500["previous_rank"] == 0,"previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()
print(prev_rank_after)
# NOTE: The index of the series that Series.value_counts() produces now shows us floats like 471.0 instead of integers. T
# he reason behind this is that pandas uses the NumPy integer dtype, which does not support NaN values.
# Pandas inherits this behavior, and in instances where you t
# ry and assign a NaN value to an integer column, pandas will silently convert that column to a float dtype.

# adding a column with mdified effects
f500['rank_change'] = f500['previous_rank'] - f500['rank']
rank_change_desc = f500['rank_change'].describe()
print(rank_change_desc)



# Create a series, industry_usa, containing counts of the two most common values in the industry column for companies headquartered in the USA.
# Create a series, sector_china, containing counts of the three most common values in the sector column for companies headquartered in the China.
industry_usa = f500['industry'][f500['country'] == 'USA'].value_counts().head(2)
print(industry_usa)

sector_china = f500['sector'][f500['country'] == 'China'].value_counts().head(3)
print(sector_china)
