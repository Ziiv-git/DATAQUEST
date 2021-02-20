SELECT [column_names] FROM [table_name_one]
INNER JOIN [table_name_two] ON [join_constraint];

SELECT * FROM facts
INNER JOIN cities ON cities.facts_id = facts.id
LIMIT 5;

SELECT *
FROM facts
INNER JOIN cities ON cities.facts_id = facts.id
LIMIT 10;

SELECT c.*, f.name AS country_name
FROM facts AS f
INNER JOIN cities AS c ON c.facts_id = f.id
LIMIT 5;

SELECT f.name country, c.name capital_city
FROM cities c
INNER JOIN facts f ON f.id = c.facts_id
WHERE c.capital = 1
LIMIT 10;


SELECT f.name AS country, f.population
FROM facts AS f
LEFT JOIN cities AS c on c.facts_id = f.id
WHERE c.name IS NULL;



SELECT c.name AS capital_city, f.name AS country, c.population
FROM facts AS f
INNER JOIN cities AS c ON c.facts_id = f.id
WHERE c.capital = 1
ORDER BY c.population DESC
LIMIT 10;



SELECT c.name capital_city, f.name country, c.population
FROM facts f
INNER JOIN (SELECT *
            FROM cities c
            WHERE c. capital = 1 AND c.population > 10000000)
            c ON c.facts_id = f.id
ORDER BY c.population DESC;


-- Write a query that generates output as shown above. The query should include:
-- The following columns, in order:
-- country, the name of the country.
-- urban_pop, the sum of the population in major urban areas belonging to that country.
-- total_pop, the total population of the country.
-- urban_pct, the percentage of the population within urban areas, calculated by dividing urban_pop by total_pop.
-- Only countries that have an urban_pct greater than 0.5.
-- Rows should be sorted by urban_pct in ascending order.
SELECT f.name country, c.urban_pop,  f.population total_pop, (c.urban_pop / CAST(f.population AS FLOAT)) urban_pct
FROM facts f
INNER JOIN (SELECT facts_id, SUM(population) urban_pop
            FROM cities c
            GROUP BY facts_id)
            c on c.facts_id = f.id
WHERE urban_pct > 0.5
ORDER by urban_pct ASC;


-- joining more than two tables based on primary keys
SELECT * FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
WHERE invoice_id = 3;



SELECT il.track_id, t.name track_name, mt.name track_type, il.unit_price, il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
WHERE il.invoice_id = 4;


SELECT
    il.track_id,
    t.name track_name,
    ar.name artist_name,
    mt.name track_type,
    il.unit_price,
    il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
INNER JOIN album al ON al.album_id = t.album_id
INNER JOIN artist ar on ar.artist_id = al.artist_id
WHERE il.invoice_id = 4;


SELECT
    il.invoice_line_id,
    il.track_id,
    ta.artist_name
FROM invoice_line il
INNER JOIN (
            SELECT
                t.track_id,
                ar.name artist_name
            FROM track t
            INNER JOIN album al ON al.album_id = t.album_id
            INNER JOIN artist ar ON ar.artist_id = al.artist_id
           ) ta
           ON ta.track_id = il.track_id
ORDER BY il.invoice_line_id
LIMIT 10;


SELECT
    ta.artist_name artist,
    COUNT(*) tracks_purchased
FROM invoice_line il
INNER JOIN (
            SELECT
                t.track_id,
                ar.name artist_name
            FROM track t
            INNER JOIN album al ON al.album_id = t.album_id
            INNER JOIN artist ar ON ar.artist_id = al.artist_id
           ) ta
           ON ta.track_id = il.track_id
GROUP BY artist
ORDER BY tracks_purchased DESC LIMIT 10;


SELECT
    ta.album album,
    ta.artist_name artist,
    COUNT(*) tracks_purchased
FROM invoice_line il
INNER JOIN (SELECT
                al.title album,
                t.track_id,
                ar.name artist_name
            FROM track t
            INNER JOIN album al ON al.album_id = t.album_id
            INNER JOIN artist ar ON ar.artist_id = al.artist_id) ta
           ON ta.track_id = il.track_id
GROUP BY album, artist
ORDER BY tracks_purchased DESC
LIMIT 5;



-- recursive join
-- used when we want to join the single table to itself
SELECT
    e1.employee_id,
    e2.employee_id supervisor_id
FROM employee e1
INNER JOIN employee e2 on e1.reports_to = e2.employee_id
LIMIT 4;


 -- strng concatentaion
 SELECT
    album_id,
    artist_id,
    "album id is" || album_id col_1,
    "artist id is" || artist_id col2,
    album_id || artist_id col3
FROM album LIMIT 3;


SELECT
    e1.first_name || " " || e1.last_name employee_name,
    e1.title employee_title,
    e2.first_name || " " || e2.last_name supervisor_name,
    e2.title supervisor_title
FROM employee e1
LEFT JOIN employee e2 ON e1.reports_to = e2.employee_id
ORDER BY 1;


SELECT
    first_name,
    last_name,
    phone
FROM customer
where first_name LIKE '%Belle%';


SELECT
    media_type_id,
    name,
    CASE
        WHEN name LIKE '%Protected%' THEN 1
        ELSE 0
        END
        AS protected
FROM media_type;



SELECT
    c.first_name || " " || c.last_name customer_name,
    COUNT(i.invoice_id) number_of_purchases,
    SUM(i.total) total_spent,
    CASE
        WHEN SUM(i.total) < 40 THEN 'small spender'
        WHEN SUM(i.total) > 100 THEN 'big spender'
        ELSE 'regular'
        END
        AS customer_category
FROM invoice i
INNER JOIN customer c ON c.customer_id = i.customer_id
GROUP BY 1
ORDER BY 1;



WITH track_info AS
    (
     SELECT
         t.name,
         ar.name artist,
         al.title album_name,
         mt.name media_type,
         g.name genre,
         t.milliseconds length_milliseconds
     FROM track t
     INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
     INNER JOIN genre g ON g.genre_id = t.genre_id
     INNER JOIN album al ON al.album_id = t.album_id
     INNER JOIN artist ar ON ar.artist_id = al.artist_id
    )
SELECT * FROM track_info
WHERE album_name = "Jagged Little Pill";





WITH playlist_info AS
    (
     SELECT
         p.playlist_id,
         p.name playlist_name,
         t.name track_name,
         (t.milliseconds / 1000) length_seconds
     FROM playlist p
     LEFT JOIN playlist_track pt ON pt.playlist_id = p.playlist_id
     LEFT JOIN track t ON t.track_id = pt.track_id
    )
SELECT
    playlist_id,
    playlist_name,
    COUNT(track_name) number_of_tracks,
    SUM(length_seconds) length_seconds
FROM playlist_info
GROUP BY playlist_id, playlist_name
ORDER by playlist_id ASC;



CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT c.*
    FROM chinook.invoice i
    INNER JOIN chinook.customer c ON i.customer_id = c.customer_id
    GROUP BY 1
    HAVING SUM(i.total) > 90;
SELECT * FROM chinook.customer_gt_90_dollars;


SELECT * FROM customer_usa
UNION
SELECT * FROM customer_gt_90_dollars;



WITH customers_usa_gt_90 AS
    ( SELECT * FROM customer_usa
      INTERSECT
      SELECT * FROM customer_gt_90_dollars )
SELECT
    e.first_name || " " || e.last_name employee_name,
    COUNT(c.customer_id) customers_usa_gt_90
FROM  employee e
LEFT JOIN customers_usa_gt_90 c ON c.support_rep_id = e.employee_id
WHERE e.title = 'Sales Support Agent'
GROUP BY employee_name
ORDER BY employee_name;


WITH
    customers_india as
        ( SELECT * FROM customer
         WHERE country = "India" ),
    sales_per_customer as
        ( SELECT customer_id, SUM(total) total
          from invoice
          GROUP BY customer_id )
SELECT
    ci.first_name || '' || ci.last_name customer_name,
    spc.total total_purchases
FROM customers_india ci
INNER JOIN sales_per_customer spc ON ci.customer_id = spc.customer_id
ORDER BY 1;










WITH
    customer_country_purchases AS
        (
        SELECT
            i.customer_id,
            c.country,
            SUM(i.total) total_purchases
        FROM invoice i
        INNER JOIN customer c ON i.customer_id = c.customer_id
        GROUP BY 1,2
        ),
    country_max_purchase AS
        (
         SELECT
             country,
             MAX(total_purchases) max_purchase
         FROM customer_country_purchases
         GROUP BY 1
        ),
     country_best_customer AS
        (
         SELECT
            cmp.country,
            cmp.max_purchase,
            (
             SELECT ccp.customer_id
             FROM customer_country_purchases ccp
             WHERE ccp.country = cmp.country AND cmp.max_purchase = ccp.total_purchases
             ) customer_id
          FROM country_max_purchase cmp
          )
SELECT
    cbc.country country,
    c.first_name || " " || c.last_name customer_name,
    cbc.max_purchase total_purchased
FROM customer c
INNER JOIN country_best_customer cbc ON cbc.customer_id = c.customer_id
ORDER BY 1 ASC;
