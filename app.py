import streamlit as st
import sqlite3
import pandas as pd
from datetime import date
from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([
    [90, 13, 180],
    [95, 14, 170],
    [140, 12, 250],
    [150, 11, 260],
    [130, 10, 240],
    [85, 15, 160],
    [160, 10, 280],
    [100, 13, 190]
])

y = np.array([
    0, 0, 1, 2,
    2, 0, 2, 0
])

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

conn = sqlite3.connect(
    "patients.db",
    check_same_thread=False
)

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob TEXT,
    glucose REAL,
    haemoglobin REAL,
    cholesterol REAL,
    remarks TEXT
)
""")

conn.commit()

st.title("Health Prediction Application")

st.header("Add Patient")

name = st.text_input("Full Name")

email = st.text_input("Email Address")

dob = st.date_input("Date of Birth")

glucose = st.number_input(
    "Glucose",
    min_value=0.0
)

haemoglobin = st.number_input(
    "Haemoglobin",
    min_value=0.0
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=0.0
)

if st.button("Predict"):

    # Email Validation
    if "@" not in email or "." not in email:
        st.error("Please enter a valid email address")
        st.stop()

    # DOB Validation
    if dob > date.today():
        st.error("Date of Birth cannot be a future date")
        st.stop()

    # ML Prediction
    prediction = model.predict([
        [glucose, haemoglobin, cholesterol]
    ])[0]

    if prediction == 0:
        remark = "Low Health Risk"
    elif prediction == 1:
        remark = "Possible Diabetes Risk"
    else:
        remark = "Possible Cardiovascular Risk"

    probabilities = model.predict_proba([
        [glucose, haemoglobin, cholesterol]
    ])[0]

    confidence = round(
        max(probabilities) * 100,
        2
    )

    st.success(
        f"Prediction: {remark}"
    )

    st.info(
        f"Model Confidence: {confidence}%"
    )

    # Save Record
    c.execute("""
    INSERT INTO patients
    (
        name,
        email,
        dob,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    )
    VALUES (?,?,?,?,?,?,?)
    """,
    (
        name,
        email,
        str(dob),
        glucose,
        haemoglobin,
        cholesterol,
        remark
    ))

    conn.commit()

    st.success(
        "Patient Record Saved Successfully!"
    )

st.header("Patient Records")

records = c.execute(
    "SELECT * FROM patients"
).fetchall()

if records:

    df = pd.DataFrame(
        records,
        columns=[
            "ID",
            "Name",
            "Email",
            "DOB",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    st.dataframe(df)

st.header("Update Patient")

update_id = st.number_input(
    "Patient ID",
    min_value=1,
    step=1
)

new_name = st.text_input(
    "New Name"
)

new_email = st.text_input(
    "New Email"
)

new_glucose = st.number_input(
    "New Glucose",
    min_value=0.0,
    key="update_glucose"
)

new_haemoglobin = st.number_input(
    "New Haemoglobin",
    min_value=0.0,
    key="update_hb"
)

new_cholesterol = st.number_input(
    "New Cholesterol",
    min_value=0.0,
    key="update_chol"
)

if st.button("Update Patient"):
    # Email Validation
    if "@" not in new_email  or "." not in new_email :
        st.error("Please enter a valid email address")
        st.stop()

    c.execute("""
    UPDATE patients
    SET
        name=?,
        email=?,
        glucose=?,
        haemoglobin=?,
        cholesterol=?
    WHERE id=?
    """,
    (
        new_name,
        new_email,
        new_glucose,
        new_haemoglobin,
        new_cholesterol,
        update_id
    ))

    conn.commit()

    if c.rowcount > 0:
        st.success("Patient Updated Successfully!")
    else:
        st.error("Patient ID not found!")

st.header("Delete Patient")

delete_id = st.number_input(
    "Patient ID to Delete",
    min_value=1,
    step=1,
    key="delete_id"
)

if st.button("Delete Patient"):

    c.execute(
        "DELETE FROM patients WHERE id=?",
        (delete_id,)
    )

    conn.commit()

    st.success(
        "Patient Deleted Successfully!"
    )

