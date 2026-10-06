import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Load dataset
data = pd.read_csv("Csv_files/student_marks.csv")
# Input and output
X = data[['Hours']]
y = data['Marks']
#Split dataset
X_train, X_test,y_train, y_test = train_test_split(
    X,y,
test_size=0.3, random_state=1
)
# Train model
model = LinearRegression()
model.fit(X_train,y_train)
#Display accuracy
print("Training Accuracy:",
round(model.score(X_train, y_train)*100,2))
print("Testing Accuracy:")
round(model.score(X_test, y_test)*100,2)
# Predict marks for 11 study hours
new_data = pd.DataFrame([[11]],columns=['Hours'])
pred = model.predict(new_data)
print("Predicted Marks for 11 hours:",round(pred[0],2))