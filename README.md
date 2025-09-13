# Medicine-Prediction-System
The "Medicine Prediction System" is a Streamlit web app that predicts diseases from symptoms using "CountVectorizer + Naive Bayes" and recommends medicines with age-based dosage guidance. It combines ML classification with rule-based mapping and features . For educational use only.
Here’s a clean **README.md** file for your GitHub repo 👇

````markdown

# Medicine Prediction System

The "Medicine Prediction System" is a machine learning–based web app built with "Streamlit" that predicts possible diseases from user-entered symptoms and recommends medicines with dosage guidance based on age. It uses "CountVectorizer + Naive Bayes" for text classification and provides a clean modern UI theme.

⚠ "This project is for educational purposes only and should not be considered professional medical advice."

# Features
- Predict diseases from symptoms using "ML classification"
- Medicine recommendations with "rule-based mapping"
- "Age-based dosage guidance" (children, adults, elderly)
- Suggests doctor consultation for severe cases
- Modern pista green UI with Streamlit

# Tech Stack
- "Python"
- "Scikit-learn" (CountVectorizer, Multinomial Naive Bayes, Pipeline)
- "Pandas"
- "Streamlit"

# Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/medicineprediction.git
   cd medicineprediction
````

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run medicineprediction.py
   ```
   
# How It Works

1. User enters symptoms in text form.
2. Symptoms are vectorized using **CountVectorizer**.
3. **Naive Bayes classifier** predicts the disease.
4. A rule-based mapping suggests medicines.
5. Dosage is adjusted based on **age group**.

# Future Enhancements

* Expand dataset with more symptoms and diseases
* Support multiple ML algorithms (Logistic Regression, Decision Tree, etc.)
* Integrate with external medical APIs
* Add history/log feature for users

---

# License

This project is licensed under the MIT License.
