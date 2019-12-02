from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
parameters = ('hidden_layer_sizes':([3], [10], [3,3], [3,3,3]), 'activation':('identity', 'logistic',
cv_results = GridSearchCV(clf,parameters)
gs.fit(X,y)
print(cv_results)
