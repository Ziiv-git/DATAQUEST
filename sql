In many real-word situations, data is distributed across many sources. SQL allows us to select specific data and transform it to
fit our needs. For example, working with spreadsheets can be difficult if the data we need to answer our question is distributed
across many files. SQL allows us to structure our data in a way that makes it accessible from one place.
SELECT *
  FROM recent_grads;

select * from recent_grads limit 5;

select Major, ShareWomen from recent_grads;

select Major, ShareWomen from recent_grads where ShareWomen < 0.5;

select Major, Major_category, Median, ShareWomen
from recent_grads
where ShareWomen > 0.5
and Median > 50000;

select Major, Median, Unemployed
from recent_grads
where Median >= 10000
or Men > Women
limit 20;

select Major, Major_category, ShareWomen, Unemployment_rate
from recent_grads
where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);

select Major, ShareWomen, Unemployment_rate
from recent_grads
where ShareWomen > 0.3 and Unemployment_rate < 0.1
order by ShareWomen desc;

select Major_category, Major, Unemployment_rate
from recent_grads
where Major_category = 'Engineering' or Major_category = 'Physical Sciences'
order by Unemployment_rate asc;

select MIN(Unemployment_rate)
from recent_grads;
