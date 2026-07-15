# 🎓 Student Marks Predictor

A simple Machine Learning web app built with **Flask** that predicts a student's marks based on their study hours, using **Linear Regression**.

![Predict Marks App](https://img.shields.io/badge/Machine%20Learning-Flask%20App-blue)



## 📌 Overview

This project takes a dataset of students' study hours and marks, trains a Linear Regression model on it, and serves predictions through a clean, interactive web interface. Enter the number of hours studied, and the app instantly predicts the expected marks.

---

## ✨ Features

- 🧹 Handles missing data using median imputation
- 🤖 Trains a Linear Regression model with scikit-learn
- 🌐 Flask backend to serve real-time predictions
- 🎨 Clean, responsive UI with custom CSS styling
- ⚡ Instant predictions on form submission

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Handling | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Backend | Flask |
| Frontend | HTML, CSS |

---

## 📊 Dataset

The dataset (`student_info.csv`) contains 200 records with two columns:

| Column | Description |
|---|---|
| `hours` | Number of hours a student studied |
| `marks` | Marks scored by the student |

Some `hours` values were missing and were filled using **median imputation** (`SimpleImputer`) before training.

---

## ⚙️ How It Works

1. **Data Preprocessing** — Missing `hours` values are filled with the median using `SimpleImputer`.
2. **Train-Test Split** — Data is split into 80% training and 20% testing sets.
3. **Model Training** — A `LinearRegression` model is trained on the training data to learn the relationship between hours studied and marks scored.
4. **Prediction** — When a user submits hours studied via the web form, the Flask backend passes it to the trained model and returns the predicted marks.

> Note: Predicted marks may not exactly match the values in the dataset for the same hours — this is expected, since the model learns a general trend rather than memorizing individual data points (which helps avoid overfitting).

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/pratikshapawar1525/Student-Marks-Predictor
cd student-marks-predictor

# Install dependencies
pip install flask pandas numpy scikit-learn seaborn matplotlib
```

### Run the App


python main.py


Then open your browser and go to:

http://127.0.0.1:5000/



## 📁 Project Structure

student-marks-predictor/
│
├── app.py                 # Flask application & ML model training
├── student_info.csv       # Dataset
├── templates/
│   └── index.html         # Frontend HTML
├── static/
│   └── style.css           # Styling
└── README.md



## 📸 Preview

## App Screenshot

![Student Marks Predictor](prediction%20img.png)




## 🧠 What I Learned

This project helped me understand the complete Machine Learning workflow — from data cleaning and model training to building and deploying a functional web application using Flask.

---

## 📄 License

This project is open source and available for learning purposes.

---

## 🙌 Connect

If you found this project helpful or have suggestions, feel free to connect or open an issue!
# Student-Marks-Predictor
A simple Machine Learning web app built with Flask that predicts student marks based on study hours using Linear Regression.
