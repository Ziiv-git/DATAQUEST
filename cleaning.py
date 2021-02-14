null_counts = mvc.isnull().sum() #counting null Values
null_counts_pct = null_counts / mvc.shape[0] * 100 #counting null value percentage
# We'll then add both the counts and percentages to a dataframe to make them easier to compare:
null_df = pd.DataFrame({'null_counts': null_counts, 'null_pct': null_counts_pct})
# Rotate the dataframe so that rows become columns and vice-versa
null_df = null_df.T.astype(int)
# We can see that each of the individual categories have no missing values, but the total_killed column has five missing values.
killed_cols = [col for col in mvc.columns if 'killed' in col]
killed_cols = [col for col in mvc.columns if 'killed' in col]
killed = mvc[killed_cols].copy()
killed_manual_sum= killed.iloc[:, 0:3].sum(axis=1)
killed_mask= killed_manual_sum != killed['total_killed']
killed_non_eq= killed[killed_mask]
We can categorize these into two categories:
#
# Five rows where the total_killed is not equal to the sum of the other columns because the total value is missing.
# One row where the total_killed is less than the sum of the other columns.
# From this, we can conclude that filling null values with the sum of the columns is a fairly good choice for our imputation, given that only six rows out of around 58,000 don't match this pattern.
# In order to execute this, we'll learn to use the Series.mask() method. Series.mask() is useful when you want to replace certain values in a series based off a boolean mask. The syntax for the method is:
Series.mask(bool_mask, val_to_replace)
killed_null = killed['total_killed'].isnull()
killed['total_killed'] = killed['total_killed'].mask(killed_null, killed_manual_sum)

import numpy as np

# fix the killed values
killed['total_killed'] = killed['total_killed'].mask(killed['total_killed'].isnull(), killed_manual_sum)
killed['total_killed'] = killed['total_killed'].mask(killed['total_killed'] != killed_manual_sum, np.nan)

# Create an injured dataframe and manually sum values
injured = mvc[[col for col in mvc.columns if 'injured' in col]].copy()
injured_manual_sum = injured.iloc[:,:3].sum(axis=1)
injured['total_injured']= injured['total_injured'].mask(injured['total_injured'].isnull(), injured_manual_sum)
injured['total_injured']= injured['total_injured'].mask(injured['total_injured'] != injured_manual_sum, np.nan)

Let's summarize the count of null values before and after our changes:


summary = {
    'injured': [
        mvc['total_injured'].isnull().sum(),
        injured['total_injured'].isnull().sum()
    ],
    'killed': [
        mvc['total_killed'].isnull().sum(),
        killed['total_killed'].isnull().sum()
    ]
}
print(pd.DataFrame(summary, index=['before','after']))

mvc['total_injured']= injured['total_injured']
mvc['total_killed']= killed['total_killed']



import matplotlib.pyplot as plt
import seaborn as sns

def plot_null_correlations(df):
    # create a correlation matrix only for columns with at least
    # one missing value
    cols_with_missing_vals = df.columns[df.isnull().sum() > 0]
    missing_corr = df[cols_with_missing_vals].isnull().corr()

    # create a mask to avoid repeated values and make
    # the plot easier to read
    missing_corr = missing_corr.iloc[1:, :-1]
    mask = np.triu(np.ones_like(missing_corr), k=1)

    # plot a heatmap of the values
    plt.figure(figsize=(20,14))
    ax = sns.heatmap(missing_corr, vmin=-1, vmax=1, cbar=False, cmap='RdBu', mask=mask, annot=True)

    # format the text in the plot to make it easier to read
    for text in ax.texts:
        t = float(text.get_text())
        if -0.05 < t < 0.01:
            text.set_text('')
        else:
            text.set_text(round(t, 2))
        text.set_fontsize('x-large')
    plt.xticks(rotation=90, size='x-large')
    plt.yticks(rotation=0, size='x-large')

    plt.show()

veh_cols= [c for c in mvc.columns if 'vehicle' in c]
plot_null_correlations(mvc[veh_cols])

col_labels = ['v_number', 'vehicle_missing', 'cause_missing']

vc_null_data = []

for v in range(1,6):
    v_col = 'vehicle_{}'.format(v)
    c_col = 'cause_vehicle_{}'.format(v)
    v_null = (mvc[v_col].isnull() & mvc[c_col].notnull()).sum()
    c_null = (mvc[c_col].isnull() & mvc[v_col].notnull()).sum()
    vc_null_data.append([v, v_null, c_null])

vc_null_df= pd.DataFrame(vc_null_data, columns= col_labels)

# To convert a dataframe to a single column of values, we use the DataFrame.stack() method, which stacks a dataframe object into a Series object.
v_cols = [c for c in mvc.columns if c.startswith("vehicle")]
vehicles = mvc[v_cols]
vehicles_1d= vehicles.stack()
vehicle_counts= vehicles_1d.value_counts()
top10_vehicles= vehicle_counts.head(10)


def summarize_missing():
    v_missing_data = []

    for v in range(1,6):
        v_col = 'vehicle_{}'.format(v)
        c_col = 'cause_vehicle_{}'.format(v)

        v_missing = (mvc[v_col].isnull() & mvc[c_col].notnull()).sum()
        c_missing = (mvc[c_col].isnull() & mvc[v_col].notnull()).sum()

        v_missing_data.append([v, v_missing, c_missing])

    col_labels = columns=["vehicle_number", "vehicle_missing", "cause_missing"]
    return pd.DataFrame(v_missing_data, columns=col_labels)

summary_before = summarize_missing()

for v in range(1,6):
    v_col = 'vehicle_{}'.format(v)
    c_col = 'cause_vehicle_{}'.format(v)
    # create a mask for each column
    v_missing_mask = mvc[v_col].isnull() & mvc[c_col].notnull()
    c_missing_mask = mvc[c_col].isnull() & mvc[v_col].notnull()

# replace the values matching the mask for each column
    mvc[v_col] =  mvc[v_col].mask(v_missing_mask, "Unspecified")
    mvc[c_col] =  mvc[c_col].mask(c_missing_mask, "Unspecified")

summary_after = summarize_missing()

sup_data = pd.read_csv('supplemental_data.csv')

location_cols = ['location', 'on_street', 'off_street', 'borough']
null_before = mvc[location_cols].isnull().sum()
for col in location_cols:
    mvc[col] = mvc[col].mask(mvc[col].isnull(), sup_data[col])

null_after = mvc[location_cols].isnull().sum()
