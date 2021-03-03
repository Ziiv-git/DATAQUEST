from sklearn.datasets import make_regression
import pandas as pd
data = make_regression(n_samples=100, n_features=3, random_state=1)
features = pd.DataFrame(data[0])
labels = pd.Series(data[1])

# Because the inputs from one layer of neurons feed to the next layer of the single, output neuron,
# this is known as a feedforward network. In the language of graphs, a feedforward network is a directed, acyclic graph.
features['bias'] = 1

from sklearn.linear_model import SGDRegressor

def train(features,labels):
    sgd = SGDRegressor()
    sgd.fit(features,labels)
    weights = sgd.coef_
    return weights

def feedforward(features,weights):
    predictions = np.dot(features,weights.T)
    return predictions

train_weights = train(features, labels)
linear_predictions = feedforward(features, train_weights)






from sklearn.datasets import make_classification
data = make_classification(n_samples=100, n_features=4, random_state=1)
class_features = pd.DataFrame(data[0])
class_labels = pd.Series(data[1])


# neural networks need:
# a network structure (how are the nodes connected? which direction does the data and computation flow?)
# a feedforward function (how are the node weights and observation values combined?)
# an activation function (what transformations on the data are performed?)
# a model fitting function (how is the model fit?)

from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_classification

class_data = make_classification(n_samples=100, n_features=4, random_state=1)
class_features = pd.DataFrame(class_data[0])
class_labels = pd.Series(class_data[1])

class_features["bias"] = 1

def log_train(class_features, class_labels):
    sg = SGDClassifier()
    sg.fit(class_features, class_labels)
    return sg.coef_

def sigmoid(linear_combination):
    return 1/(1+np.exp(-linear_combination))

def log_feedforward(class_features, log_train_weights):
    linear_combination = np.dot(class_features, log_train_weights.T)
    log_predictions = sigmoid(linear_combination)
    log_predictions[log_predictions >= 0.5] = 1
    log_predictions[log_predictions < 0.5] = 0
    return log_predictions

log_train_weights = log_train(class_features, class_labels)
log_predictions = log_feedforward(class_features, log_train_weights)



from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_moons
import pandas as pd
import matplotlib.pyplot as plt
data = make_moons(random_state=3, noise=0.04)
features = pd.DataFrame(data[0])
labels = pd.Series(data[1])
fig  = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(features[0], features[1], labels)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')






from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
np.random.seed(8)

data = make_moons(100, random_state=3, noise=0.04)
features = pd.DataFrame(data[0])
labels = pd.Series(data[1])
features["bias"] = 1

shuffled_index = np.random.permutation(features.index)
shuffled_data = features.loc[shuffled_index]
shuffled_labels = labels.loc[shuffled_index]
mid_length = int(len(shuffled_data)/2)
train_features = shuffled_data.iloc[0:mid_length]
test_features = shuffled_data.iloc[mid_length:len(shuffled_data)]
train_labels = shuffled_labels.iloc[0:mid_length]
test_labels = shuffled_labels.iloc[mid_length: len(labels)]
mlp = MLPClassifier(hidden_layer_sizes=(1,), activation='logistic')
mlp.fit(train_features, train_labels)
nn_predictions = mlp.predict(test_features)

lr = LogisticRegression()
lr.fit(train_features, train_labels)
log_predictions = lr.predict(test_features)

nn_accuracy = accuracy_score(test_labels, nn_predictions)
log_accuracy = accuracy_score(test_labels, log_predictions)

print("Logistic Regression Model Accuracy: ", log_accuracy)
print("Single Neuron Single Layer NN Model Accuracy: ", nn_accuracy)


neurons = [1,5,10,15,20,25]
accuracies = []
for value in neurons:
    mlp = MLPClassifier(hidden_layer_sizes=(value,), activation='logistic')
    mlp.fit(train_features, train_labels)
    predictions = mlp.predict(test_features)
    acc = accuracy_score(test_labels, predictions)
    accuracies.append(acc)
print(accuracies)

neurons = [1,5,10,15,20,25]
nn_accuracies = []
for n in neurons:
    mlp = MLPClassifier(hidden_layer_sizes=(n, n), activation='relu', max_iter = 1000)
    mlp.fit(train_features, train_labels)
    predictions = mlp.predict(test_features)
    acc = accuracy_score(test_labels, predictions)
    nn_accuracies.append(acc)
print(nn_accuracies)
