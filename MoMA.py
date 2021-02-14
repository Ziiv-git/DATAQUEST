from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

age1 = "I am thirty-one years old"
age2 = age1.replace('one','two')
print(age2)

# NOTE: to replace and append that changed value back again to the lists
for nation in moma:
    n= nation[2]
    n1 = n.replace('(', '')
    nationality = n1.replace(')', '')
    nation[2] = nationality

for gender in moma:
    g = gender[5]
    g = g.replace('(', '')
    g = g.replace(')', '')
    gender[5] = g


    for row in moma:
    # fix the capitalization and missing
    # values for the gender column
    gender = row[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender

    # fix the capitalization and missing
    # values for the nationality column
    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality


    def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date
for row in moma:
    birth_date = row[3]
    death_date = row[4]

    birth_date = clean_and_convert(birth_date)
    death_date = clean_and_convert(death_date)

    row[3] = birth_date
    row[4] = death_date


# NOTE: for stripping of characters in the list using function and calling that function from a for loop

    test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = []
for d in test_data:
    date = strip_characters(d)
    stripped_test_data.append(date)

print(stripped_test_data)




test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(string):
    for s in string:
        if '-' in s:
            s1 = s.split('-')
            avg = (int(s1[0]) + int(s1[1]))/2
            s = round(avg)
        else:
             s = int(s)
    return s

processed_test_data = []

for date in stripped_test_data:
    d = process_date(date)
    processed_test_data.append(d)

print(processed_test_data)




# NOTE:  stripping date converting it into int, also if there is a range that number is average and appended back

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']
def process_date(date):
    if "-" in date:
        split_date = date.split("-")
        date_one = split_date[0]
        date_two = split_date[1]
        date = (int(date_one) + int(date_two)) / 2
        date = round(date)
    else:
        date = int(date)
    return date

processed_test_data = []

for d in stripped_test_data:
    date = process_date(d)
    processed_test_data.append(date)

for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)
    row[6] = date

# NOTE: cutting and slicing and adding to the lists by first converting each element to string
decades = []
for age in final_ages:
    if age == 'Unknown':
        decade = age
    else:
        decade = str(age)
        decade = decade[:-1]
        decade = decade + '0s'
    decades.append(decade)

print(decades[:3])

# NOTE: creating a dict out of list basically creating a kev-value pair or you can say a table
decade_frequency = {}
for decade in decades:
    if decade not in  decade_frequency:
        decade_frequency[decade] = 1
    else:
        decade_frequency[decade] += 1

artist_freq = {}
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1


def artist_summary(artist):
#     printing summary of artist
    num_artworks = artist_freq[artist]
    return 'There are {} artworks by {} in the data set'.format((num_artworks),(artist))

artist_summary('Henri Matisse')

artist_gender = {}
for row in moma:
    gender = row[5]
    if gender not in artist_gender:
        artist_gender[gender] = 1
    else:
        artist_gender[gender] += 1
print(artist_gender)

for gender,num in artist_gender.items():
    print('There are {:,} artworks by {} artists'.format((num),(gender)))
