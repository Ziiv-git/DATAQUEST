import pandas as pd
df = pd.read_csv("nps.csv", parse_dates=["event_date"])
# a numeric column in df called yearmonth that stores the year and the month of each row in the yyyymm format.
year = df['event_date'].dt.year
month = df['event_date'].dt.month
df['yearmonth'] = 100*year + month

def categorize(score):
    """Returns NPS category"""
    if score in range(0,7):
        return "Detractor"
    elif score in (7, 8):
        return "Passive"
    elif score in (9,10):
        return "Promoter"
    return None
#  column in df called "category" that assigns the category corresponding to its score to each row, as per the function created above.
df['category'] = df['score'].apply(categorize)
# df.head(5)
nps = df.pivot_table(index='yearmonth', columns='category', aggfunc='size') #new dataframe
# nps.head(5)
nps['total_responses'] = nps.sum(axis='columns') #new column in nps whose values are the sum of the values of each row to get the total number of responses for the month
# nps.head(5)
nps['nps'] = (nps['Promoter'] - nps['Detractor']) / nps['total_responses'] #creating the nps score
# nps.head(5)
nps['nps'] = (nps['nps'] * 100).astype(int)
nps.head()


ax = nps.reset_index().plot(kind="line", x="yearmonth",y="nps",figsize=(12,6), legend=False)
ax.set_xticks(nps.index)
ax.set_xticklabels(nps.index, rotation=45)
