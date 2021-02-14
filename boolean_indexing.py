import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
#  np.array.shape gives results in tuple form
taxi_shape = taxi.shape
# to remove header
taxi = taxi[1:]


# boolean array/ masks/ vectors
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = (a < 3)
print(a_bool)

b_bool = (b == 'blue')
print(b_bool)

c_bool = (c > 100)
print(c_bool)


#   boolean indexing
pickup_month = taxi[:,1]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]
print(february_rides)

#  The only limitation is that the boolean array must have the same length as the dimension you're indexing
# selecting the columns
tip_amount = taxi[:,12]
# setting the criteria for boolean indexing
tip_bool = tip_amount > 50
# finding the top tips
top_tips = taxi[tip_bool,5:14]
print(top_tips)


# modifying Values
# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
taxi_modified[1066,5] = 1
taxi_modified[:,0] = 16
taxi_modified[550:552,7] = taxi[:,7].mean()

# Select the fourteenth column (index 13) in taxi_copy. Assign it to a variable named total_amount.
# For rows where the value of total_amount is less than 0, use assignment to change the value to 0.
# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()
total_amount = taxi[:,13]
t_bool = total_amount < 0
total_amount[t_bool] = 0

# For rows where the value for the column index 5 is equal to 2 (JFK Airport), assign the value 1 to column index 15.
# For rows where the value for the column index 5 is equal to 3 (LaGuardia Airport), assign the value 1 to column index 15.
# For rows where the value for the column index 5 is equal to 5 (Newark Airport), assign the value 1 to column index 15.
taxi_modified[taxi_modified[:, 5] == 2, 15] = 1
taxi_modified[taxi_modified[:, 5] == 3, 15] = 1
taxi_modified[taxi_modified[:, 5] == 5, 15] = 1

# Calculate how many trips from taxi had Laguardia Airport as their destination:
# Use boolean indexing to select only the rows where the dropoff_location_code column (column index 6) has a value that corresponds to Laguardia. Assign the result to laguardia.
# Calculate how many rows are in the new laguardia array. Assign the result to laguardia_count.
# taxi_modified[taxi_modified[:, 5] == 2, 15] = 1


jfk = taxi[taxi[:,6] == 2]
jfk_count = jfk.shape[0]
#  Because we are interested in the number of rows only, you will need to use [0] to extract the length of the first dimension only.
print(jfk_count)

laguardia = taxi[taxi[:, 6] == 3]
laguardia_count = laguardia.shape[0]
print(laguardia_count)

newark = taxi[taxi[:,6] == 5]
newark_count = newark.shape[0]
print(newark_count)


trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
# Create a new ndarray, cleaned_taxi, containing only rows for which the values of trip_mph are less than 100.
cleaned_taxi = taxi[trip_mph < 100]
print(cleaned_taxi.shape[0])
# Calculate the mean of the trip_distance column of cleaned_taxi. Assign the result to mean_distance.
mean_distance = cleaned_taxi[:,7].mean()
print(mean_distance)
# Calculate the mean of the trip_length column of cleaned_taxi. Assign the result to mean_length
mean_length = cleaned_taxi[:,8].mean()
print(mean_length)
# Calculate the mean of the total_amount column of cleaned_taxi. Assign the result to mean_total_amount.
mean_total_amount = cleaned_taxi[:,13].mean()
print(mean_total_amount)
