import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75

fig, ax = plt.subplots()
ax.bar(bar_positions,bar_heights, 0.5)
plt.show()


num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
fig, ax = plt.subplots()

ax.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation=90)

ax.set_xlabel('Rating Source')
ax.set_ylabel('Average Rating')
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
plt.show()

We can create a horizontal bar plot in matplotlib in a similar fashion.
Instead of using Axes.bar(), we use Axes.barh(). This method has 2 required parameters, bottom and width.
We use the bottom parameter to specify the y coordinate for the bottom sides for the bars and the width parameter
to specify the lengths of the bars:

bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
fig, ax = plt.subplots()

ax.barh(bar_positions, bar_widths, 0.5)
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)

ax.set_ylabel('Rating Source')
ax.set_xlabel('Average Rating')
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
plt.show()



fig, ax = plt.subplots()

ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')

plt.show()


When using scatter plots to understand how 2 variables are correlated, it's usually not important which one is on the x-axis
and which one is on the y-axis. This is because the relationship is still captured either way, even if the plots look a
little different.
If you want to instead understand how an independent variable affects a dependent variables, you want to put the independent
one on the x-axis and the dependent one on the y-axis. Doing so helps emphasize the potential cause and effect relation.


fandango_distribution = norm_reviews['Fandango_Ratingvalue'].value_counts()
imdb_distribution = norm_reviews['IMDB_norm'].value_counts()
print(fandango_distribution)

print(imdb_distribution)







We can generate a histogram using Axes.hist(). This method has only 1 required parameter, an iterable object containing the values we want a histogram for. By default, matplotlib will:

calculate the minimum and maximum value from the sequence of values we passed in
create 10 bins of equal length that span the range from the minimum to the maximum value
group unique values into the bins
sum up the associated unique values
generate a bar for the frequency sum for each bin

The default behavior of Axes.hist() is problematic for the use case of comparing distributions for multiple columns using
the same binning strategy. This is because the binning strategy for each column would depend on the minimum and maximum values,
instead of a shared binning strategy.
We can use the range parameter to specify the range we want matplotlib to use as a tuple:

fig, ax=plt.subplots()
ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(0, 5))
plt.show()



Histograms help us visualize continuous values using bins while bar plots help us visualize discrete values.




# fig = plt.figure(figsize=(5,20))
# ax1 = fig.add_subplot(4,1,1)
# ax2 = fig.add_subplot(4,1,2)
# ax3 = fig.add_subplot(4,1,3)
# ax4 = fig.add_subplot(4,1,4)
fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews['Fandango_Ratingvalue'], bins=20, range=(0, 5))
ax1.set_title('Distribution of Fandango Ratings')
ax1.set_ylim(0, 50)

ax2.hist(norm_reviews['RT_user_norm'], 20, range=(0, 5))
ax2.set_title('Distribution of Rotten Tomatoes Ratings')
ax2.set_ylim(0, 50)

ax3.hist(norm_reviews['Metacritic_user_nom'], 20, range=(0, 5))
ax3.set_title('Distribution of Metacritic Ratings')
ax3.set_ylim(0, 50)

ax4.hist(norm_reviews['IMDB_norm'], 20, range=(0, 5))
ax4.set_title('Distribution of IMDB Ratings')
ax4.set_ylim(0, 50)

plt.show()




While histograms allow us to visually estimate the percentage of ratings that fall into a range of bins, they don't allow us to
easily understand how the top 25% or the bottom 25% of the ratings differ across the sites.
The bottom 25% of values and top 25% of values both represent quartiles.
The four quartiles divide the range of values into four regions where each region contains 1/4th of the total values.

While these regions may sound similar to bins, they differ in how values are grouped into each region.
Each bin covers an equal proportion of the values in the range. On the other hand, each quartile covers an equal number of
values (1/4th of the total values). To visualize quartiles, we need to use a box plot, also referred to as a box-and-whisker plot.


fig, ax = plt.subplots()

ax.boxplot(norm_reviews['RT_user_norm'])
ax.set_ylim(0,5)
ax.set_xticklabels(['Rotten Tomatoes'])

plt.show()



num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']

fig, ax = plt.subplots()

ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim(0,5)
plt.show()
