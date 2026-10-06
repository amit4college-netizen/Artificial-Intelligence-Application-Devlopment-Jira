from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# Load MNIST-like digits dataset
digits = load_digits()
X = digits.data
y = digits.target
# Binary classification
# True if digit is 5, otherwise False
y = (y == 5)
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.3,
random_state=1
)
#Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
#Accuracу
print("Training Accuracy:", model.score(X_train,y_train)*100)
print("Testing Accuracy:", model.score(X_test,y_test)*100)
# Predictfirst test sample
prediction = model.predict([X_test[0]])
if prediction[0]:
    print("Digit is 5")
else:
    print("Digit is not 5")