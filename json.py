world_cup_str = """
[
    {
        "team_1": "France",
        "team_2": "Croatia",
        "game_type": "Final",
        "score" : [4, 2]
    },
    {
        "team_1": "Belgium",
        "team_2": "England",
        "game_type": "3rd/4th Playoff",
        "score" : [2, 0]
    }
]
"""
import json
world_cup_obj= json.loads(world_cup_str)
print(world_cup_obj)

import json
file= open('hn_2014.json')
hn= json.load(file)
print(type(hn))

# The function will use the json.dumps() function ("dump string") which does the opposite of the json.loads()
# function — it takes a JSON object and returns a string version of it. The json.dumps() function accepts arguments that can
# specify formatting for the string, which we'll use to make things easier to read:
LOOP VERSION

hn_clean = []

for d in hn:
    new_d = del_key(d, 'createdAtI')
    hn_clean.append(new_d)
hn_clean= [del_key(d,'createdAtI') for d in hn]

urls = [d['url'] for d in hn_clean]
thousand_points = [d for d in hn_clean if d['points'] > 1000]
num_thousand_points = len(thousand_points)

def get_age(json_dict):
    return json_dict['age']

youngest = min(json_obj, key=get_age)
jprint(youngest)

# Create a "key function" that accepts a single dictionary and returns the value from the numComments key.
def key_function(json_dict):
    return json_dict['numComments']
# Use the max() function with the "key function" you just created to find the value from the hn_clean list with the most comments:
# Assign the result to the variable most_comments.
most_comments= max(hn_clean, key=key_function)
jprint(most_comments)

# def multiply(a, b):
#    return a * b
multiply = lambda a, b : a * b

hn_sorted_points= sorted(hn_clean, key=lambda d: d['points'], reverse=True)

top_5_titles= [post['title'] for post in hn_sorted_points[:5]]

json_df = pd.DataFrame(json_obj)
print(json_df)
import pandas as pd
hn_df= pd.DataFrame(hn_clean)


tags = hn_df['tags']
# print(tags.dtype)
tag_types = tags.apply(type)
type_counts= tag_types.value_counts(dropna=False)
# print(type_counts)
tags_types= tags.apply(len)
type_lengths= tags_types.value_counts(dropna=False)

tags = hn_df['tags']
tags_types= tags.apply(len)==4
four_tags= tags[tags_types]

cleaned_tags= tags.apply(lambda l: l[-1] if len(l)==4 else None)
hn_df['tags'] = cleaned_tags
