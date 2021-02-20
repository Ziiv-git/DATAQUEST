headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"} #reddit Authorization token
# need to use the string bearer instead of the string token. That's because we're using OAuth this time
parameters = {'t':'day'}
response = requests.get('https://oauth.reddit.com/r/python/top', headers=headers, params=parameters) #top posts of python subreddit in past day
python_top = response.json()



python_top_articles = python_top['data']['children'] #Extract the list containing all of the posts from the dictionary
# finding the post with most upvotes
most_upvoted = ''
most_upvotes = 0
for article in python_top_articles:
    ar = article['data']
    if ar['ups'] >= most_upvotes:
        most_upvoted = ar['id']
        most_upvotes = ar['ups']


# getting the comments from the most upvoted article in subreddit of python
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.get('https://oauth.reddit.com/r/python/comments/4b7w9u', headers=headers)
comments = response.json()


comments_list = comments[1]['data']['children'] #Extract the list containing all of the comments from the list
# finding the commentt with most upvotes
most_upvoted_comment = ''
most_upvotes = 0
for comment in comments_list:
    cm = comment['data']
    if cm['ups'] >= most_upvotes:
        most_upvoted_comment = cm['id']
        most_upvotes = cm['ups']



payload = {'dir':1, 'id':'d16y4ry'} #upvoting the most commented comment
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.post('https://oauth.reddit.com/api/vote', headers=headers, json=payload)
status = response.status_code
