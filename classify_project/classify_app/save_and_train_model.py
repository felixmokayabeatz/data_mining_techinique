import pandas as pd
import joblib  
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os
from .classifier import predict_insurance

def train_and_save_model():
    """Generate data, train model, and save to disk. Only run this function once."""
    excel_file = "insurance_data.xlsx"
    model_file = "insurance_model.pkl"
    
    
    if not os.path.exists(excel_file):
        print("No data found")
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
    
    
    joblib.dump(model, model_file)
    print(f"Model saved as {model_file}")
    
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")
    
    return accuracy



train_and_save_model()


example_age = 35
example_salary = 75000
prediction = predict_insurance(example_age, example_salary)
print(f"\nWill a {example_age}-year-old with ${example_salary} salary buy insurance? {'Yes' if prediction == 1 else 'No'}")