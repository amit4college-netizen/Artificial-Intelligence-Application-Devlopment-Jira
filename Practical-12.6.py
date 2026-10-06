import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
#Load dataset
data = pd.read_csv("Csv_files/student_marks.csv")
#Input and output
X = data[['Hours']]
y = data['Marks']
# Split dataset
X_train, X_test, y_train,y_test = train_test_split( 
X,
y,
test_size=0.3,
random_state=1
)
# Create model
model = DecisionTreeRegressor()
#Train model
model.fit(X_train, y_train)
#Display accuracy
print("Training Accuracy:",model.score(X_train,y_train)*100)
print("Testing Accuracy:",model.score(X_test,y_test)*100)
# Prediction
new_data = pd.DataFrame([[11]],columns=['Hours']) 
prediction = model.predict(new_data)
print("Predicted Marks for 11 Hours:",prediction[0])