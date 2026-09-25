import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

# 1. Defined data (Fixed: Standardised mismatched quotes for 'Yes')
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal'],
    'Windy': ['False', 'True', 'False', 'False', 'False', 'True', 'True'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
}

# 2. Fixed Order: Initialize the DataFrame BEFORE looping through its columns
df = pd.DataFrame(data)

# 3. Encoded categorical strings to numbers

le_features = LabelEncoder()
for col in ['Outlook', 'Temperature', 'Humidity', 'Windy']:
    df[col] = le_features.fit_transform(df[col])

le_target = LabelEncoder()
df['Play'] = le_target.fit_transform(df['Play'])

# 4. Feature and Target Split (Fixed: Mismatched quotes and trailing square brackets)
X = df[['Outlook', 'Temperature', 'Humidity', 'Windy']]
y = df['Play']

# 5. Model Initialization & Training (Fixed: Hidden Cyrillic 'у' variable typo)
model = GaussianNB()
model.fit(X, y)

# 6. Test Data Construction (Fixed: Corrected parenthetical nesting layout)
test = pd.DataFrame(
    [[2, 0, 0, 1]], 
    columns=['Outlook', 'Temperature', 'Humidity', 'Windy']
)

# 7. Predict and Decode Output
prediction = model.predict(test)
predicted_label = le_target.inverse_transform(prediction)[0]

if predicted_label == "Yes":
    print("Prediction: Yes, we can play")
else:
    print("Prediction: No, we cannot play")
