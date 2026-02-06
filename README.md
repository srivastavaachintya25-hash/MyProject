# 🌾 Crop Yield Prediction Using Machine Learning

## 📌 Overview
This project predicts crop yield based on environmental and agricultural factors using machine learning. The aim is to help understand how factors like rainfall, fertilizer, and pesticide usage influence crop productivity.

---

## 🎯 Problem Statement
Accurate crop yield prediction is challenging due to varying environmental conditions. Farmers and planners need data-driven tools to estimate yield and improve decision-making.

---

## 🚀 Objective
- Build a machine learning model to predict crop yield  
- Use environmental and agricultural parameters  
- Deploy the model using a Streamlit web application  

---

## 📊 Dataset
- Source: Public agriculture dataset  
- Features used:
  - Area (hectares)
  - Annual Rainfall (mm)
  - Fertilizer usage
  - Pesticide usage
- Target variable:
  - Yield (tonnes per hectare)

---

## 🔍 Exploratory Data Analysis (EDA)
- Dataset structure analysis
- Identification of missing values
- Feature relevance analysis
- Removal of irrelevant or sparse categorical columns

---

## ⚙️ Feature Engineering & Preprocessing
- Selected relevant numeric features
- Handled missing values using mean imputation
- Removed invalid and infinite values
- Performed train-test split (80-20)

---

## 🤖 Models Used
- Linear Regression (baseline model)
- Decision Tree Regression
- Random Forest Regression (final model)

---

## 📈 Model Evaluation
- Evaluation Metric: R² Score
- Best Model: Random Forest
- R² Score: ~0.13

---

## 🖥️ Deployment
- Model saved as a `.pkl` file
- Streamlit used for real-time prediction
- Users input values and receive yield predictions

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook

---

## ▶️ How to Run the Project
```bash
pip install -r requirement.text
streamlit run main.py
