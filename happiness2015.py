# we'll work with the World Happiness Report, an annual report created by the UN Sustainable Development Solutions Network
# with the intent of guiding policy. The report assigns each country a happiness score based on the answers to a poll question
# that asks respondents to rank their life on a scale of 0 - 10.
#
# It also includes estimates of factors that may contribute to each country's happiness, including economic production,
# social support, life expectancy, freedom, absence of corruption, and generosity, to provide context for the score.
# Although these factors aren't actually used in the calculation of the happiness score, they can help illustrate why a
# country received a certain score.
#
# Throughout this course, we'll work to answer the following questions:
#
# How can aggregating the data give us more insight into happiness scores?
# How did world happiness change from 2015 to 2017?
# Which factors contribute the most to the happiness score?


happiness2015['Happiness Score'].plot(kind='bar', title='Happiness Scores', ylim=(0,10))

# Plotting the data in its current form isn't helpful at all! There are so many data points that we can't
# see any of the values or labels.
#
# in the happiness2015 dataframe is assigned to a region, specified in the Region column.
# We can use the Series.unique() method to confirm the unique regions:

happiness2015['Region'].unique()

# Let's try plotting just one region next:

so_asia = happiness2015[happiness2015['Region'] == 'Southern Asia']
so_asia.plot(x='Country', y='Happiness Score', kind='barh', title='Southern Asia Happiness Scores', xlim=(0,10))


# loops for aggregation. Our process looked like this:
#
# Identify each unique group in the data set.
# For each group:
# Select only the rows corresponding to that group.
# Calculate the average for those rows.


#
# Create an empty dictionary named mean_happiness to store the results of this exercise.
# Use the Series.unique() method to create an array of unique values for the Region column.
# Use a for loop to iterate over the unique region values from the Region column.
# Assign the rows belonging to the current region to a variable named region_group.
# Use the Series.mean() method to calculate the mean happiness score for region_group.
# Assign the mean value to the mean_happiness dictionary, using the region name as the key and the mean happiness score as the value.

mean_happiness = {}

region = happiness2015['Region'].unique()

for reg in region:
    region_group = happiness2015[happiness2015['Region'] == reg]
    mean_happ = region_group['Happiness Score'].mean()
    mean_happiness[reg] = float(mean_happ)

print(mean_happiness)


mean_happiness = {}
regions = happiness2015['Region'].unique()

for r in regions:
    #1. Split the dataframe into groups.
    region_group = happiness2015[happiness2015['Region'] == r]
    #2. Apply a function to each group.
    region_mean = region_group['Happiness Score'].mean()


GROUPING BY

grouped = happiness2015.groupby('Region')
aus_nz = grouped.get_group("Australia and New Zealand")

# We can also use the GroupBy.groups attribute to get more information about the GroupBy object:

grouped = happiness2015.groupby('Region')
grouped.groups
# The result is a dictionary in which each key corresponds to a region name. See below for the first couple of keys:

grouped = happiness2015.groupby('Region')
north_america = happiness2015.iloc[[4,14]]
na_group = grouped.get_group('North America')
equal = north_america == na_group
print(equal)
#functions/methods that can be called on groups
# Methods	Description
# mean()	Calculates the mean of groups.
# sum()	    Calculates the sum of group values.
# size()	Calculates the size of the groups.
# count()	Calculates the count of values in groups.
# min()	    Calculates the minimum of group values.
# max()	    Calculates the maximum of group values.
#
# grouping another group from already existing group
# Select by Label	  Syntax
# Single column	      GroupBy["col1"]
# List of columns	  GroupBy[["col1", "col2"]]
grouped = happiness2015.groupby('Region')
happy_grouped = grouped['Happiness Score']
# print(happy_grouped)
happy_mean = happy_grouped.mean()
print(happy_mean)

# Luckily, however, the GroupBy.agg() method can perform both (mean and max) aggregations at once. We can use the following syntax:
# groupby.agg([fn1, fn2, fn3])
import numpy as np
grouped = happiness2015.groupby('Region')
happy_grouped = grouped['Happiness Score']

def dif(group):
    return (group.max() - group.mean())

happy_mean_max = happy_grouped.agg(['mean', 'max'])
mean_max_dif = happy_grouped.agg(dif)


PIVOT
#
# the DataFrame.pivot_table() method. This df.pivot_table() method can perform the same kinds of aggregations
# as the df.groupby method and make the code for complex aggregations easier to read.
happiness2015.pivot_table(values='Happiness Score', index='Region', aggfunc=np.mean, margins =True)
pv_happiness = happiness2015.pivot_table('Happiness Score', 'Region')
pv_happiness.plot(kind='barh', title='Mean Happiness Scores by Region', xlim=(0,10), legend=False)

pv_happiness = happiness2015.pivot_table(values='Happiness Score', index='Region', aggfunc=np.mean, margins=True)
pv_happiness.plot(kind='barh', xlim=(0,10), title='Mean Happiness Scores by Region', legend=False)
world_mean_happiness = happiness2015['Happiness Score'].mean()
#
# The pivot_table method also allows us to aggregate multiple columns and apply multiple functions at once.
# Below, we aggregate both the 'Happiness Score' and 'Family' columns in happiness2015 and group by the 'Region' column:

happiness2015.pivot_table(['Happiness Score', 'Family'], 'Region')

# To apply multiple functions, we can pass a list of the functions into the aggfunc parameter:
happiness2015.pivot_table('Happiness Score', 'Region', aggfunc=[np.mean, np.min , np.max], margins=True)



COMBINING DataSETS

Did world happiness increase, decrease, or stay about the same from 2015 to 2017?
#
# concat() function combines dataframes one of two ways:
# Stacked: Axis = 0 (This is the default option.)
# Side by Side: Axis = 1
head_2015 = happiness2015[['Country','Happiness Score', 'Year']].head(3)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)

concat_axis0 = pd.concat([head_2015, head_2016], axis = 0)
concat_axis1 = pd.concat([head_2015, head_2016], axis = 1)
concat_update_index = pd.concat([head_2015, head_2016], axis = 0, ignore_index = True)


# merge function only combines dataframes horizontally (axis=1) and can only combine two dataframes at a time.
# However, it can be valuable when we need to combine very large dataframes quickly and provides more flexibility in terms
# of how data can be combined
merged = pd.merge(left = three_2015, right = three_2016, on = 'Country')

# An inner join returns only the intersection of the keys, or the elements that appear in both dataframes with a common key.
# Inner: only includes elements that appear in both dataframes with a common key
# Outer: includes all data from both dataframes
# Left: includes all of the rows from the "left" dataframe along with any rows from the "right" dataframe with a common key;
# the result retains all columns from both of the original dataframes
# Right: includes all of the rows from the "right" dataframe along with any rows from the "left" dataframe with a common key; t
# he result retains all columns from both of the original dataframes
merged_suffixes = pd.merge(left=three_2015, right=three_2016, how='left', on='Country', suffixes = ('_2015', '_2016'))
merged_updated_suffixes = pd.merge(left=three_2016, right=three_2015, how = 'left', on='Country', suffixes = ('_2016', '_2015'))
# joining through index (matches the index values)
pd.merge(left=four_2015, right=three_2016, left_index=True, right_index=True, suffixes=('_2015','_2016'))





happiness2017.rename(columns={'Happiness.Score': 'Happiness Score'}, inplace=True)
combined = pd.concat([happiness2015, happiness2016, happiness2017], axis = 0)
pivot_table_combined = combined.pivot_table('Happiness Score', 'Year')
pivot_table_combined.plot(kind='barh', xlim=(0,10), title='Mean Happiness Scores by Year')

 # confirmed that the mean world happiness score stayed approximately the same from 2015 to 2017.


Which of the factors above contribute the most to the happiness score?
# renaming
mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health', 'Trust (Government Corruption)': 'Trust' }
happiness2015 = happiness2015.rename(mapping, axis = 1)
#
# Recall that each number represents the extent to which each factor contributes to the happiness score.
#
# However, not only is this definition a little hard to understand, but it can also be challenging to analyze all of
# these numbers across multiple columns. Instead, we can first convert these numbers to categories that indicate whether the
# factor has a high impact on the happiness score or a low impact using the following function:
def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'

economy_impact_map = happiness2015['Economy'].map(label)
economy_impact_apply = happiness2015['Economy'].apply(label)
equal = economy_impact_map.equals(economy_impact_apply)

# differe between apply and map methods
# use the Series.apply() method to apply a function with additional arguments element-wise - the Series.map() method will return an error.
def label(elemen,x):
    if element > x:
        return 'High'
    else:
        return 'Low'
economy_impact_apply = happiness2015['Economy'].apply(label, x=0.8)


# applying to mre than one rows_391_to_500def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
# economy_apply = happiness2015['Economy'].apply(label)
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']
factors_impact = happiness2015[factors].applymap(label)
#
# Method      Series or Dataframe Method	Applies Functions Element-wise?
# Map	        Series	                    Yes
# Apply	        Series	                        Yes
# Applymap   	Dataframe	                Yes

factors_impact.apply(pd.value_counts) #returns counts of high nad lows from the column

# Create a function that calculates the percentage of 'High' and 'Low' values in each column.
def v_counts(col):
    num = col.value_counts()
    den = col.size
    return num/den

v_counts_pct = factors_impact.apply(v_counts)

# One thing you probably didn't notice about the factor columns is that the sum of the six factors and the
# Dystopia Residual column equals the happiness score:


main_cols = ['Country', 'Region', 'Happiness Rank', 'Happiness Score']
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']
melt = pd.melt(happiness2015, id_vars = main_cols, value_vars = factors)
melt['Percentage'] = round(melt['value']/melt['Happiness Score'] * 100, 2)
#
# The melt function moved the values in the seven columns - Economy, Health, Family, Freedom, Generosity, Trust, and
# Dystopia Residual - to the same column, which meant we could transform them all at once.
melt = pd.melt(happiness2015, id_vars = ['Country', 'Region', 'Happiness Rank', 'Happiness Score'], value_vars= ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual'])
melt['Percentage'] = round(melt['value']/melt['Happiness Score'] * 100, 2)

pv_melt = melt.pivot_table('value', 'variable')
pv_melt.plot(kind = 'pie', y= 'value', legend = False)





WORKING WITH STRINGS IN PANDAS


world_dev = pd.read_csv("World_dev.csv")
col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}

merged = pd.merge(left=happiness2015, right=world_dev, how='left', left_on='Country', right_on='ShortName')

merged = merged.rename(col_renaming, axis = 1)

def extract_last_word(element):
    word = str(element).split()
    return word[-1]

merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last_word)

merged['Currency Apply'].head(5)


#
# Method	                 Description
# Series.str.split()	   Splits each element in the Series.
# Series.str.strip()	   Strips whitespace from each string in the Series.
# Series.str.lower()	   Converts strings in the Series to lowercase.
# Series.str.upper()	   Converts strings in the Series to uppercase.
# Series.str.get()	       Retrieves the ith element of each element in the Series.
# Series.str.replace()	   Replaces a regex or string in the Series with another string.
# Series.str.cat()	       Concatenates strings in a Series.
# Series.str.extract()	   Extracts substrings from the Series matching a regex pattern.

merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(-1)
merged['Currency Vectorized'].head(5)

# using vectorized string methods results in:
#
# Better performance
# Code that is easier to read and write
# Automatically excludes missing values

lengths = merged['CurrencyUnit'].str.len()
value_counts = lengths.value_counts(dropna=False)

pattern = r"[Nn]ational accounts"

national_accounts = merged['SpecialNotes'].str.contains(pattern, na=False)
merged_national_accounts = merged[national_accounts]
merged_national_accounts.head(5)
#
# With regular expressions, we use the following syntax to indicate a character could be a range of numbers:
# pattern = r"[0-9]"
# And we use the following syntax to indicate a character could be a range of letters:
# #lowercase letters
# pattern1 = r"[a-z]"
# #uppercase letters
# pattern2 = r"[A-Z]"
# We could also make these ranges more restrictive. For example, if we wanted to find a three character substring in a column that starts with a number between 1 and 6 and ends with two letters of any kind, we could use the following syntax:
# pattern = r"[1-6][a-z][a-z]"
# If we have a pattern that repeats, we can also use curly brackets { and } to indicate the number of times it repeats:
# pattern = r"[1-6][a-z][a-z]" = r"[1-6][a-z]{2}"

pattern =r"([1-2][0-9][0-9][0-9])"
years = merged['SpecialNotes'].str.extract(pattern)

pattern = r"([1-2][0-9]{3})"
years = merged['SpecialNotes'].str.extract(pattern, expand=True)

pattern = r"(?P<Years>[1-2][0-9]{3})"
years = merged['IESurvey'].str.extractall(pattern)
value_counts = years['Years'].value_counts()
print(value_counts)

pattern = r"(?P<First_Year>[1-2][0-9]{3})/?(?P<Second_Year>[0-9]{2})?"
years = merged['IESurvey'].str.extractall(pattern)
first_two_year = years['First_Year'].str[0:2]
years['Second_Year'] = first_two_year + years['Second_Year']

merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(' income','').str.replace(':','').str.upper()
pv_incomes = merged.pivot_table('Happiness Score', 'IncomeGroup')
pv_incomes.plot(kind='bar', rot=30, ylim=(0,10))
plt.show()




# Missing or duplicate data may exist in a data set for a number of different reasons. Sometimes, missing or duplicate data
# is introduced as we perform cleaning and transformation tasks such as:
# Combining data
# Reindexing data
# Reshaping data
# Other times, it exists in the original data set for reasons such as:
# User input error
# Data storage or conversion issues
# In the case of missing values, they may also exist in the original data set to purposely indicate that data is unavailable.
# In the Pandas Fundamentals course, we learned that there are various ways to handle missing data:
# Remove any rows that have missing values.
# Remove any columns that have missing values.
# Fill the missing values with some other value.
# Leave the missing values as is.
missing = happiness2015['Happiness Score'].isnull()
happiness2015[missing]
happiness2015.isnull().sum()
# we'll use the following workflow to clean our missing values, starting with checking for errors:
# Check for errors in data cleaning/transformation.
# Use data from additional sources to fill missing values.
# Drop row/column.
# Fill missing values with reasonable estimates computed from the available data.
happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper()
happiness2015.columns = happiness2015.columns.str.upper().str.replace(r"[()]", "")
happiness2016.columns = happiness2016.columns.str.upper().str.replace(r"[()]", "")
combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)
missing = combined.isnull().sum()
# heatmap for missing values in the combined dataset
import seaborn as sns
combined_updated = combined.set_index('YEAR')
sns.heatmap(combined_updated.isnull(), cbar = False)
# We can make the following observations:
# No values are missing in the COUNTRY column.
# There are some rows in the 2015, 2016, and 2017 data with missing values in all columns EXCEPT the COUNTRY column.
# Some columns only have data populated for one year.
# It looks like the REGION data is missing for the year 2017.
regions_2017 = combined[combined["YEAR"]==2017]['REGION']
missing = regions_2017.isnull().sum()
# Since the regions are fixed values - the region a country was assigned to in 2015 or 2016 won't change - we should be
# able to assign the 2015 or 2016 region to the 2017 row.
# In order to do so, we'll use the following strategy:
# Create a dataframe containing all of the countries and corresponding regions from the happiness2015, happiness2016, and
# happiness2017 dataframes.
# Use the pd.merge() function to assign the REGION in the dataframe above to the corresponding country in combined.
# The result will have two region columns - the original column with missing values will be named REGION_x.
# The updated column without missing values will be named REGION_y. We'll drop REGION_x to eliminate confusion.
combined = pd.merge(left=combined, right=regions, on='COUNTRY', how='left')
combined = combined.drop('REGION_x', axis=1)
missing = combined.isnull().sum()
# checking for duplicate Values
combined['COUNTRY'] = combined['COUNTRY'].str.upper()
dups = combined.duplicated(['COUNTRY', 'YEAR'])
print(combined[dups])
# droping the duplicates, if you want the last duplicate data then use the parameter keep=last
combined['COUNTRY'] = combined['COUNTRY'].str.upper()
combined = combined.drop_duplicates(['COUNTRY', 'YEAR'])
# When deciding if you should drop a row or column, carefully consider whether you'll lose information that could alter your analysis.
# Instead of just saying, "If x percentage of the data is missing, we'll drop it.", it's better to also ask the following questions:
# Is the missing data needed to accomplish our end goal?
# How will removing or replacing the missing values affect our analysis?
# To answer the first question, let's establish our end goal:
# End Goal: We want to analyze happiness scores and the factors that contribute to happiness scores by year and region.
# Since missing values make up more than half of the following columns and we don't need them to accomplish our end goal,
# we'll drop them:
# STANDARD ERROR
# LOWER CONFIDENCE INTERVAL
# UPPER CONFIDENCE INTERVAL
# WHISKER HIGH
# WHISKER LOW
columns_to_drop = ['LOWER CONFIDENCE INTERVAL', 'STANDARD ERROR', 'UPPER CONFIDENCE INTERVAL', 'WHISKER HIGH', 'WHISKER LOW']
combined = combined.drop(columns_to_drop, axis=1)
missing = combined.isnull().sum()
# in larger datasets its hard to see which columns to drop, so thresh method can be used
combined.notnull().sum().sort_values()
combined = combined.dropna(thresh=159, axis=1) #159 number is chosen from the above statement, which helps us in knowing which column has least registry
missing = combined.isnull().sum()
# Let's return to the following questions:
# Is the missing data needed to accomplish our end goal?
# Yes, we need the data to accomplish our goal of analyzing happiness scores and contributing factors by region and year.
# How will removing or replacing the missing values affect our analysis?
# Let's break the second question down into a couple more specific questions:
# What percentage of the data is missing?
# Will dropping missing values cause us to lose valuable information in other columns?
# Can we identify any patterns in the missing data?
# Question: What percentage of the data is missing?
# As we saw when looking at the results of combined.isnull().sum() above, if missing values exist in a column of our dataframe,
# they account for about 4 percent of the total values (19 missing out of 489 values per column).
# Generally speaking, the lower the percentage of missing values, the less likely dropping them will significantly impact the analysis.
# Question: Will dropping missing values cause us to lose valuable information in other columns?
# To answer this question, let's visualize the missing data once more. Note below that before we create the heatmap,
# we first set the index of combined to the REGION column and sort the values:
# sorted = combined.set_index('REGION').sort_values(['REGION', 'HAPPINESS SCORE'])
# sns.heatmap(sorted.isnull(), cbar=False)
# heatmap_regions
# As a reminder, in the heatmap above, the missing values are represented with light gray and all other values with black.
# From this visualization, we can confirm that if the data is missing, it's missing in almost every column.
# We'll conclude that dropping the missing values(row) won't cause us to lose valuable information in other columns.
# Question: Can we identify any patterns in the missing data?
# From the visualization above, we can also identify that only three regions contain missing values:
# Sub-Saharan Africa
# Middle East and Northern Africa
# Latin America and Carribbean
# The Sub-Saharan Africa region contains the most missing values, accounting for about 9 percent of that regions's values.
# Since we'd like to analyze the data according to region, we should also think about how these values impact the analysis
# for this region specifically.
# However, before we make a decision, let's consider handling the missing values by replacing them with estimated values,
# also called imputation.
# Check for errors in data cleaning/transformation.
# Use data from additional sources to fill missing values.
# Drop row/column.
# Fill missing values with reasonable estimates computed from the available data.
# There are many options for choosing the replacement value, including:
# A constant value
# The mean of the column
# The median of the column
# The mode of the column
# For non-numeric columns, common replacement values include the most frequent value or a string like "Unknown" that is
# used to treat missing values as a separate category.
happiness_mean = combined['HAPPINESS SCORE'].mean()
combined['HAPPINESS SCORE UPDATED'] = combined['HAPPINESS SCORE'].fillna(happiness_mean)
new_happiness_mean = combined['HAPPINESS SCORE'].mean()
# In the last exercise, we confirmed that replacing missing values with the Series mean doesn't change the mean of the Series.
# If we were to plot the distributions before and after replacing the missing values with the mean, we'd see that the shape of
# the distribution changes as more values cluster around the mean. Note that the mean is represented with the red and
# green lines in the plots below:
# Happiness_means_original
# Happiness_means
# As we decide to use this approach, we should ask the following questions - are the missing happiness scores likely to
# be close to the mean? Or is it more likely that the scores are very high or very low? If the missing values lie at
# extremes, the mean won't be a good estimate for them.
# Missing_values
# Recall that when we visualized the missing data, we determined that the Sub-Saharan Africa region
# contained the most missing values. Since we'd like to analyze the data according to region, let's look more closely at t
# he means for each region:
combined.pivot_table(index='REGION', values='HAPPINESS SCORE', margins=True)
# 	                           HAPPINESS SCORE
# REGION
# Australia and New Zealand	    7.302500
# Central and Eastern Europe	5.371184
# Eastern Asia	                5.632333
# Latin America and Caribbean	6.069074
# Middle East and Northern Africa	5.387879
# North America	                7.227167
# Southeastern Asia	            5.364077
# Southern Asia	                4.590857
# Sub-Saharan Africa	        4.150957
# Western Europe	            6.693000
# # All	                        5.370728
# As a reminder, the All row in the table above represents the mean happiness score for the whole world - the value that we
# used to replace our missing values. We can see that the world mean happiness score, 5.370728, is over 1 point higher
# than the mean happiness score for the Sub-Saharan Africa region, 4.150957.
# Also, if we think about the reasons why a country may not have participated in the happiness survey - war,
# natural disaster, etc - many of them would likely result in a lower happiness score than even the region's mean. We'll conclude
# that the mean for the whole world wouldn't be a good estimate for them.
# As a result, we'll decide that of these two options, it's better to drop the rows with missing values. Let's do that next
combined = combined.dropna()
missing = combined.isnull().sum()
