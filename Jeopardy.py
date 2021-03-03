#!/usr/bin/env python
# coding: utf-8

# # Jeopardy 
# 
# is a popular TV show in the US where participants answer questions to win money. It's been running for many years, and is a major force in popular culture.

# working with a dataset of Jeopardy questions to figure out some patterns in the questions that could help you win.

# In[1]:


import pandas as pd 
jeopardy = pd.read_csv('jeopardy.csv')
jeopardy.info()


# * Show Number - the Jeopardy episode number
# * Air Date - the date the episode aired
# * Round - the round of Jeopardy
# * Category - the category of the question
# * Value - the number of dollars the correct answer is worth
# * Question - the text of the question
# * Answer - the text of the answer

# In[2]:


jeopardy.head()


# In[3]:


jeopardy.columns


# In[4]:


#replacing the space
jeopardy.columns = ['Show Number', 'Air Date', 'Round', 'Category', 'Value', 'Question', 'Answer']


# In[5]:


jeopardy.columns


# ## normalizing
# 
# idea is to ensure to put words in lowercase and remove punctuation so Don't and don't aren't considered to be different words when we compare them.

# In[6]:


import re 

def normalise_text(string):
    string = string.lower() #string to lower case
    pattern = r'[^A-za-z0-9\s]' #removing the punctuation marks
    string = re.sub(pattern, '', string) 
    string = re.sub('s\+', ' ', string) #removes newlines and tabs..
    return string


# In[7]:


jeopardy['Clean_Question'] = jeopardy['Question'].apply(normalise_text)
jeopardy['Clean_Answer'] = jeopardy['Answer'].apply(normalise_text)


# In[8]:


def normalise_values(string):
    pattern = r'[^A-za-z0-9\s]'
    string = re.sub(pattern,'',string)
    try:
        string = int(string)
    except Exception:
        string = 0
    return string


# In[9]:


jeopardy['Clean_Value'] = jeopardy['Value'].apply(normalise_values)


# In[10]:


jeopardy.head()


# In[11]:


jeopardy['Air Date'] = pd.to_datetime(jeopardy['Air Date'])


# In[12]:


jeopardy.dtypes


# In order to figure out whether to study past questions, study general knowledge, or not study it all, it would be helpful to figure out two things:
# 
# * How often the answer can be used for a question.
# * How often questions are repeated.
# 
# can answer the first question by seeing how many times words in the answer also occur in the question. 

# In[13]:


#function that takes in the row from the dataset to count the number of matches of word that
#occur in answer and question 
def count_matches(row):
    split_answer = row['Clean_Answer'].split(' ') #splitting by spaces
    split_question = row['Clean_Question'].split(' ')
    match_count = 0
    #removing the from the split_answer as it is very common 
    if 'the' in split_answer:
        split_answer.remove('the')
    if len(split_answer) == 0:
        return 0 #tp prevent division by 0 later
    for word in split_answer: #counting number of matches
        if word in split_question:
            match_count += 1
    return match_count / len(split_answer)
            


# In[14]:


jeopardy['Ans_in_Que'] = jeopardy.apply(count_matches, axis  = 1)


# In[16]:


jeopardy['Ans_in_Que'].mean()


# ## Recycled questions
# 
# On average, the answer only makes up for about 6% of the question. This isn't a huge number, and means that we probably can't just hope that hearing a question will enable us to figure out the answer. We'll probably have to study.

# ## investigate 
# 
# how often new questions are repeats of older ones. We can't completely answer this, because we only have about 10% of the full Jeopardy question dataset, but we can investigate it at least.

# In[24]:


question_overlap = []
terms_used = set()

jeopardy = jeopardy.sort_values("Air Date") #sorting based on airing date of episodes

for i, row in jeopardy.iterrows():
        split_question = row["Clean_Question"].split(" ")
        split_question = [q for q in split_question if len(q) > 5]#keeping words greater than length of 5 to remove the most common words like 'the', 'than'.......
        match_count = 0
        for word in split_question:
            if word in terms_used:
                match_count += 1
        for word in split_question:
            terms_used.add(word)  #capturing the unique words using set
        if len(split_question) > 0:
            match_count /= len(split_question)
        question_overlap.append(match_count)


# In[25]:


jeopardy["Question_overlap"] = question_overlap

jeopardy["Question_overlap"].mean()


# ## Low value vs high value questions
# 
# There is about 70% overlap between terms in new questions and terms in old questions. This only looks at a small set of questions, and it doesn't look at phrases, it looks at single terms. This makes it relatively insignificant, but it does mean that it's worth looking more into the recycling of questions.

# In[26]:


#finding questions who's value is more than 800
def determine_value(row):
    if row['Clean_Value'] > 800:
        value = 1
    else:
        value = 0
    return value


# In[27]:


jeopardy['High_Value'] = jeopardy.apply(determine_value, axis=1)


# In[28]:


jeopardy.head()


# In[29]:


def count_usage(word):
    low_count = 0
    high_count = 0
    for i, row in jeopardy.iterrows():
        split_question = row['Clean_Question'].split(' ')
        if word in split_question:
            if row['High_Value'] == 1:
                high_count += 1
            else:
                low_count += 1
    return high_count, low_count


# In[31]:


from random import choice

terms_used_list = list(terms_used)
comparison_terms = [choice(terms_used_list) for _ in range(10)] #choosing random 10 words 

observed_expected = []

for word in comparison_terms:
    observed_expected.append(count_usage(word))
    
observed_expected


# In[34]:


high_value_count = jeopardy[jeopardy['High_Value'] == 1].shape[0]
high_value_count


# In[35]:


low_value_count = jeopardy[jeopardy['High_Value'] == 0].shape[0]
low_value_count


# In[36]:


from scipy.stats import chisquare 
import numpy as np 

chi_squared = []

for obs in observed_expected:
    total = sum(obs) #summing both high and low count
    total_prep = total / jeopardy.shape[0] #dividing by number of rows 
    high_value_exp = total_prep * high_value_count #
    low_value_exp = total_prep * low_value_count
    
    observed = np.array([obs[0], obs[1]])
    expected = np.array([high_value_count, low_value_count])
    chi_squared.append(chisquare(observed, expected))


# In[37]:


chi_squared


# # Chi-squared results
# 
# None of the terms had a significant difference in usage between high value and low value rows. Additionally, the frequencies were all lower than 5, so the chi-squared test isn't as valid. It would be better to run this test with only terms that have higher frequencies.

# In[ ]:




