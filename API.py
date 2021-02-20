# An API is a set of methods and tools that allows different applications to interact with each other. Programmers use APIs to query and retrieve data
# dynamically (which they can then integrate into their own apps). A client can retrieve information quickly and easily with an API.
#
# Reddit, Spotify, Twitter, Facebook, and many other companies provide free APIs that make the information they store on their servers accessible.
# Other companies charge for access to their APIs.
#
# In this mission, we'll query a basic API to retrieve data about the International Space Station (ISS). Using an API will save us the time and effort of
# doing all the computation ourselves.

# Make a get request to get the latest position of the ISS from the OpenNotify API.
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code #The server will send a status code indicating the success or failure of your request.

200 — Everything went okay, and the server returned a result (if any).
301 — The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or when an endpoint's name has changed.
401 — The server thinks you're not authenticated. This happens when you don't send the right credentials to access an API (we'll talk about this in a later mission).
400 — The server thinks you made a bad request. This can happen when you don't send the information the API requires to process your request (among other things).
403 — The resource you're trying to access is forbidden, and you don't have the right permissions to see it.
404 — The server didn't find the resource you tried to access.


# Set up the parameters we want to pass to the API.
parameters = {"lat": 37.78, "lon": -122.41}
# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# Print the content of the response (the data the server returned)
content = response.content


# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
# print(type(best_food_chains)) -- list
# Import the JSON library.
import json
# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
# print(type(best_food_chains_string))

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
# print(type(fast_food_franchise_string))

fast_food_franchise_2 = json.loads(fast_food_franchise_string)
# print(type(fast_food_franchise_2))







# Make the same request we did two screens ago.
parameters = {"lat": 37.78, "lon": -122.41} #San Francisco
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a Python object.  Verify that it's a dictionary.
json_data = response.json()
# print(type(json_data))
# print(json_data)
first_pass_duration = json_data['response'][0]['duration']
# Headers is a dictionary
print(response.headers)
content_type = response.headers['content-type']
type(content_type) #string
print(content_type)


response = requests.get('http://api.open-notify.org/astros.json')
json_data = response.json()
in_space_count = json_data['number']



# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

# Make a GET request to the GitHub API with our headers.
# This API endpoint will give us details about Vik Paruchuri.
response = requests.get("https://api.github.com/users/VikParuchuri", headers=headers)

# Print the content of the response.  As you can see, this token corresponds to the account of Vik Paruchuri.
print(response.json())
response = requests.get("https://api.github.com/users/VikParuchuri/orgs", headers=headers)
orgs = response.json()



params = {"per_page": 50, "page": 2}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page2_repos = response.json()

# Create the data we'll pass into the API endpoint.  While this endpoint only requires the "name" key, there are other optional keys.
payload = {"name": "learning-about-apis"} #creating a new repo
# We need to pass in our authentication headers!
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
status = response.status_code



payload = {"description": "Learning about requests!", "name": "learning-about-apis"} #updating the existing repo using patch
response = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payload, headers=headers)
status = response.status_code


# deleting the repo
response = requests.delete("https://api.github.com/repos/VikParuchuri/learning-about-apis", headers=headers)
status = response.status_code
