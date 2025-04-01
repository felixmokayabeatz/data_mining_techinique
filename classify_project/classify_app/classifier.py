import pandas as pd
import numpy as np
import joblib  
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

def predict_insurance(age: int, salary: int):
    """Make a prediction using the saved model.
    
    Args:
        age: Age of the person
        salary: Annual salary of the person
        
    Returns:
        1 if the person is predicted to buy insurance, 0 otherwise
    """
    loaded_model = joblib.load("insurance_model.pkl")
    return loaded_model.predict([[age, salary]])[0]


if __name__ == "__main__":
    
    example_age = 35
    example_salary = 75000
    prediction = predict_insurance(example_age, example_salary)
    print(f"\nWill a {example_age}-year-old with ${example_salary} salary buy insurance? {'Yes' if prediction == 1 else 'No'}")