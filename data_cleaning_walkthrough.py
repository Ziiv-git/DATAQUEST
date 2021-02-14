import pandas as pd
# adding number of csv files in a single dictionary
data_files =   ["ap_2010.csv","class_size.csv","demographics.csv","graduation.csv","hs_directory.csv","sat_results.csv"]
data = {}
for file in data_files:
    path= pd.read_csv('schools/{0}'.format(file))
    key_name= file.replace('.csv','')
    data[key_name]= path
# to read a dataframe from the dictionary
print(data['sat_results'].head())
# Loop through each key in data. For each key:
# Display the first five rows of the dataframe associated with the key.
for key in data:
    print(data[key].head(5))
# Each data set appears to either have a DBN column, or the information we need to create one. That means we can use a DBN column
# to combine the data sets. First we'll pinpoint matching rows from different data sets by looking for identical DBNs, then group all
# of their columns together in a single data set.
# Some fields look interesting for mapping -- particularly Location 1, which contains coordinates inside a larger string.
# Some of the data sets appear to contain multiple rows for each school (because the rows have duplicate DBN values).
# That means we’ll have to do some preprocessing to ensure that each DBN is unique within each data set. If we don't do this,
# we'll run into problems when we combine the data sets, because we might be merging two rows in one data set with one row in
# another data set.
all_survey= pd.read_csv('schools/survey_all.txt', delimiter='\t', encoding='windows-1252')
d75_survey= pd.read_csv('schools/survey_d75.txt', delimiter='\t', encoding='windows-1252')
# merging both the files
survey= pd.concat([all_survey, d75_survey], axis=0)
survey.head(5)
# There are over 2000 columns, nearly all of which we don't need. We'll have to filter the data to remove the unnecessary ones. Working
# with fewer columns will make it easier to print the dataframe out and find correlations within it.
# The survey data has a dbn column that we'll want to convert to uppercase (DBN). The conversion will make the column name consistent
# with the other data sets.
# First, we'll need to filter the columns to remove the ones we don't need. Luckily, there's a data dictionary at the original
# data download location. The dictionary tells us what each column represents. Based on our knowledge of the problem and the
# analysis we're trying to do, we can use the data dictionary to determine which columns to use.
# Based on the dictionary, it looks like these are the relevant columns:
["dbn", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11",
"eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
# These columns will give us aggregate survey data about how parents, teachers, and students feel about school safety, academic
# performance, and more. It will also give us the DBN, which allows us to uniquely identify the school.
survey['DBN']= survey['dbn'] #  copy the data from the dbn column into a new column called DBN
cols= ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11",
"aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey= survey[cols]
survey.shape
data['survey']= survey # adding survey into the dictionary
def pad_csd(num):
    return str(num).zfill(2) #function to apply zero before the num, if the length of the num is one
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd) #creating a new column and padding the csd column
# first to make it a two digit, overall aim is to join the two columns in class_size to make it a dbn column, so first padding
# and then concatenating
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"] #merged two columns to generate a dbn column
print(data["class_size"].head())#checking the result
# we'll need to convert the SAT Math Avg. Score, SAT Critical Reading Avg. Score, and SAT Writing Avg. Score columns in
# the sat_results data set from the object (string) data type to a numeric data type. We can use the pandas.to_numeric()
# method for the conversion. If we don't convert the values, we won't be able to add the columns together.
# t's important to pass the keyword argument errors="coerce" when we call pandas.to_numeric(), so that pandas treats any
# invalid strings it can't convert to numbers as missing values instead.
# After we perform the conversion, we can use the addition operator (+) to add all three columns together.
cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']
for c in cols:
    data["sat_results"][c] = pd.to_numeric(data["sat_results"][c], errors="coerce")
data['sat_results']['sat_score'] = data['sat_results']['SAT Math Avg. Score'] + data['sat_results']['SAT Critical Reading Avg. Score'] + data['sat_results']['SAT Writing Avg. Score']
print(data['sat_results']['sat_score'].head(5))
# Next, we'll want to parse the latitude and longitude coordinates for each school. This will enable us to map the schools and
# uncover any geographic patterns in the data.
# The coordinates are currently in the text field Location 1 in the hs_directory data set.
# We want to extract the latitude, 40.8276026690005, and the longitude, -73.90447525699966. Taken together, latitude and longitude
# make up a pair of coordinates that allows us to pinpoint any location on Earth.
import re
def coords(string):
    pattern= r'\(.+\)'
    coord = re.findall(pattern, string)
    lat= coord[0].split(',')[0].replace('(','')
    return lat
data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(coords)
print(data['hs_directory']['lat'].head(5))

def longitudes(string):
    pattern= r'\(.+\)'
    coord = re.findall(pattern, string)
    long= coord[0].split(',')[1].replace(')','').strip()
    return long
data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(longitudes)
# print(data['hs_directory']['lon'].head(5))

cols= ['lat', 'lon']
for c in cols:
    data['hs_directory'][c]= pd.to_numeric(data['hs_directory'][c], errors='coerce')

print(data['hs_directory'].head(5))











#
# We'll need to condense these data sets so that each value in the DBN column is unique. If not, we'll run into issues when it
# comes time to combine the data sets.
# While the main data set we want to analyze, sat_results, has unique DBN values for every high school in New York City, other
# data sets aren't as clean. A single row in the sat_results data set may match multiple rows in the class_size data set, for example.
# This situation will create problems, because we don't know which of the multiple entries in the class_size data set we should
# combine with the single matching entry in sat_results
# To resolve this issue, we'll condense the class_size, graduation, and demographics data sets so that each DBN is unique.
# As you can see, the first few rows all pertain to the same school, which is why the DBN appears more than once. It looks
# like each school has multiple values for GRADE, PROGRAM TYPE, CORE SUBJECT (MS CORE and 9-12 ONLY), and CORE COURSE (MS CORE and 9-12 ONLY).
# If we look at the unique values for GRADE, we get the following:
# array(['0K', '01', '02', '03', '04', '05', '0K-09', nan, '06', '07', '08',
#        'MS Core', '09-12', '09'], dtype=object)
# Because we're dealing with high schools, we're only concerned with grades 9 through 12. That means we only want to pick
# rows where the value in the GRADE column is 09-12.
# If we look at the unique values for PROGRAM TYPE, we get the following:
# array(['GEN ED', 'CTT', 'SPEC ED', nan, 'G&T'], dtype=object)
# Each school can have multiple program types. Because GEN ED is the largest category by far, let's only select rows where
# PROGRAM TYPE is GEN ED.

class_size = data['class_size'] #class_size here is df which is added by extracting the value of class_size(key) from the dictionary data
# class_size.info()
class_size = class_size[class_size['GRADE '] == '09-12'] #only keeping the rows where column data is 9-12
class_size = class_size[class_size['PROGRAM TYPE'] == 'GEN ED'] #only keeping the certain the program type
print(class_size.head())
#
# As we saw when we displayed class_size on the last screen, DBN still isn't completely unique. This is due to the
# CORE COURSE (MS CORE and 9-12 ONLY) and CORE SUBJECT (MS CORE and 9-12 ONLY) columns.
# CORE COURSE (MS CORE and 9-12 ONLY) and CORE SUBJECT (MS CORE and 9-12 ONLY) seem to pertain to different kinds of classes.
# For example, here are the unique values for CORE SUBJECT (MS CORE and 9-12 ONLY):
# array(['ENGLISH', 'MATH', 'SCIENCE', 'SOCIAL STUDIES'], dtype=object)
# This column only seems to include certain subjects. We want our class size data to include every single class a school
# offers -- not just a subset of them. What we can do is take the average across all of the classes a school offers.
# This will give us unique DBN values, while also incorporating as much data as possible into the average.

# Fortunately, we can use the pandas.DataFrame.groupby() method to help us with this.
# The DataFrame.groupby() method will split a dataframe up into unique groups, based on a given column.
# We can then use the agg() method on the resulting pandas.core.groupby object to find the mean of each column.

# Using the groupby() method, we'll split this dataframe into four separate groups -- one with the DBN 01M292,
# one with the DBN 01M332, one with the DBN 01M378, and one with the DBN 01M448:

# Then, we can compute the averages for the AVERAGE CLASS SIZE column in each of the four groups using the agg() method:
#
# After we group a dataframe and aggregate data based on it, the column we performed the grouping on (in this case DBN)
# will become the index, and will no longer appear as a column in the data itself. To undo this change and keep DBN as a
# column, we'll need to use pandas.DataFrame.reset_index(). This method will reset the index to a list of
# integers and make DBN a column again.
import numpy
class_size = class_size.groupby('DBN').agg(numpy.mean) #grouping the data by dbn and aggregating the mean simultaneously in the groups created
class_size.reset_index(inplace=True) #when we grouped by dbn the dbn column became the index therefore to reset it again as the column
data['class_size'] = class_size # sending the modified the data back to the dictionary
print(data['class_size'].head())
# the only column that prevents a given DBN from being unique is schoolyear. We only want to select rows where schoolyear
# is 20112012. This will give us the most recent year of data, and also match our SAT results data.
data['demographics'] = data['demographics'][data['demographics']['schoolyear'] == 20112012] #only keeping the value when the conditions are met
print(data['demographics'])
data['graduation']= data['graduation'][data['graduation']['Cohort'] == '2006']
data['graduation']= data['graduation'][data['graduation']['Demographic'] == 'Total Cohort']
print(data['graduation'].head())
# . High school students take the AP exams before applying to college. There are several AP exams, each corresponding to a school
# subject. High school students who earn high scores may receive college credit.
# AP exams have a 1 to 5 scale; 3 or higher is a passing score. Many high school students take AP exams -- particularly those who
# attend academically challenging institutions. AP exams are much more rare in schools that lack funding or academic rigor.
# It will be interesting to find out whether AP exam scores are correlated with SAT scores across high schools. To determine
# this, we'll need to convert the AP exam scores in the ap_2010 data set to numeric values first.
cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for c in cols:
    data['ap_2010'][c] = pd.to_numeric(data['ap_2010'][c], errors='coerce')
# changing to numeric from string
print(data['ap_2010'].dtypes)











# Because this project is concerned with determing demographic factors that correlate with SAT score, we'll want to preserve as
# many rows as possible from sat_results while minimizing null values.
# This means that we may need to use different merge strategies with different data sets. Some of the data sets have a lot of
# missing DBN values. This makes a left join more appropriate, because we don't want to lose too many rows when we merge.
# If we did an inner join, we would lose the data for many high schools.
# Some data sets have DBN values that are almost identical to those in sat_results. Those data sets also have information we
# need to keep. Most of our analysis would be impossible if a significant number of rows was missing from demographics, for example.
# Therefore, we'll do an inner join to avoid missing data in these columns.
combined = data["sat_results"] #irst put one data set into new df
combined = combined.merge(data['ap_2010'], on='DBN', how='left') #merging another dataset into our existing df based on left join and using the column DBN
combined = combined.merge(data['graduation'], on='DBN', how='left')
print(combined.head())
combined.shape
to_merge = ['class_size', 'demographics', 'survey', 'hs_directory']
for m in to_merge:
    combined = combined.merge(data[m], on='DBN', how='inner')# using inner join coz most of the data has null values in the following datasets that we will be merging
print(combined.head(5))
combined.shape
# You may have noticed that the inner joins resulted in 116 fewer rows in sat_results. This is because pandas couldn't find the
# DBN values that existed in sat_results in the other data sets. While this is worth investigating, we're currently looking for
# high-level correlations, so we don't need to dive into which DBNs are missing.
# You may also have noticed that we now have many columns with null (NaN) values. This is because we chose to do left joins,
# where some columns may not have had data. The data set also had some missing values to begin with. If we hadn't performed a
# left join, all of the rows with missing data would have been lost in the merge process, which wouldn't have left us
# with many high schools in our data set.
means = combined.mean() #calculating the mean of each column to fill the null values in that respective column with the mean
combined = combined.fillna(means)
combined = combined.fillna(0)
print(combined.head(5))











#
# We've finished cleaning and combining our data! We now have a clean data set on which we can base our analysis.
# Mapping the statistics out on a school district level might be an interesting way to analyze them.
# Adding a column to the data set that specifies the school district will help us accomplish this.
# The school district is just the first two characters of the DBN. We can apply a function over the DBN column of combined
# that pulls out the first two letters.
def extract_first_two(string):
    return string[0:2] #function extracts the first two characters of the string
combined['school_dist'] = combined['DBN'].apply(extract_first_two)
print(combined['school_dist'].head(5))
















#
# In this mission, we'll discover correlations, create plots, and then make maps. The first thing we'll do is find any
# correlations between any of the columns and sat_score. This will help us determine which columns might be interesting to
# plot out or investigate further. Afterwards, we'll perform more analysis and make maps using the columns we've identified.
# Correlations tell us how closely related two columns are. We'll be using the r value, also called Pearson's
# correlation coefficient, which measures how closely two sequences of numbers are correlated.
# An r value falls between -1 and 1. The value tells us whether two columns are positively correlated,
# not correlated, or negatively correlated. The closer to 1 the r value is, the stronger the positive correlation between the
# two columns. The closer to -1 the r value is, the stronger the negative correlation (i.e., the more "opposite" the columns are).
# The closer to 0, the weaker the correlation.
# To really assess whether or not a correlation exists, we need to look at the data using a scatterplot to see its "shape."
correlations = combined.corr()
correlations = correlations['sat_score'] #correlations only for sat_score
print(correlations)
# Unsurprisingly, SAT Critical Reading Avg. Score, SAT Math Avg. Score, SAT Writing Avg. Score, and sat_score are strongly correlated
# with sat_score.
# We can also make some other observations:
# total_enrollment has a strong positive correlation with sat_score. This is surprising because we'd expect smaller schools where
# students receive more attention to have higher scores. However, it looks like the opposite is true -- larger schools tend to do
# better on the SAT.
# Other columns that are proxies for enrollment correlate similarly. These include total_students, N_s, N_p, N_t, AP Test Takers,
# Total Exams Taken, and NUMBER OF SECTIONS.
# Both the percentage of females (female_per) and number of females (female_num) at a school correlate positively with SAT score,
# whereas the percentage of males (male_per) and the number of males (male_num) correlate negatively.
# This could indicate that women do better on the SAT than men.
# Teacher and student ratings of school safety (saf_t_11, and saf_s_11) correlate with sat_score.
# Student ratings of school academic standards (aca_s_11) correlate with sat_score, but this does not hold for ratings
# from teachers and parents (aca_p_11 and aca_t_11).
# There is significant racial inequality in SAT scores (white_per, asian_per, black_per, hispanic_per).
# The percentage of English language learners at the school (ell_percent, frl_percent) has a strong negative correlation with
# SAT scores.
import matplotlib.pyplot as plt
combined.plot.scatter(x="total_enrollment", y="sat_score") #scatterplot
plt.show()
# Judging from the plot we just created, it doesn't appear that there's an extremely strong correlation between sat_score and
# total_enrollment. If there was a very strong correlation, we'd expect all of the points to line up. Instead, there's a large
# cluster of schools, and then a few others going off in three different directions.
# However, there's an interesting cluster of points at the bottom left where total_enrollment and sat_score are both low. T
# his cluster may be what's making the r value so high. It's worth extracting the names of the schools in this cluster so we can
# research them further.
low_enrollment = combined[combined['total_enrollment'] < 1000] #selecting only those having value less than 1000 and adding them into new df
low_enrollment = low_enrollment[low_enrollment['sat_score'] < 1000] #only selecting those who meets the required condition
print(low_enrollment['School Name'])
# Our research on the last screen revealed that most of the high schools with low total enrollment and low SAT scores have
# high percentages of English language learners. This indicates that it's actually ell_percent that correlates strongly with
# sat_score, rather than total_enrollment
combined.plot.scatter(x='ell_percent', y='sat_score')
plt.show()
# One way to make very granular statistics easier to read is to aggregate them. In this case, we will aggregate by district, which will enable us
# to understand how ell_percent varies district-by-district instead of the unintelligibly granular school-by-school variation.
import numpy
districts = combined.groupby('school_dist').agg(numpy.mean) #getting the average of schools based on districts
districts.reset_index(inplace=True) #resetting the index
print(districts.head())
