import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding = 'Latin-1')
laptops.info()

# print(laptops.columns)
laptops_test = laptops.copy()
# Not only can we use the attribute to view the column labels, we can also assign new labels to the attribute:
laptops_test.columns = ['A', 'B', 'C', 'D', 'E',
                        'F', 'G', 'H', 'I', 'J',
                        'K', 'L', 'M']
# print(laptops_test.columns)

new_columns = []

for column in laptops:
    new_column = column.strip(' ')
    new_columns.append(new_column)

# print(new_columns)

laptops.columns = new_columns
# print(laptops.columns)

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')
# However, the column labels still have a variety of upper and lowercase letters, as well as parentheses, which will make them harder to work with and read. Let's finish cleaning our column labels by:

# Replacing spaces with underscores.
# Removing special characters.
# Making all labels lowercase.
# Shortening any long column names.
def clean_col(col):
    col = col.strip()
    col = col.replace('Operating System', 'OS')
    col = col.replace(' ','_')
    col = col.replace("(","")
    col = col.replace(")","")
    col = col.lower()
    return col

new_columns = []
for c in laptops.columns:
    clean_c = clean_col(c)
    new_columns.append(clean_c)

laptops.columns = new_columns
# print(laptops.columns)

# We observed earlier that all 13 columns have the object dtype, meaning they're stored as strings. Let's look at the first few rows of some of our columns:
# print(laptops.iloc[:5,2:5])
# 1.explore the data in column
#  2. identify patterns and special cases
# 3. remove non-digit characters
# 4.convert the column to numeric dtpe
# 5. rename column if required

print(laptops['screen_size'].dtype)
print(laptops['screen_size'].unique())
unique_ram = laptops['ram'].unique()
# print(unique_ram)

laptops['screen_size'] = laptops['screen_size'].str.replace('"','')
# print(laptops['screen_size'].unique())
laptops['ram'] = laptops['ram'].str.replace('GB','')
unique_ram = laptops['ram'].unique()
# print(unique_ram)

# converting to float and int to laptops["ram"] = laptops["ram"].str.replace('GB','')
laptops["screen_size"] = laptops["screen_size"].astype(float)
# print(laptops["screen_size"].dtype)
# print(laptops["screen_size"].unique())
laptops['ram'] = laptops['ram'].astype(int)
# print(laptops["ram"].dtype)
# print(laptops["ram"].unique())

laptops["ram"] = laptops["ram"].str.replace('GB','').astype(int)
# To stop us from losing information that helps us understand the data, we can use the DataFrame.rename() method to rename the column from screen_size to screen_size_inches
laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)
# print(laptops.dtypes)
laptops.rename({'ram' : 'ram_gb'}, axis = 1, inplace = True)
# print(laptops.columns)
ram_gb_desc = laptops['ram_gb'].describe()
print(ram_gb_desc)

# using split method to extract just the manufacturer name
laptops["gpu_manufacturer"] = (laptops["gpu"]
                                       .str.split()
                                       .str[0]
                              )
# print(laptops['gpu_manufacturer'].head())
# print(laptops['cpu'].head())
laptops['cpu_manufacturer'] = (laptops['cpu'].str.split().str[0])
# print(laptops['cpu_manufacturer'].head())
cpu_manufacturer_counts = laptops['cpu_manufacturer'].value_counts()
# print(cpu_manufacturer_counts)


We can see that there are two variations of the Apple operating system — macOS — in our dataset: Mac OS and macOS.
One way we can fix this is with the Series.map() method. The Series.map() method is ideal when we want to change multiple values
in a column, but we'll use it now as an opportunity to learn how the method works.

0       pair
1     oranje
2    bananna
3     oranje
4     oranje
5     oranje
dtype: object

corrections = {"pair": "pear","oranje": "orange","bananna": "banana"}
s = s.map(corrections)
print(s)

 One important thing to remember with Series.map() is that
 if a value from your series doesn't exist as a key in your dictionary, it will convert that value to NaN

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops['os'] = laptops['os'].map(mapping_dict)
print(laptops['os'])

 we can use the DataFrame.isnull() method to identify missing values, which returns a boolean dataframe.
 We can then use the DataFrame.sum() method to give us a count of the True values for each column:

 print(laptops.isnull().sum())

There are a few options for handling missing values:

Remove any rows that have missing values.
Remove any columns that have missing values.
Fill the missing values with some other value.
Leave the missing values as is.
The first two options are often used to prepare data for machine learning algorithms, which are unable to be used with data
that includes null values.
We can use the DataFrame.dropna() method to remove or drop rows and columns with null values.

The default value for the axis parameter is 0, so df.dropna() returns an identical result to df.dropna(axis=0):

laptops_no_null_rows = laptops.dropna(axis = 0)
laptops_no_null_cols = laptops.dropna(axis = 1)

print(laptops["os_version"].value_counts(dropna=False))

Because we set the dropna parameter to False, the result includes null values.
We can see that the majority of values in the column are 10 and missing values are the next most common.

os_with_null_v = laptops.loc[laptops["os_version"].isnull(),"os"]
# print(os_with_null_v.value_counts())
# use assignment with a boolean comparison to perform this replacement, like below:
value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
# print(value_counts_before)
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"
laptops.loc[laptops["os"] == "No OS", "os_version"] = "Version Unknown"
value_counts_after = laptops.loc[laptops['os_version'].isnull(), 'os'].value_counts()
print(value_counts_after)


laptops["weight"] = laptops["weight"].str.replace("kgs","").str.replace("kg","").astype(float)
laptops.rename({'weight' : 'weight_kg'}, axis = 1, inplace = True)
laptops.to_csv('laptops_cleaned.csv', index = False)












Our dataset is ready for some analysis, but there are still some data cleaning tasks left! Here are your next steps:

Convert the price_euros column to a numeric dtype.
Extract the screen resolution from the screen column.
Extract the processor speed from the cpu column.
Here are some questions you might like to answer in your own time by analyzing the cleaned data:

Are laptops made by Apple more expensive than those made by other manufacturers?
What is the best value laptop with a screen size of 15" or more?
Which laptop has the most storage space?
The final mission in our course is a guided project, where we'll put everything together to clean and analyze a dataset using pandas!
