# medicineprediction.py

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# 1. Sample Training Data

data = {
    "symptoms": [
        "headache cough body heat",
        "fever cold shivering",
        "stomach pain nausea vomiting",
        "skin rash itching allergy",
        "chest pain difficulty breathing",
        "joint pain swelling fatigue",
        "high fever continuous cough",
        "diarrhea stomach cramps dehydration"
    ],
    "disease": [
        "Flu",
        "Common Cold",
        "Food Poisoning",
        "Allergy",
        "Heart Problem",
        "Arthritis",
        "Pneumonia",
        "Cholera"
    ],
}

df = pd.DataFrame(data)

# 2. Build ML Pipeline

pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(df["symptoms"], df["disease"])

# 3. Medicine & Dosage Mapping

medicine_dict = {
    "Flu": "Paracetamol 500mg",
    "Common Cold": "Antihistamine (Cetirizine)",
    "Food Poisoning": "ORS + Antiemetic",
    "Allergy": "Antihistamine (Loratadine)",
    "Heart Problem": "Immediate doctor consultation",
    "Arthritis": "Pain Reliever (Ibuprofen)",
    "Pneumonia": "Antibiotics (Consult doctor)",
    "Cholera": "ORS + Antibiotics (Consult doctor)"
}

# Dosage rules by age
def dosage_recommendation(medicine, age):
    if "doctor" in medicine.lower() or "consult" in medicine.lower():
        return "Please consult a doctor immediately."
    
    if age < 12:
        return f"{medicine} — Pediatric dose (Consult pediatrician)"
    elif 12 <= age <= 60:
        return f"{medicine} — Standard adult dose"
    else:
        return f"{medicine} — Lower dose recommended for elderly"

# 4. Streamlit UI

st.set_page_config(page_title="Medicine Prediction System", layout="wide")

# Pista green background
st.markdown(
    """
    <style>
        body {
            background-color: #e6f5d6;
        }
        .stButton>button {
            background-color: #a8d5ba;
            color: black;
            border-radius: 8px;
            font-size: 16px;
        }
        .stTextInput>div>div>input {
            background-color: #f5f5f5;
        }
        .stTextArea textarea {
            background-color: #f5f5f5;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Medicine Prediction System")
st.write("This system predicts a possible disease based on symptoms and recommends medicines with dosage guidance based on age.")
st.warning("For educational purposes only — not medical advice.")

# Input fields
symptoms_input = st.text_area("Enter your symptoms", placeholder="e.g. headache, cough, body heat")
age = st.number_input("Enter your age", min_value=1, max_value=120, value=20)

if st.button("Predict"):
    if symptoms_input.strip():
        prediction = pipeline.predict([symptoms_input])[0]
        medicine = medicine_dict.get(prediction, "No specific medicine found")
        dosage = dosage_recommendation(medicine, age)

        st.success(f"**Predicted Disease:** {prediction}")
        st.info(f"**Recommended Medicine:** {dosage}")
    else:
        st.error("Please enter symptoms.")

#text feature extraction -(countVectorizer)
#Classification algorithm - (Multinomial Naive Bayes (mnb))
#Pipelint - ([countVectorizer,mnb])
#Rule-based Medicine Recommendation
#Dosage recommendation based on age