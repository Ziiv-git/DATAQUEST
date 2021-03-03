from sklearn.tree import DecisionTreeClassifier

# A list of columns to train with
# We've already converted all columns to numeric
columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

# Instantiate the classifier
# Set random_state to 1 to make sure the results are consistent
clf = DecisionTreeClassifier(random_state=1)
clf.fit(income[columns], income['high_income'])

import numpy
import math
# Set a random seed so the shuffle is the same every time
numpy.random.seed(1)
# Shuffle the rows
# This permutes the index randomly using numpy.random.permutation
# Then, it reindexes the dataframe with the result
# The net effect is to put the rows into random order
income = income.reindex(numpy.random.permutation(income.index))
train_max_row = math.floor(income.shape[0] * .8)
train = income.iloc[:train_max_row]
test = income.iloc[train_max_row:]

from sklearn.metrics import roc_auc_score

clf = DecisionTreeClassifier(random_state=1)
clf.fit(train[columns], train["high_income"])
predictions = clf.predict(test[columns])
error = roc_auc_score(test['high_income'], predictions)
print(error)

predictions = clf.predict(train[columns])
print(roc_auc_score(train['high_income'], predictions))


# Decision trees model from the last screen
clf = DecisionTreeClassifier(random_state=1)
# pruning the tree
clf = DecisionTreeClassifier(min_samples_split=13, random_state=1)
clf.fit(train[columns], train['high_income'])
predictions = clf.predict(test[columns])
test_auc = roc_auc_score(test['high_income'], predictions)
train_predictions = clf.predict(train[columns])
train_auc = roc_auc_score(train['high_income'], train_predictions)
print(test_auc)
print(train_auc)



# The first decision trees model we trained and tested
clf = DecisionTreeClassifier(random_state=1, min_samples_split=13, max_depth=7)
clf.fit(train[columns], train["high_income"])
predictions = clf.predict(test[columns])
test_auc = roc_auc_score(test["high_income"], predictions)

train_predictions = clf.predict(train[columns])
train_auc = roc_auc_score(train["high_income"], train_predictions)

print(test_auc)
print(train_auc)
#
# High bias can cause underfitting -- if a model is consistently failing to predict the correct value, it may be that it's too simple to model the data faithfully.
#
# High variance can cause overfitting. If a model varies its predictions significantly based on small changes in the input data, then it's likely fitting itself to quirks in the training data, rather than making a generalizable model.
# Decision trees typically suffer from high variance. The entire structure of a decision tree can change if we make a minor alteration to its training data. By restricting the depth of the tree, we increase the bias and decrease the variance. If we restrict the depth too much, we increase bias to the point where it will underfit.
# Pruning involves building a full tree, and then removing the leaves that don't add to prediction accuracy. Pruning prevents a model from becoming overly complex. It can result in a simpler model that has higher accuracy on the testing set.
# Let's go over the main advantages and disadvantages of using decision trees. The main advantages of using decision trees is that they're:
#
# Easy to interpret
# Relatively fast to fit and make predictions
# Able to handle multiple types of data
# Able to pick up nonlinearities in data, and usually fairly accurate
# The main disadvantage of using decision trees is their tendency to overfit.
#
# Decision trees are a good choice for tasks where it's important to be able to interpret and convey why the algorithm is doing what it's doing.
#
# The most powerful way to reduce decision tree overfitting is to create ensembles of trees. The random forest algorithm is a popular choice for doing this. In cases where prediction accuracy is the most important consideration, random forests usually perform better.
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2)
clf.fit(train[columns], train["high_income"])

clf2 = DecisionTreeClassifier(random_state=1, max_depth=5)
clf2.fit(train[columns], train["high_income"])
predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))

predictions = clf2.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))


predictions = clf.predict_proba(test[columns])[:,1]
predictions2 = clf2.predict_proba(test[columns])[:,1]
combined = (predictions + predictions2) / 2
rounded = numpy.round(combined)

print(roc_auc_score(test["high_income"], rounded))


# We'll build 10 trees
tree_count = 10

# Each "bag" will have 60% of the number of original rows
bag_proportion = .6

predictions = []
for i in range(tree_count):
    # We select 60% of the rows from train, sampling with replacement
    # We set a random state to ensure we'll be able to replicate our results
    # We set it to i instead of a fixed value so we don't get the same sample in every loop
    # That would make all of our trees the same
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)

    # Fit a decision tree model to the "bag"
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2)
    clf.fit(bag[columns], bag["high_income"])

    # Using the model, make predictions on the test data
    predictions.append(clf.predict_proba(test[columns])[:,1])
combined = numpy.sum(predictions, axis=0) / 10
rounded = numpy.round(combined)

print(roc_auc_score(test["high_income"], rounded))


# Create the data set that we used two missions ago
data = pandas.DataFrame([
    [0,4,20,0],
    [0,4,60,2],
    [0,5,40,1],
    [1,4,25,1],
    [1,5,35,2],
    [1,5,55,1]
    ])
data.columns = ["high_income", "employment", "age", "marital_status"]

# Set a random seed to make the results reproducible
numpy.random.seed(1)

# The dictionary to store our tree
tree = {}
nodes = []


def find_best_column(data, target_name, columns):
    information_gains = []

    # Select two columns randomly
    cols = numpy.random.choice(columns, 2)

    for col in cols:
        information_gain = calc_information_gain(data, col, "high_income")
        information_gains.append(information_gain)

    highest_gain_index = information_gains.index(max(information_gains))

    # Get the highest gain by indexing "cols"
    highest_gain = cols[highest_gain_index]

    return highest_gain

id3(data, "high_income", ["employment", "age", "marital_status"], tree)
print(tree)



# We'll build 10 trees
tree_count = 10

# Each "bag" will have 60% of the number of original rows
bag_proportion = .6

predictions = []
for i in range(tree_count):
    # We select 60% of the rows from train, sampling with replacement
    # We set a random state to ensure we'll be able to replicate our results
    # We set it to i instead of a fixed value so we don't get the same sample every time
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)

    # Fit a decision tree model to the "bag"
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2, splitter="random", max_features="auto")
    clf.fit(bag[columns], bag["high_income"])

    # Using the model, make predictions on the test data
    predictions.append(clf.predict_proba(test[columns])[:,1])

combined = numpy.sum(predictions, axis=0) / 10
rounded = numpy.round(combined)

print(roc_auc_score(test["high_income"], rounded))





from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=5, random_state=1, min_samples_leaf=2)
clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))
# While the random forest algorithm is incredibly powerful, it isn't applicable to all tasks. The main strengths of a random forest are:
#
# Very accurate predictions - Random forests achieve near state-of-the-art performance on many machine learning tasks. Along with neural networks and gradient-boosted trees, they're typically one of the top-performing algorithms.
# Resistance to overfitting - Due to their construction, random forests are fairly resistant to overfitting. We still need to set and tweak parameters like max_depth though.
# The main weaknesses of using a random forest are:
#
# They're difficult to interpret - Because we're averaging the results of many trees, it can be hard to figure out why a random forest is making predictions the way it is.
# They take longer to create - Making two trees takes twice as long as making one, making three takes three times as long, and so on. Fortunately, we can exploit multicore processors to parallelize tree construction. Scikit allows us to do this through the n_jobs parameter on RandomForestClassifier.
