(.+//([\w\.]+0/?(.*)
#
# Hacker News is a site started by the startup incubator Y Combinator, where user-submitted stories (known as "stories") are
# voted and commented upon, similar to reddit. Hacker News is extremely popular in technology and startup circles; stories that
# make it to the top of Hacker News' listings can get hundreds of thousands of visitors
# The dataset we will be working with is based off this CSV of Hacker News stories from September 2015 to September 2016.
# The columns in the dataset are explained below:
# id: The unique identifier from Hacker News for the story
# title: The title of the story
# url: The URL that the stories links to, if the story has a URL
# num_points: The number of points the story acquired, calculated as the total number of upvotes minus the total number of downvotes
# num_comments: The number of comments that were made on the story
# author: The username of the person who submitted the story
# created_at: The date and time at which the story was submitted
string_list = ["Julie's favorite color is Blue.",
               "Keli's favorite color is Green.",
               "Craig's favorite colors are blue and red."]
pattern = "Blue"
for s in string_list:
    if re.search(pattern, s):
        print("Match")
    else:
        print("No Match")
# for loop
import re
titles = hn["title"].tolist()
python_mentions = 0
pattern= '[Pp]ython'
for title in titles:
    if re.search(pattern,title):
        python_mentions+=1
print(python_mentions)
# vectorisation
pattern = '[Pp]ython'
titles = hn['title']
python_mentions = titles.str.contains(pattern).sum()
ruby_titles= titles[titles.str.contains('[Rr]uby')]
 # we could use braces ({}) to specify that a character repeats in our regular expression. The name for this type of
 # regular expression syntax is called a quantifier. Quantifiers specify how many of the previous character our pattern
 # requires, which can help us when we want to match substrings of specific lengths.
# we're going to find how many titles in our dataset mention email or e-mail. To do this, we'll need to use ?, the optional quantifier,
# to specify that the dash character - is optional in our regular expression.
email_bool= titles.str.contains('e-?mail')
email_count= email_bool.sum()
email_titles= titles[email_bool]
# # To match the substring "[pdf]", we can use backslashes to escape both the open and closing brackets: \[pdf\].
# The one that we'll be using to match characters in tags is \w, which represents any number or letter. Each character class
# represents a single character, so to match multiple characters (e.g. words like video and pdf), we'll need to combine them
# with quantifiers.
# In order to match word characters between our brackets, we can combine the word character class (\w) with the 'one or more'
# quantifier (+), giving us a combined pattern of \w+.
# This will match sequences like pdf, video, Python, and 2018 but won't match a sequence containing a space or punctuation
# character like PHP-DEV or XKCD Flowchart. If we wanted to match those tags as well, we could use .+
pattern = "\[\w+\]"
tag_titles= titles[titles.str.contains(pattern)]
tag_count= tag_titles.shape[0]
# recommend using raw strings for every regex you write, rather than remember which sequences are escape sequences and using raw strings
# selectively. That way, you'll never encounter a situation where you forget or overlook something which causes your regex to break.
# In the previous screen, we were able to calculate that 444 of the 20,100 Hacker News stories in our dataset contain tags.
# What if we wanted to find out what the text of these tags were, and how many of each are in the dataset?
# In order to do this, we'll need to use capture groups. Capture groups allow us to specify one or more groups within our match
# that we can access separately. In this mission, we'll learn how to use one capture group per regular expression, but in the
# next mission we'll learn some more complex capture group patterns.
# We specify capture groups using parentheses.
pattern = r"\[(\w+)\]"
tag_5_matches = tag_5.str.extract(pattern, expand=False)
print(tag_5_matches)
# we specify expand=False with the Series.str.extract() method to return a series. If we then use Series.value_counts() we can quickly
# get a frequency table of the tags:
tag_5_freq = tag_5_matches.value_counts()
print(tag_5_freq)
pattern = r"\[(\w+)\]"
tag_freq = titles.str.extract(pattern, expand=False).value_counts()
pattern= r'[Jj]ava[^Ss]'
java_titles = titles[titles.str.contains(pattern)]
# boundary anchor
pattern= r'\b[Jj]ava\b'
java_titles= titles[titles.str.contains(pattern)]
# beginning anchor and ending anchor
pattern= r'^\[(\w+)\]'
beginning_count= titles.str.contains(pattern).sum()
ending_count= titles.str.contains(r'\[(\w+)\]$').sum()
pattern= r'\be[\-\s]?mails?\b'
email_mentions= titles.str.contains(pattern,flags=re.I).sum()
sql_counts= titles.str.contains(r'sql',flags=re.I).sum()
# Recall that we specify expand=False with the Series.str.extract() method to return a series.
# Lastly, we use the Series.value_counts() method to create a frequency table of those capitalizations:
 # created a new dataframe, hn_sql, including only rows that mention a SQL flavor.
hn_sql = hn[hn['title'].str.contains(r"\w+SQL", flags=re.I)].copy()
hn_sql['flavor']= hn_sql['title'].str.extract(r'(\w+sql)', flags=re.I, expand=False)
hn_sql['flavor']= hn_sql['flavor'].str.lower()
sql_pivot= hn_sql.pivot_table(index='flavor', values='num_comments')
pattern= r'python ([\d\.]+)'
py_versions= hn['title'].str.extract(pattern, flags=re.I, expand=False)
py_versions_freq= dict(py_versions.value_counts())#creating a dictionary of frequency table
def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10
pattern = r"\b[Cc]\b[^.+]"
first_ten= first_10_matches(pattern)
# These tips can help you remember the syntax for lookarounds:
# Inside the parentheses, the first character of a lookaround is always ?.
# If the lookaround is a lookbehind, the next character will be <, which you can think of as an arrow head pointing behind the match.
# The next character indicates whether the lookaround is positive (=) or negative (!).
test_cases = ['Red_Green_Blue',
              'Yellow_Green_Red',
              'Red_Green_Red',
              'Yellow_Green_Blue',
              'Green']
def run_test_cases(pattern):
    for tc in test_cases:
        result = re.search(pattern, tc)
        print(result or "NO MATCH")
run_test_cases(r"Green(?=_Blue)") #+ve lookahead
run_test_cases(r"Green(?!_Red)")#-ve lookahead
run_test_cases(r"(?<=Red_)Green")# +ve lookbehind
run_test_cases(r"(?<!Yellow_)Green")# -ve lookbehind
# Match instances of C or c where they are not preceded or followed by another word character.
# From the match above:
# Exclude instances where it is followed by a . or + character, without removing instances where the match occurs at the
# end of the sentence.
# Exclude instances where the word 'Series' immediately precedes the match.
pattern= r'(?<!Series\s)\b[Cc]\b((?![+.])|\.$)'
c_mentions = titles.str.contains(pattern).sum()
# finding repeated words
pattern= r'\b(\w+)\s\1\b'
repeated_words = titles[titles.str.contains(pattern)]
email_variations = pd.Series(['email', 'Email', 'e Mail',
                        'e mail', 'E-mail', 'e-mail',
                        'eMail', 'E-Mail', 'EMAIL'])
pattern= r'\be[-\s]?mail'
email_uniform= email_variations.str.replace(pattern, 'email', flags=re.I)
titles_clean = titles.str.replace(pattern,'email', flags=re.I)

test_urls = pd.Series([
 'https://www.amazon.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429',
 'http://www.interactivedynamicvideo.com/',
 'http://www.nytimes.com/2007/11/07/movies/07stein.html?_r=0',
 'http://evonomics.com/advertising-cannot-maintain-internet-heres-solution/',
 'HTTPS://github.com/keppel/pinn',
 'Http://phys.org/news/2015-09-scale-solar-youve.html',
 'https://iot.seeed.cc',
 'http://www.bfilipek.com/2016/04/custom-deleters-for-c-smart-pointers.html',
 'http://beta.crowdfireapp.com/?beta=agnipath',
 'https://www.valid.ly?param',
 'http://css-cursor.techstream.org'
])

pattern = r'https?://([\w\-\.]+)'
test_urls_clean= test_urls.str.extract(pattern, flags=re.I, expand=False)
domains= hn['url'].str.extract(pattern, expand=False, flags=re.I)
top_domains= domains.value_counts().head(5)
# 8/4/2016	11:52
# 1/26/2016	19:30
# 6/23/2016	22:20
# 6/17/2016	0:01
# 9/30/2015	4:12
pattern = r"(.+)\s(.+)"
dates_times = created_at.str.extract(pattern)
print(dates_times)
pattern = r'(https?)://([\w\-\.]+)/?(.*)'#extracting url in th form of protocol, domain and pagepath
test_url_parts= test_urls.str.extract(pattern, flags=re.I, expand=False)
url_parts= hn['url'].str.extract(pattern, flags=re.I, expand=True)
pattern = r"(?P<protocol>https?)://(?P<domain>[\w\.\-]+)/?(?P<path>.*)" #naming the capture groups
url_parts= hn['url'].str.extract(pattern, flags=re.I, expand=False)
