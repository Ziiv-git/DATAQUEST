Titanic: Machine Learning from Disaster.


The goal of the competition is to build machine learning models that can predict if a passenger survives from their attributes.

The data for the passengers is contained in two files:
train.csv: Contains data on 712 passengers
test.csv: Contains data on 418 passengers

Each row in both data sets represents a passenger on the Titanic, and some information about them.
We'll be working with the train.csv file, because the Survived column, which describes if a given passenger survived the crash,
is preserved in the file. The column was removed in test.csv, to encourage competitors to practice making predictions using the data.

Here are descriptions for each of the columns in train.csv:

PassengerId -- A numerical id assigned to each passenger.
Survived -- Whether the passenger survived (1), or didn't (0).
Pclass -- The class the passenger was in.
Name -- the name of the passenger.
Sex -- The gender of the passenger -- male or female.
Age -- The age of the passenger. Fractional.
SibSp -- The number of siblings and spouses the passenger had on board.
Parch -- The number of parents and children the passenger had on board.
Ticket -- The ticket number of the passenger.
Fare -- How much the passenger paid for the ticket.
Cabin -- Which cabin the passenger was in.
Embarked -- Where the passenger boarded the Titanic.
Here's what the first few rows look like:

PassengerId	Survived	Pclass	Name	                   Sex	    Age	    SibSp	Parch	Ticket	     Fare	Cabin	Embarked
1	          0	          3	    Braund, Mr. Owen Harris	   male	    22.0	1    	0	    A/5          21171	7.2500		S
2	          1	          1	    Cumings, Mrs. John Bradley (Florence Briggs Thayer)	female	38.0	1	0	PC 17599	71.2833	C85	C
3	          1	          3	    Heikkinen, Miss. Laina	   female	26.0	0	0	STON/O2. 3101282	7.9250		S


Kernel density plots are especially helpful when we're comparing distributions
To generate just the kernel density plot
sns.kdeplot(titanic['Age'])
plt.show




import pandas as pd
titanic = pd.read_csv('train.csv')
cols = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp','Parch','Fare','Embarked']
titanic = titanic[cols].dropna()
titanic.info()

import seaborn as sns
import matplotlib.pyplot as plt

sns.kdeplot(titanic['Age'], shade=True)
plt.xlabel("Age")
plt.show()


# Condition on unique values of the "Survived" column.
g = sns.FacetGrid(titanic, col="Survived", size=6)
# For each subset of values, generate a kernel density plot of the "Age" columns.
g.map(sns.kdeplot, "Age", shade=True)

g = sns.FacetGrid(titanic, col="Survived", size=6)
g.map(plt.hist, "Age")

g = sns.FacetGrid(titanic, col="Pclass", size=6)
g.map(sns.kdeplot, "Age", shade = True)
sns.despine(left = True, bottom =True)
plt.show()



We can use two conditions to generate a grid of plots, each containing a subset of the data with a unique combination of
each condition. When creating a FacetGrid, we use the row parameter to specify the column in the dataframe we want used to
subset across the rows in the grid.
g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()


g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue = "Sex", size = 3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()


g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue = "Sex", size = 3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
# g.set_axis_labels("Total bill", "Tip")
g.add_legend()
plt.show()
