import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor() #returning a cursor class

query = "select * from recent_grads;"
cursor.execute(query) #executing query
results = cursor.fetchall()
# print(results[0:2])
query = 'select major from recent_grads;'
majors = cursor.execute(query).fetchall()
# print(majors[0:3])
query = 'select Major, Major_category from recent_grads;'
five_results = cursor.execute(query).fetchmany(5)
conn.close()
query = 'select Major from recent_grads order by Major desc;'
reverse_alphabetical = cursor.execute(query).fetchall()
