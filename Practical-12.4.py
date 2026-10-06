from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

#Load Dataset
iris = load_iris()

X=iris.data
y=iris.target

#create Classification model
model = KNeighborsClassifier()

#Apply 5 cross fold selection
scores = cross_val_score(model,X,y,cv=5)

print("Accuracy score for each folds : ")
print(scores)

print("Average Accuracy:", round(scores.mean()*100,2),"%")