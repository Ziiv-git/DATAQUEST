# Although NumPy provides fundamental structures and tools that make working with data easier, there are several things that limit its usefulness:

# The lack of support for column names forces us to frame questions as multi-dimensional array operations.
# Support for only one data type per ndarray makes it more difficult to work with data that contains both numeric and string data.
# There are lots of low level methods, but there are many common analysis patterns that don't have pre-built methods.
# The pandas library provides solutions to all of these pain points and more. Pandas is not so much a replacement for NumPy as an extension of NumPy. The underlying code for pandas uses the NumPy library extensively, which means the concepts you've been learning will come in handy as you begin to learn more about pandas.
#
# The primary data structure in pandas is called a dataframe. Dataframes are the pandas equivalent of a Numpy 2D ndarray, with a few key differences:
#
# Axis values can have string labels, not just numeric ones.
# Dataframes can contain columns with multiple data types: including integer, float, and string.

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None
f500_type = type(f500)
print(f500_type)
f500_shape = f500.shape
print(f500_shape)

f500_head = f500.head(6)
# print(f500_head)
f500_tail = f500.tail(8)
# print(f500_tail)

f500.info()

industries = f500['industry']
# print(industries)
industries_type = type(industries)
print(industries_type)

# On the last screen, we observed that when you select just one column of a dataframe, you get a new pandas type: a series object. Series is the pandas type for one-dimensional objects. Anytime you see a 1D pandas object, it will be a series. Anytime you see a 2D pandas object, it will be a dataframe.

# In fact, you can think of a dataframe as a collection of series objects, which is similar to how pandas stores the data behind the scenes.


Select by Label	      Explicit Syntax	            Common Shorthand
Single column	      df.loc[:,"col1"]	            df["col1"]
List of columns	      df.loc[:,["col1", "col7"]]	df[["col1", "col7"]]
Slice of columns	  df.loc[:,"col1":"col4"]

countries = f500['country']
# print(countries)
# In order, select the revenues and years_on_global_500_list columns. Assign the result to the variable name revenues_years
revenues_years= f500[['revenues','years_on_global_500_list']]
# print(revenues_years)
ceo_to_sector = f500.loc[:,'ceo':'sector']
print(ceo_to_sector)

# Create a new variable toyota, with:Just the row with index Toyota Motor.All columns.
toyota = f500.loc['Toyota Motor']
# print(toyota)
# Create a new variable, drink_companies, with:Rows with indicies Anheuser-Busch InBev, Coca-Cola, and Heineken Holding, in that order.All columns.
drink_companies = f500.loc[['Anheuser-Busch InBev','Coca-Cola','Heineken Holding']]
# print(drink_companies)
# Create a new variable, middle_companies with:All rows with indicies from Tata Motorsto Nationwide, inclusive.All columns from rank to country, inclusive.
middle_companies = f500.loc['Tata Motors':'Nationwide','rank':'country']
print(middle_companies)


# Because series and dataframes are two distinct objects, they have their own unique methods. Let's look at an example of a series method next - the Series.value_counts() method. This method displays each unique non-null value in a column and their counts in order.

countries = f500_sel['country']
country_counts = countries.value_counts()
print(countries)

# for selecting thing/s in Series
Select by Label	                Explicit Syntax	              Shorthand Convention
Single item from series	        s.loc["item8"]	              s["item8"]
List of items from series	    s.loc[["item1","item7"]]      s[["item1","item7"]]
Slice of items from series	    s.loc["item2":"item4"]	      s["item2":"item4"]


countries = f500['country']
countries_counts = countries.value_counts()
india = countries_counts['India']
# print(india)
north_america = countries_counts[['USA', 'Canada', 'Mexico']]
# print(north_america)



Select by Label	                        Explicit Syntax	                    Shorthand Convention
Single column from dataframe	        df.loc[:,"col1"]	                df["col1"]
List of columns from dataframe	        df.loc[:,["col1","col7"]]	        df[["col1","col7"]]
Slice of columns from dataframe	        df.loc[:,"col1":"col4"]
Single row from dataframe	            df.loc["row4"]
List of rows from dataframe	            df.loc[["row1", "row8"]]
Slice of rows from dataframe	        df.loc["row3":"row5"]	            df["row3":"row5"]
Single item from series	                s.loc["item8"]	                    s["item8"]
List of items from series	            s.loc[["item1","item7"]]	        s[["item1","item7"]]
Slice of items from series	            s.loc["item2":"item4"]	            s["item2":"item4"]


# Create a new variable big_movers, with:Rows with indices Aviva, HP, JD.com, and BHP Billiton, in that order.The rank and previous_rank columns, in that order.
big_movers = f500.loc[['Aviva', 'HP', 'JD.com', 'BHP Billiton'], ['rank','previous_rank']]
# print(big_movers)
# Create a new variable, bottom_companies with:All rows with indices from National Gridto AutoNation, inclusive.The rank, sector, and country columns.
bottom_companies = f500.loc['National Grid':'AutoNation', ['rank', 'sector', 'country']]
# print(bottom_companies)
