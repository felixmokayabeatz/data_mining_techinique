import pandas as pd
import numpy as np
import joblib  
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os


def generate_insurance_dataset():
    np.random.seed(42)  
    
    
    ages = np.random.normal(45, 12, 1000).astype(int)
    ages = np.clip(ages, 18, 85)  
    
    
    salaries = np.random.lognormal(mean=11, sigma=0.4, size=1000)
    salaries = np.round(salaries, -2).astype(int)  
    
    
    probabilities = 0.3 + 0.4 * (ages > 40).astype(float) + 0.3 * (salaries > 60000).astype(float)
    probabilities = np.clip(probabilities, 0.1, 0.9)  
    buys_insurance = (np.random.random(1000) < probabilities).astype(int)
    
    
    data = {
        "Age": ages,
        "Salary": salaries,
        "Buys_Insurance": buys_insurance
    }
    
    return pd.DataFrame(data)


excel_file = "insurance_data.xlsx"

if not os.path.exists(excel_file):
    print("Generating new dataset...")
    df = generate_insurance_dataset()
    
    df.to_excel(excel_file, index=False)
    print(f"Dataset saved to {excel_file}")
else:
    print(f"Loading existing dataset from {excel_file}")


df = pd.read_excel(excel_file)

print(f"Dataset shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())
print("\nClass distribution:")
print(df["Buys_Insurance"].value_counts())


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


example_age = 35
example_salary = 75000
prediction = predict_insurance(example_age, example_salary)
print(f"\nWill a {example_age}-year-old with ${example_salary} salary buy insurance? {'Yes' if prediction == 1 else 'No'}")