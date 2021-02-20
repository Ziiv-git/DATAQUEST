One way is to list all the data sources you can find, and then randomly pick only a few of them to collect data from. Then you can sample individually each of
the sources you've randomly picked. This sampling method is called cluster sampling, and each of the individual data sources is called a cluster.

clusters = pd.Series(wnba['Team'].unique()).sample(4,random_state=0)#Pick four team clusters randomly
sample = pd.DataFrame()
#collects the data from the cluster and putting it into a dataframe
for cluster in clusters:
    data_collected = wnba[wnba['Team'] == cluster]
    sample = sample.append(data_collected)

sampling_error_height = wnba['Height'].mean() - sample['Height'].mean()
sampling_error_age = wnba['Age'].mean() - sample['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - sample['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - sample['PTS'].mean()


When we describe a sample or a population (by measuring averages, proportions, and other metrics; by visualizing properties of the data through graphs; etc.),
we do descriptive statistics.
When we try to use a sample to draw conclusions about a population, we do inferential statistics (we infer information from the sample about the population).

For instance, the Height variable in our dataset describes how tall each player is. The Age variable describes how much time has passed since each player was born.
The MIN variable describes how many minutes each player played in the 2016-2017 WNBA season.
Generally, a variable that describes how much there is of something describes a quantity, and, for this reason, it's called a quantitative variable.

Usually, quantitative variables describe a quantity using real numbers, but there are also cases when words are used instead. Height, for example, can be described using
real numbers, like in our dataset, but it can also be described using labels like "tall" or "short".

A few variables in our dataset clearly don't describe quantities. The Name variable, for instance, describes the name of each player. The Team variable describes what
team each player belongs to. The College variable describes what college each player goes or went to.The Name, Team, and College variables describe for each individual
a quality, that is, a property that is not quantitative. Variables that describe qualities are called qualitative variables or categorical variables.
Generally, qualitative variables describe what or how something is.

Usually, qualitative variables describe qualities using words, but numbers can also be used. For instance, the number of a player's shirt or the number of a racing car
are described using numbers. The numbers don't bear any quantitative meaning though, they are just names, not quantities.


The Team variable is an example of a variable measured on a nominal scale. For any variable measured on a nominal scale:
We can tell whether two individuals are different or not (with respect to that variable).
We can't say anything about the direction and the size of the difference.
We know that it can only describe qualities.


wnba = pd.read_csv('wnba.csv')
intervals = pd.interval_range(start=0, end=600, freq=60)
gr_freq_table_10 = pd.Series([0,0,0,0,0,0,0,0,0,0], index = intervals)

for value in wnba["PTS"]:
    for interval in intervals:
        if value in interval:
            gr_freq_table_10.loc[interval] += 1


print(gr_freq_table_10)


expwnba = wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar()

wnba['Exp_ordinal'].value_counts().plot.pie(figsize = (6,6), autopct = '%.2f%%', title='Percentage of players in WNBA by level of experience')
plt.ylabel('')

wnba['PTS'].plot.hist()
