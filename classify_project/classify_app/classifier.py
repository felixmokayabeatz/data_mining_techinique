import pandas as pd
import joblib  # For saving and loading the model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Dummy dataset (You remember to use/replace with real data)
data = {
    "Age": [25, 30, 35, 40, 45],
    "Salary": [40000, 50000, 60000, 70000, 80000],
    "Buys_Insurance": [0, 0, 1, 1, 1]  # 1 = Yes, 0 = No
}
df = pd.DataFrame(data)

X = df[["Age", "Salary"]]
y = df["Buys_Insurance"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "insurance_model.pkl")
print("Model saved as insurance_model.pkl")

y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred)}")

def predict_insurance(age: int, salary: int):
    loaded_model = joblib.load("insurance_model.pkl")
    return loaded_model.predict([[age, salary]])[0]
