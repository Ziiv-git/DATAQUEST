# A lot of data aren't accessible through data sets or APIs. They may exist on the Internet as Web pages, though. One way to access the data without waiting for the
# provider to create an API is to use a technique called Web scraping.
#
# Web scraping allows us to load a Web page into Python and extract the information we want. We can then work with the data using standard analysis tools like pandas
# and numpy.
#
# Before we can do Web scraping, we need to understand the structure of the Web page we're working with, then find a way to extract parts of that structure in a
# sensible way.

from bs4 import BeautifulSoup
# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')
# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
body = parser.body
# Get the p tag from the body.
p = body.p
# Print the text inside the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)
head = parser.head
title = head.title
title_text = title.text


parser = BeautifulSoup(content, 'html.parser')
# Get a list of all occurrences of the body tag in the element.
body = parser.find_all("body")
# Get the paragraph tag.
p = body[0].find_all("p")
# Get the text.
print(p[0].text)
head = parser.find_all('head')
title = head[0].find_all('title')
title_text = title[0].text


# Pass in the ID attribute to only get the element with that specific ID.
first_paragraph = parser.find_all("p", id="first")[0]
# print(first_paragraph.text)
second_paragraph = parser.find_all('p', id= 'second')[0]
second_paragraph_text= second_paragraph.text



# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then, take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
# print(first_inner_paragraph.text)
second_inner_paragraph = parser.find_all('p', class_= 'inner-text')[1]
second_inner_paragraph_text = second_inner_paragraph.text
first_outer_paragraph = parser.find_all('p', class_='outer-text')[0]
first_outer_paragraph_text = first_outer_paragraph.text


This CSS will make all of the text inside all paragraphs red:
p{
    color: red
 }
 This CSS will change the text color to red for any paragraphs that have the class inner-text. We select classes with the period or dot symbol (.):
p.inner-text{
    color: red
 }
This CSS will change the text color to red for any paragraphs that have the ID first. We select IDs with the pound or hash symbol (#):
p#first{
    color: red
 }
You can also style IDs and classes without using any specific tags. For example, this CSS will make the element with the ID first red (not just paragraphs):
#first{
    color: red
 }
This CSS will make any element with the class inner-text red:
.inner-text{
    color: red
 }



# Select all of the elements that have the first-item class.
first_items = parser.select(".first-item")
# Print the text of the first paragraph (the first element with the first-item class).
# print(first_items[0].text)
outer_text = parser.select('.outer-text')
first_outer_text = outer_text[0].text
second = parser.select('#second')                                               #working with css style
second_text = second[0].text


This selector will target any paragraph inside a div tag: div p
This selector will target any item inside a div tag that has the class first-item: div .first-item
This one is even more specific. It selects any item that's inside a div tag inside a body tag, but only if it also has the ID first: body div "#first"
This selector zeroes in on any items with the ID first that are inside any items with the class first-item: .first-item #first





# Find the number of turnovers the Seahawks committed.
turnovers = parser.select("#turnovers")[0]
seahawks_turnovers = turnovers.select("td")[1]
seahawks_turnovers_count = seahawks_turnovers.text
# print(seahawks_turnovers_count)
total_plays = parser.select('#total-plays')[0]
patriots_total_plays = total_plays .select('td')[2] #index 1 would represent that of Seahawks
patriots_total_plays_count = patriots_total_plays.text

total_yards = parser.select("#total-yards")[0]
seahawks_total_yards = total_yards.select("td")[1]
seahawks_total_yards_count = seahawks_total_yards.text
