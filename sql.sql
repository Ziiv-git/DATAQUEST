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

select SUM(Total)
from recent_grads

select COUNT(Major)
from recent_grads
where ShareWomen < 0.5;

select COUNT(*),
COUNT(Unemployment_rate)
from recent_grads;

SELECT AVG(Total), MIN(Men), MAX(Women)
FROM recent_grads;

SELECT Major AS m, Major_category AS mc, Unemployment_rate AS ur
  FROM recent_grads
 WHERE (mc = 'Engineering') AND (ur > 0.04 and ur < 0.08)
 ORDER BY ur DESC

 SELECT COUNT(*) 'Number of Majors', MAX(Unemployment_rate) 'Highest Unemployment Rate'
FROM recent_grads

select COUNT(DISTINCT Major) 'unique_majors', COUNT(DISTINCT Major_category) 'unique_major_categories', COUNT(DISTINCT Major_code) 'unique_major_codes'
from recent_grads;

SELECT Major, Total, Men, Women, Unemployment_rate, LENGTH(Major) AS Length_of_name
FROM recent_grads
ORDER BY Unemployment_rate DESC
LIMIT 3;

SELECT 'Cat: ' || Major_category
FROM recent_grads
LIMIT 2;

SELECT 'Major: ' || LOWER(Major) 'Major', Total, Men, Women, Unemployment_rate, LENGTH(Major) 'Length_of_name'
from recent_grads
ORDER BY Unemployment_rate DESC;

SELECT Major, Major_category, (P75th - P25th) AS quartile_spread
FROM recent_grads
ORDER BY quartile_spread ASC
LIMIT 20;

SELECT CASE
WHEN Sample_size < 200 THEN 'Small'
WHEN Sample_size < 1000 THEN 'Medium'
ELSE 'Large'
END AS Sample_category
FROM recent_grads;

SELECT Major, Sample_size, CASE
WHEN Sample_size < 200 THEN 'Small'
WHEN Sample_size < 1000 THEN 'Medium'
ELSE 'Large'
END AS Sample_category
FROM recent_grads;

SELECT Major_category, SUM(Total) AS Total_graduates
FROM recent_grads
GROUP BY Major_category;

SELECT Major_category, AVG(ShareWomen) AS Average_women
FROM recent_grads
GROUP BY Major_category;

SELECT Major_category, SUM(Women) AS Total_women, AVG(ShareWomen) AS Mean_women, SUM(Total) * AVG(ShareWomen) AS Estimate_women
FROM recent_grads
GROUP BY Major_category;

SELECT Major_category, Sample_category, AVG(ShareWomen) AS Mean_women, SUM(Total) AS Total_graduates
FROM new_grads
GROUP BY Major_category, Sample_category;

SELECT Major_category, AVG(Low_wage_jobs) / AVG(Total) AS Share_low_wage
FROM new_grads
GROUP BY Major_category
HAVING Share_low_wage > .1;

SELECT ROUND(ShareWomen,4) AS Rounded_women, Major_category
FROM new_grads
LIMIT 10;

SELECT Major_category, ROUND(AVG(College_jobs) / AVG(Total), 3) AS Share_degree_jobs
FROM new_grads
GROUP BY Major_category
HAVING Share_degree_jobs < 0.3;

SELECT Major_category, CAST(SUM(Women) AS Float) / CAST(SUM(Total) AS Float) AS SW
FROM new_grads
GROUP BY Major_category
ORDER BY SW;

SELECT Major, Unemployment_rate
FROM recent_grads
WHERE Unemployment_rate < (SELECT AVG(Unemployment_rate)
                           FROM recent_grads);


SELECT COUNT(*),
       (SELECT COUNT(*)
        FROM recent_grads)
FROM recent_grads
WHERE ShareWomen > (SELECT AVG(ShareWomen)
                    FROM recent_grads);



SELECT CAST(COUNT(*) AS FLOAT)/(SELECT COUNT(*)
                                       FROM recent_grads) AS proportion_abv_avg
FROM recent_grads
WHERE ShareWomen > (SELECT AVG(ShareWomen)
                    FROM recent_grads);



SELECT Major_category, Major
FROM recent_grads
WHERE Major_category IN ('Business', 'Humanities & Liberal Arts', 'Education');



SELECT Major_category, Major
  FROM recent_grads
 WHERE Major_category IN (select Major_category
                          from recent_grads
                          GROUP BY Major_category
                          ORDER BY SUM(TOTAL) DESC
                          LIMIT 3);



SELECT AVG(CAST(Sample_size AS FLOAT) / Total) AS avg_ratio
FROM recent_grads;




SELECT Major, Major_category, (CAST(Sample_size AS FLOAT) / Total) AS ratio
FROM recent_grads
WHERE ratio > (SELECT AVG(CAST(Sample_size AS FLOAT) / Total) AS avg_ratio
               FROM recent_grads);
