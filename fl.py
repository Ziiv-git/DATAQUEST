import pandas as pd
import datetime as dt

data = pd.read_csv("rfm_xmas19.txt", parse_dates=["trans_date"])
group_by_customer = data.groupby("customer_id")
last_transaction = group_by_customer["trans_date"].max()
best_churn = pd.DataFrame(last_transaction) #converting into DataFrame
#by setting the date 3 months from now todefine churning, and apply it to find out the customers who have churned
def churning(date):
    cutoff_day= dt.datetime(2019,10,16)
    if date < cutoff_day:
        return 1
    else:
        return 0
best_churn['churned'] = best_churn['trans_date'].apply(churning)

#to get the number of purchases and the total amount spent by each customer — the necessary components for this score.
best_churn["nr_of_transactions"] = group_by_customer.size()
# aggregating method to get the total amount spent by each customer as a columns
best_churn['amount_spent'] = group_by_customer.sum()
# Drop the trans_date column
best_churn.drop('trans_date', axis='columns', inplace=True)


# ranges of nr_of_transactions and amount_spent are.
best_churn[["nr_of_transactions", "amount_spent"]].describe().loc[["min", "max"]]
# nr_of_transactions ranges between 4 and 39, while amount_spent ranges between 149 and 2933


# calculating the score by min-max feature scaling factor. here its done between the spent amount and no of transactions
best_churn["scaled_tran"] = (best_churn["nr_of_transactions"] \
                             - best_churn["nr_of_transactions"].min()) \
                             / (best_churn["nr_of_transactions"].max() \
                             - best_churn["nr_of_transactions"].min())
best_churn["scaled_amount"] = (best_churn["amount_spent"] \
                               -best_churn["amount_spent"].min()) \
                               / (best_churn["amount_spent"].max()\
                               - best_churn["amount_spent"].min())
best_churn["score"] = 100*(.5*best_churn["scaled_tran"] \
                           + .5*best_churn["scaled_amount"])
best_churn.sort_values("score", inplace=True, ascending=False)



# With all this in mind, you decide to employ the following strategy to determine the cutoff point:
# --Find the mean of the transactions and compute 30% of that. Make this the value of the coupon;
# --Divide the budget by the value obtained above to get the number of coupons you're going to be sending out;
# --Pick the first n churned customers where n is the result of the calculation done in the previous step. This is your cutoff point.
coupon = data['tran_amount'].mean()*0.3
nr_of_customers = 1000/coupon



# Create a dataframe with the top 50 churned customers. Filter best_churn for only the churned customers.
top_50_churned = best_churn.loc[best_churn['churned'] == 1].head(50)
# saving to a text file
top_50_churned.to_csv('best_customers.txt')
