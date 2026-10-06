import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# a)Load datasets using Pandas
data=pd.read_csv("Csv_files/student.csv")

print("dataset: ")
print(data)

le = LabelEncoder()

data["Result"] = le.fit_transform(data["Result"])

# Input and Output
X = data[["Hours","Attendance"]]
y = data["Result"]

# b) Preprocessing (Scaling)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# c) Split data
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,random_state=1
)

# d) Train Classifier
model = KNeighborsClassifier()

model.fit(X_train,y_train)

# e) Training and Testing Accuracy

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("\nTraining Accuracy:", accuracy_score(y_train,train_pred)*100)
print("\nTesting Accuracy:", accuracy_score(y_test,test_pred)*100)
