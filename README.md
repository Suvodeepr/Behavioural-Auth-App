# 🔐 Behaviour-Based Authentication System

This project implements a **behaviour-based authentication and malicious session detection system** using machine learning.  
It analyzes user session behavior and assigns a **continuous risk score** to classify sessions as **Legitimate**, **Suspicious**, or **Malicious**.

---

## 📌 Project Overview

Traditional authentication systems rely on static credentials.  
This system enhances security by continuously monitoring **behavioral patterns** such as session activity and interaction features to detect anomalies in real time.

The model outputs:
- A **binary prediction** (Normal / Anomalous)
- A **risk score (0–100)**
- A **risk label** based on severity

---

## ⚙️ Technologies Used

- Python  
- Streamlit (Web Application)  
- Scikit-learn (Machine Learning)  
- Pandas & NumPy (Data Processing)  
- Joblib (Model Serialization)

---

## 🧠 Machine Learning Models

- Logistic Regression  
- Random Forest Classifier
- Naive Bayes

The final model is selected based on **F1-score and Recall**, ensuring better detection of malicious sessions.

---

## 📊 Risk Scoring Logic

| Risk Score Range | Risk Label |
|------------------|------------|
| 0 – 30 | Legitimate |
| 31 – 70 | Suspicious |
| 71 – 100 | Malicious |

This allows **fine-grained, continuous behavioral analysis** instead of simple binary decisions.

---

## 🚀 Deployment

The application is deployed using **Streamlit Cloud** and hosted via **GitHub**.

**Live App:**  
👉 *Add your Streamlit app URL here*

---

## ▶️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/behaviour-authentication-system.git
   cd behaviour-authentication-system
pip install -r requirements.txt
streamlit run app.py
