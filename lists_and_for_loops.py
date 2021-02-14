opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
rating_sum = 0
rating = []
for row in apps_data[1:]:
    rating = row[7]
    rating_sum = rating_sum + float(rating)
print(rating_sum)
avg_rating = rating_sum/7197
print(avg_rating)



# NOTE: computing average rating for free apps
free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)

avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)


# NOTE: computing average rating for non-free AppleStore
non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price != 0.0:
        non_free_apps_ratings.append(rating)

avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

if avg_rating_non_free >= avg_rating_free:
    print('Free apps are not good')
else:
    print('Free apps are better')


non_games_ratings = []
gaming_apps_ratings = []
for row in apps_data[1:]:
    genre = row[11]
    if genre != "Games":
        non_games_ratings.append(float(row[7]))
    else:
        gaming_apps_ratings.append(float(row[7]))

avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)

avg_rating_games = sum(gaming_apps_ratings) / len(gaming_apps_ratings)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)


avg_games_social = sum(games_social_ratings) / len(games_social_ratings)

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])

    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)

avg_free = sum(free_games_social_ratings) / len(free_games_social_ratings)

# Non-free apps (average)
non_free = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        non_free.append(rating)

avg_non_free = sum(non_free) / len(non_free)

# NOTE:  adding a column
for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append('free')
    else:
        app.append('non-free')
apps_data[0].append('free_or_not')
print(apps_data[0])

content_ratings = ['4+', '9+', '12+', '17+']
nums = [4433, 987, 1155, 622]
content_rating_numbers = [content_ratings, nums]

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
over_9 = content_ratings['9+']
over_17 = content_ratings['17+']
print(over_17)
print(over_9)

content_ratings = {}
content_ratings['4+'] = 4433

content_ratings['9+'] = 987

content_ratings['12+'] = 1155


content_ratings['17+'] = 622

over_12_n_apps = content_ratings['12+']
print(over_12_n_apps)

# NOTE: because we can't use dictionaries or lists as keys
{4: 'four',
1.5: 'one point five',
'string_key': 'string_value',
True: 'True',
[1,2,3]: 'a list',
{10: 'ten'}: 'a dictionary'}

# NOTE: to count unique values and updating in dictionary
content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+':0}
for row in apps_data[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
print(content_ratings)

# NOTE: adding in empty dictionary from a list
content_ratings = {}
for row in apps_data[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1

print(content_ratings)

genre_counting = {}
for row in apps_data[1:]:
    genre = row[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1

# NOTE: getting the percentage
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
for rating in content_ratings:
    content_ratings[rating] /= total_number_of_apps
    content_ratings[rating] *= 100
print(content_ratings)
percentage_17_plus = content_ratings['17+']
print(percentage_17_plus)
percentage_15_allowed = content_ratings['4+'] + content_ratings['12+'] + content_ratings['9+']
print(percentage_15_allowed)

# NOTE: from the dictionary calcualting the percentage and proportion and adding it into another dictionary
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
c_ratings_percentages = {}
c_ratings_proportions = {}
for key in content_ratings:
    proportion = content_ratings[key] / total_number_of_apps
    c_ratings_proportions[key] = proportion
    percentage = proportion*100
    c_ratings_percentages[key] = percentage

print(c_ratings_proportions)
print(c_ratings_percentages)

# NOTE: counting total ratings of an app from the column and seeing min and max ratings, then based on that created frequency
# NOTE: intervals, thereafter counted total ratings based on that frequency
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
rating_count_tot = []
for row in apps_data[1:]:
    rating_count = float(row[5])
    rating_count_tot.append(rating_count)
ratings_min = min(rating_count_tot)
ratings_max = max(rating_count_tot)
print(rating_count_tot[:3])

user_ratings_freq = {'0 - 10000': 0, '10000 - 100000': 0, '100000 - 500000': 0,'500000 - 1000000': 0, '1000000+': 0}

for row in apps_data[1:]:
    user_ratings = int(row[5])

    if user_ratings <= 10000:
        user_ratings_freq['0 - 10000'] += 1

    elif 10000 < user_ratings <= 100000:
        user_ratings_freq['10000 - 100000'] += 1

    elif 100000 < user_ratings <= 500000:
        user_ratings_freq['100000 - 500000'] += 1

    elif 500000 < user_ratings <= 1000000:
        user_ratings_freq['500000 - 1000000'] += 1

    elif user_ratings > 1000000:
        user_ratings_freq['1000000+'] += 1

print(user_ratings_freq)

# NOTE: using functions to generate rows
def extract(i):
    new_list = []
    for row in apps_data[1:]:
        r = row[i]
        new_list.append(r)
    return new_list

genres = extract(11)
print(genres)

# NOTE: using functions to produce a list of particular column and then from the list
# NOTE: creating a dictionary of frequency from that column
def extract(index):
    column = []
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)
    return column

genres = extract(11)
print(genres[:3])

def freq_table(column):
    frequency_table = {}
    for value in column:
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    return frequency_table

genres_ft = freq_table(genres)
print(genres_ft)

# NOTE:  creating the above two functions in one same function
def freq_table(index):
    frequency_table = {}

    for row in apps_data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1

    return frequency_table

ratings_ft = freq_table(7)

# NOTE:  same above functionaities but by using two parameters
def freq_table(data_set,index):
    frequency_table = {}

    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1

    return frequency_table

ratings_ft = freq_table(apps_data, 7)
print(ratings_ft)


opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
print(avg_price)


# INITIAL CODE, tuple
def open_dataset(file_name='AppleStore.csv', header=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    if header:
        return data[0], data[1:]
    else:
        return data
header, apps_data = open_dataset()
