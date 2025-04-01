# Django Classification Project - Group 10

---

## 👥 Group 10 Members

1. **Mbugua Maxwel (P101/1795G/21)**  
2. **Felix Mokaya Amwoma (P101/1823G/21)**  
3. **Samuel kariuki (p101/1725g/21)**
4. **Bithon Macharia (p101/1774g/21)**
5. **David Murichu (p101/1720g/21)**
6. **Morris Kamande (p101/1721g/21)**
7. **Victor Gabriel (kahihu P101/1715G/21)**
9. **Robert Mburu (P101/1755g/21)**
10. **Morompi Francis (p101/1779g/21)**

---

## 📌 Project Overview

This is a Django-based classification project that predicts whether a person will buy insurance based on their age and salary. The model uses a **simple machine learning classifier** to make predictions.

## 🎯 Objectives

- Develop a **machine learning-based classification model**.
- Implement a **Django web application** for user interaction.
- Use **Bootstrap styling** for a clean and user-friendly UI.
- Predict whether a user **will buy insurance or not**.

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Bootstrap
- **Machine Learning:** Scikit-learn (Logistic Regression)
- **Database:** SQLite (default Django DB)

---

## 🚀 Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/felixmokayabeatz/data_mining_techinique.git
cd data_mining_techinique
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
# For Windows:
python -m venv venv
env\Scripts\activate

# For Mac/Linux:
python3 -m venv venv
source env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Start the Django Server

```bash
python manage.py runserver
```

Then, open **<http://127.0.0.1:8000/classify/>** in your browser.

---

## 📂 Project Structure

```
    classify_project/
    │── classify_project/        # Main Django project folder
    │   │── settings.py         # Project settings
    │   │── urls.py             # Project URL configuration
    │── classify_app/           # Django app folder
    │   │── models.py          # Data model (optional if using ML only)
    │   │── views.py           # Backend logic for classification
    │   │── urls.py            # App URLs
    │   │── templates/         # Frontend templates
    │       │── classify.html  # Main UI for prediction
    │── static/                # CSS, JS, images (if needed)
    │── db.sqlite3             # SQLite database
    │── manage.py              # Django CLI
    │── requirements.txt       # Python dependencies
    │── README.md              # This file
```

---

## 📊 How It Works

1. **User Inputs Data:**
   - Age
   - Salary
2. **Backend Processes Data:**
   - Uses a trained **Logistic Regression** model.
   - Predicts whether the user will buy insurance.
3. **Displays Result:**
   - ✅ **Will Buy Insurance** (if predicted probability is high)
   - ❌ **Won't Buy Insurance** (if probability is low)

---

## 📊 Classification Technique Used

### **Logistic Regression**

- **Why Logistic Regression?**
  - Works well for binary classification (Yes/No decisions).
  - Simple, interpretable, and easy to implement.
  - Suitable for structured data like Age and Salary.

### **How the Model Works:**

1. The user **inputs Age and Salary**.
2. The system **processes the data** using the trained logistic regression model.
3. The model **calculates the probability** that the user will buy insurance.
4. The result is displayed:
   - ✅ **Will Buy Insurance** (if probability > threshold)
   - ❌ **Won't Buy Insurance** (if probability < threshold)

---

## 🏗 System Implementation

### **1️⃣ Backend (Django)**

- Handles user input and prediction processing.
- Implements the logistic regression model.

### **2️⃣ Frontend (HTML + Bootstrap)**

- Provides an easy-to-use form for data input.
- Displays classification results with a modern design.

### **3️⃣ Machine Learning Model (Scikit-learn)**

- Trained on sample insurance data.
- Predicts insurance purchasing behavior.

---

## 📌 Future Enhancements

- ✅ Train the model on a larger dataset.
- ✅ Improve UI with animations.
- ✅ Store user predictions in the database for analysis.
- ✅ Experiment with **other classification techniques** (e.g., Decision Trees, SVM).

## 📜 License

This project is open-source and available under the MIT License.

---
🚀 **Now go predict some insurance buyers!** 🎯
