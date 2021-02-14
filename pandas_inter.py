fifth_row = f500.iloc[4]
# print(fifth_row)
company_value = f500.iloc[0,0]
print(company_value)

With loc[], the ending slice is included.
With iloc[], the ending slice is not included.

loc: label based selection
iloc: integer position based selection

Select by integer position	       Explicit Syntax	      Shorthand Convention
Single column from dataframe	   df.iloc[:,3]
List of columns from dataframe	   df.iloc[:,[3,5,6]]
Slice of columns from dataframe	   df.iloc[:,3:7]
Single row from dataframe	       df.iloc[20]
List of rows from dataframe	       df.iloc[[0,3,8]]
Slice of rows from dataframe	   df.iloc[3:5]	            df[3:5]
Single items from series	       s.iloc[8]	            s[8]
List of item from series	       s.iloc[[2,8,1]]	        s[[2,8,1]]
Slice of items from series	       s.iloc[5:10]

first_three_rows = f500.iloc[0:3]
first_seventh_row_slice = f500.iloc[[0,6],0:5]


null_previous_rank = f500[f500["previous_rank"].isnull()][["company","rank", "previous_rank"]]
first_null_prev_rank = null_previous_rank.iloc[0]

food["alt_name"] = alt_name

# NOTE: using of logical operators
f500_sel = f500['company', 'revenues', 'country'].head()
over_265_million = f500_sel['revenues'] > 265000
china = f500_sel['country'] == 'China'
combined = over_265_million & china
final_cols = ['company', 'revenues']
result = f500_sel.loc[combined, final_cols]


Select all companies with revenues over 100 billion and negative profits from the f500 dataframe. The result should include all columns.
Create a boolean array that selects the companies with revenues greater than 100 billion. Assign the result to large_revenue.
Create a boolean array that selects the companies with profits less than 0. Assign the result to negative_profits.
Combine large_revenue and negative_profits. Assign the result to combined.
Use combined to filter f500. Assign the result to big_rev_neg_profit.


large_revenue = f500['revenues'] > 100000
negative_profits = f500['profits'] < 0
combined = large_revenue & negative_profits
big_rev_neg_profit = f500[combined]

or

big_rev_neg_profit = f500[(f500["revenues"] > 100000) & (f500["profits"] < 0)]


filter_brazil_venezuela = (f500["country"] == "Brazil") | (f500["country"] == "Venezuela")
brazil_venezuela = f500[filter_brazil_venezuela]

filter_tech_outside_usa = (f500["sector"] == "Technology") & ~(f500["country"] == "USA")
tech_outside_usa = f500[filter_tech_outside_usa].head()


#  use of Sorting
selected_rows = f500[f500["country"] == "China"]
sorted_rows = selected_rows.sort_values("employees")
print(sorted_rows[["company", "country", "employees"]].head())


selected_rows = f500[f500["country"] == "Japan"]
sorted_rows = selected_rows.sort_values("employees", ascending = False)
result = sorted_rows.iloc[0]
top_japanese_employer = sorted_rows.iloc[0]['company']
print(top_japanese_employer)


To identify the unique countries, we can use the Series.unique() method. This method returns an array of unique values from any series.
Then, we can loop over that array and perform our operation. Here's what that looks like:
# Create an empty dictionary to store the results
avg_rev_by_country = {}

# Create an array of unique countries
countries = f500["country"].unique()

# Use a for loop to iterate over the countries
for c in countries:
    # Use boolean comparison to select only rows that
    # correspond to a specific country
    selected_rows = f500[f500["country"] == c]
    # Calculate the mean average revenue for just those rows
    mean = selected_rows["revenues"].mean()
    # Assign the mean value to the dictionary, using the
    # country name as the key
    avg_rev_by_country[c] = mean

# Create an empty dictionary to store the results
top_employer_by_country = {}

# Create an array of unique countries
countries = f500["country"].unique()

# Use a for loop to iterate over the countries
for c in countries:
    # Use boolean comparison to select only rows that
    # correspond to a specific country
    selected_rows = f500[f500["country"] == c]
#  Use DataFrame.sort_values() to sort those rows by the employees column in descending order.
    sorted_rows = selected_rows.sort_values("employees", ascending = False)
    top_employer = sorted_rows.iloc[0]
    employer_name = top_employer['company']
    top_employer_by_country[c] = employer_name

print(top_employer_by_country)


f500['roa'] = f500['profits'] / f500['assets']
# print(f500['roa'])
top_roa_by_sector = {}
# Create an array of unique sectors
sectors = f500["sector"].unique()

for c in sectors:
    # Use boolean comparison to select only rows that
    # correspond to a specific sector
    selected_rows = f500["sector"] == c
    sector_companies = f500.loc[selected_rows]
    top_company = sector_companies.sort_values('roa', ascending = False).iloc[0]
    company_name = top_company['company']
    top_roa_by_sector[c] = company_name

print(top_roa_by_sector)


brand_mean_prices = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_price = brand_only["price_$"].mean()
    brand_mean_prices[brand] = int(mean_price)

brand_mean_prices
