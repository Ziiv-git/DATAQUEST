import seaborn as sns
sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba, order = ['Rookie', 'Little experience','Experienced', 'Very experienced', 'Veteran'], hue_order = ['C','F','F/C','G','G/F']) #grouped bar plot


wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else 'below average')


import matplotlib.pyplot as plt
wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype='step', label='Old', legend=True) #ploting histogram when age > 27 then only ploting the histogram for the minutes played column
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype='step', label='Young', legend=True)
plt.axvline(497, label='Average')
plt.legend()
plt.show()


# smoothing out the above histogram using kde plot
# Each of the smoothed histograms above is called a kernel density estimate plot or, shorter, kernel density plot. Unlike histograms, kernel density plots display
# densities on the y-axis instead of frequencies.
wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend=True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend=True)
plt.axvline(497, label='Average')
plt.legend()
plt.show()



sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter=True)
plt.show()


sns.boxplot(x='Pos', y='Weight', data=wnba)
plt.show()
A value is an outlier if:
#
# It's larger than the upper quartile by 1.5 times the difference between the upper quartile and the lower quartile (the difference is also called the interquartile range).
# It's lower than the lower quartile by 1.5 times the difference between the upper quartile and the lower quartile (the difference is also called the interquartile range).
