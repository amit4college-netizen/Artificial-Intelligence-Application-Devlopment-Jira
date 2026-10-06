from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# Load dataset
iris = load_iris()
X= iris.data
y = iris.target
#Split dataset
X_train, X_test,y_train, y_test = train_test_split( X,
y,
test_size=0.3,
random_state=1
)
# Create kNN model
model = KNeighborsClassifier(n_neighbors=3)
#Train model
model.fit(X_train, y_train)
# Display accuracy
print("Training Accuracy:", model.score(X_train, y_train) *100)
print("Testing Accuracy:", model.score(X_test, y_test)*100)
#Prediction
prediction = model.predict([X_test[0]])
print("Predicted Class:", prediction[0])
