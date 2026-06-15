# Health Prediction Application

## Overview

The Health Prediction Application is a web-based healthcare management system developed using Python, Streamlit, SQLite, and Machine Learning. The application allows users to manage patient records and predict potential health risks based on blood test parameters such as Glucose, Haemoglobin, and Cholesterol levels.

A Random Forest Machine Learning model is used to classify patient health risk and generate prediction remarks along with a confidence score.

---

## Features

### Patient Management (CRUD Operations)

* Create Patient Records
* View Patient Records
* Update Patient Records
* Delete Patient Records

### Health Risk Prediction

* Predict health risk using a Random Forest Classifier
* Generate AI/ML-based health remarks
* Display prediction confidence score

### Data Validation

* Email address validation
* Date of Birth future-date validation
* Numeric validation for blood test values

### Data Storage

* Persistent storage using SQLite database

---

## Technologies Used

* Python
* Streamlit
* SQLite
* Pandas
* NumPy
* Scikit-learn (Random Forest Classifier)

---

## Machine Learning Model

The application uses a Random Forest Classifier trained on sample healthcare data containing:

* Glucose
* Haemoglobin
* Cholesterol

The model predicts one of the following risk categories:

* Low Health Risk
* Possible Diabetes Risk
* Possible Cardiovascular Risk

The prediction result is automatically stored in the Remarks field of the patient record.

---

## Database Schema

### Patients Table

| Column      | Type                  |
| ----------- | --------------------- |
| ID          | Integer (Primary Key) |
| Name        | Text                  |
| Email       | Text                  |
| DOB         | Text                  |
| Glucose     | Real                  |
| Haemoglobin | Real                  |
| Cholesterol | Real                  |
| Remarks     | Text                  |

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Application

```bash
streamlit run app.py
```

---

## Project Structure

```text
health-prediction-app/
│
├── app.py
├── patients.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Sample Workflow

1. Enter patient details.
2. Click Predict.
3. Machine Learning model predicts health risk.
4. Prediction and confidence score are displayed.
5. Patient record is saved to the SQLite database.
6. Users can view, update, or delete records.

---

## Author

Priyanka Ratkal
