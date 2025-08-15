# 🩺 Diabetes Prediction Web App

This is a Machine Learning-based web application built using **Streamlit** that predicts whether a person is diabetic or not based on their medical details.  
It uses the **PIMA Indian Diabetes Dataset** and a trained classification model.

---

## 📂 Project Structure
📦 Diabetes Prediction
┣ 📜 diabetes.csv # Dataset
┣ 📜 model.ipynb # Jupyter notebook for model training
┣ 📜 model.pkl # Saved trained model
┣ 📜 app.py # Streamlit web app
┗ 📜 README.md # Project documentation

---

## ⚙️ How It Works
1. **Data Preprocessing** – Cleans and prepares the dataset.
2. **Model Training** – Trains a classification model (e.g., Logistic Regression, Random Forest, etc.).
3. **Model Saving** – Saves the trained model as `model.pkl` using `pickle`.
4. **Web App Interface** – Streamlit app takes user input and predicts diabetes status.

---

## 🚀 Installation & Running the App

1. **Clone the repository**
   ```bash
   git clone https://github.com/charan-0978/Diabetes_prediction.git
   cd Diabetes_Prediction
Install dependencies
pip install -r requirements.txt
Run the Streamlit app
streamlit run app.py
📊 Features
User-friendly web interface.
Takes medical input parameters:
Pregnancies
Glucose Level
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes Pedigree Function
Age
Displays results as Diabetic or Not Diabetic.
🛠 Requirements
Create a requirements.txt with:
streamlit
numpy
pandas
scikit-learn
