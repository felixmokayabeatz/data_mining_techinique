import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Dummy dataset (replace with real data)
data = {
    "Age": [25, 30, 35, 40, 45],
    "Salary": [40000, 50000, 60000, 70000, 80000],
    "Buys_Insurance": [0, 0, 1, 1, 1]  # 1 = Yes, 0 = No
}
df = pd.DataFrame(data)

# Split data into train & test
X = df[["Age", "Salary"]]
y = df["Buys_Insurance"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Check accuracy
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred)}")

# Function to predict
def predict_insurance(age, salary):
    return model.predict([[age, salary]])[0]
