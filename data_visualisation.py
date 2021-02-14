When we read the dataset into a DataFrame, pandas will set the data type of the DATE column as a text column.
Because of how pandas reads in strings internally, this column is given a data type of object.
We need to convert this column to the datetime type using the pandas.to_datetime() function, which returns a Series object
with the datetime data type that we can assign back to the DataFrame:


import pandas as pd
unrate = pd.read_csv('unrate.csv')
# Use the pandas.to_datetime function to convert the DATE column into a series of datetime values.
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
unrate[:12]


Seasonality is when a pattern is observed on a regular, predictable basis for a specific reason.
A simple example of seasonality would be a large increase textbook purchases every August every year.
Many schools start their terms in August and this spike in textbook sales is directly linked.


To create the line chart, we'll use the matplotlib library, which allows us to:

quickly create common plots using high-level functions
extensively tweak plots
create new kinds of plots from the ground up


create a plot using data
customize the appearance of the plot
display the plot
edit and repeat until satisfied

import pandas as pd
import matplotlib.pyplot as plt
unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation = 90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()


import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
first_twelve = unrate[0:12]
next_twelve = unrate[12:24]
ax1.plot(first_twelve['DATE'], first_twelve['VALUE'])
ax2.plot(next_twelve['DATE'], next_twelve['VALUE'])
fig.show()



fig = plt.figure(figsize=(12, 5))
# The unit for both width and height values is inches. The dpi parameter, or dots per inch, and the figsize parameter determine how much space on your display a plot takes up. By increasing the width and the height of the plotting area, we can address both issues.
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()


fig = plt.figure(figsize = (12,12))

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])

plt.show()


unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize = (6,3))

plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue')

plt.show()



fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
years = [1948, 1949, 1950, 1951, 1952]
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label = years[i])

plt.legend(loc='upper left')
plt.title('Monthly Unemployment Trends, 1948-1952')
plt.xlabel('Month, Integer')
plt.ylabel('Unemployment Rate, Percent')
plt.show()



import pandas as pd
reviews = pd.read_csv('fandango_scores.csv')

cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

norm_reviews = reviews[cols]

print(norm_reviews[:1])
