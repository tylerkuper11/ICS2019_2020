import pandas
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier

data=pandas.read_csv("ow.csv",header=None)
print(data)

graph = sns.pairplot( data=data,vars=(0,1,2,3), hue=4 )
plt.show(graph)

data=np.array(data)

X=data[:,0:4] 
y=data[:,4]
print(X.shape)
print(y.shape)


X,y=shuffle(X,y,random_state=0)

trainX=X[:61]
trainy=y[:61]
testX=X[61:]
testy=y[61:]


clf = MLPClassifier(activation='identity', alpha=0.0001, batch_size='auto',
              beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08,
              hidden_layer_sizes=[10], learning_rate='constant',
              learning_rate_init=0.001, max_iter=10000, momentum=0.9,
              n_iter_no_change=10, nesterovs_momentum=True, power_t=0.5,
              random_state=0, shuffle=True, solver='adam', tol=0.0001,
              validation_fraction=0.1, verbose=False, warm_start=False)
clf.fit(trainX, trainy)            

####PREDICTIONS####

# ~ trainScore=clf.score(trainX,trainy)
# ~ testScore=clf.score(testX,testy)
# ~ print("%d,%f,%f"%(trainScore,testScore))
	
# ~ print(clf.coefs_)
# ~ prediction=clf.predict(testX)

# ~ print(prediction)

####PRINT ACCURACY####
print(clf.score(trainX,trainy))
print(clf.score(testX,testy))

####CROSS-VALIDATION####
from sklearn.model_selection import cross_validate
cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)



####GRID SEARCH####
# ~ from sklearn.model_selection import GridSearchCV
# ~ parameters = {'hidden_layer_sizes':([3], [10], [3,3], [3,3,3]), 'activation':('identity', 'logistic')}
# ~ parameters = {'hidden_layer_sizes':([1],[2],[3],[4],[5],[6],[7],[8],[9],[10]), 'activation':('identity', 'logistic')}
# ~ gs = GridSearchCV(clf,parameters)
# ~ gs.fit(X,y)
# ~ print(gs.best_estimator_)
# ~ print(gs.cv_results_)


