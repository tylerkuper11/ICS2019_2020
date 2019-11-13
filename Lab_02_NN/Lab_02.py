import pandas
import sklearn
data=pandas.read_csv("iris.data",header=None)
print(data)

# 4.)
# Yes
# The Iris Setosa is easily identified because it's separated from others.
# Iris Versicolour and Iris Virginica because their data is very similar to each other.

# ~ import matplotlib.pyplot as plt
# ~ import seaborn as sns # visualization
# ~ sns.pairplot( data=data,vars=(0,1,2,3), hue=4 )
# ~ plt.show()

import numpy as np
data=np.array(data)

X=data[:,0:4] #This gets all the rows and only the first 4 columns.
y=data[:,4]
print(X.shape) #(150,4)
print(y.shape) #(150,1)

from sklearn.utils import shuffle
X,y=shuffle(X,y,random_state=0)

# 8.)
# I verified this by printing X and y's data to see if they were shuffled.
# random_state is how the shuffle initializes the random seed.
# This is useful because it uses a random seed for shuffling the data for the machine to interpret it.
# ~ print (X)
# ~ print (y)
trainX=X[:91]
trainy=y[:91]
testX=X[91:]
testy=y[91:]

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=[7], random_state=0,max_iter=10000)
clf.fit(trainX, trainy)
print(clf.coefs_)
prediction=clf.predict(testX)

#print(prediction)

print(clf.score(trainX,trainy))
print(clf.score(testX,testy))

from sklearn.model_selection import cross_validate
cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)





