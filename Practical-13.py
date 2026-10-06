import pandas as pd
from sklearn.datasets import load_iris
#Load dataset
iris = load_iris()
#Convert to DataFrame
data = pd.DataFrame(
iris.data,
columns=iris.feature_names
)
data['Class'] = iris.target
print("First 5 records:")
print(data.head())
print("Class Distribution:")
print(data['Class'].value_counts())
print("Missing Values:")
print(data.isnull().sum)
print("Bias Analysis:")
if data['Class'].value_counts().min() == data['Class'].value_counts().max(): 
    print("Dataset is balanced.") 
else:
    print("Dataset is imbalanced.")