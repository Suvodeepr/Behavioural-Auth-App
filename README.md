🔐 Behaviour-Based Authentication System

This project is a machine learning–based security system that detects malicious user sessions using behavioral data instead of only passwords.

It assigns a risk score (0–100) to each session and classifies it as:

✅ Legitimate

⚠️ Suspicious

🚨 Malicious

📌 Project Overview

Traditional login systems depend only on usernames and passwords.
This project improves security by analyzing how users behave during a session.

It continuously monitors behavior such as:

Mouse movement speed

Typing speed

Scrolling activity

to detect abnormal or malicious sessions.

🌐 Live Demo

🔗 Streamlit App:
https://behavioural-app-app-hbutiypvisspj3pjjk2jij.streamlit.app/

📸 UI Screenshot:

<img width="380" height="517" src="https://github.com/user-attachments/assets/56d49e76-14d7-47ae-a065-9744d93ffa79" />

📽 Demo Video:
https://github.com/user-attachments/assets/731d64cb-2a6b-44d0-8d5d-b265be49bc32

💡 Why This Project?

Password-based authentication alone is not enough to prevent attacks such as:

Account takeover

Session hijacking

Automated bots

This project adds an extra security layer by analyzing user behavior during a session.

🔍 What This System Does

For every user session, the system:

Extracts behavioral features

Uses a trained ML model to predict anomaly probability

Converts probability into a risk score (0–100)

Assigns a risk label based on severity

⚙️ Technologies Used

Python

Streamlit – Web application

Scikit-learn – Machine learning

Pandas & NumPy – Data processing

Joblib – Model saving & loading

🧠 Machine Learning Models Used

Logistic Regression

Random Forest Classifier

The best model is selected automatically based on F1-score, ensuring balanced detection of malicious sessions.

🎯 Feature Selection

Important features are selected using Random Forest Feature Importance, which helps to:

Remove unnecessary features

Improve model accuracy

Reduce noise in prediction

Only the most influential features are used in the final model.

📊 Risk Scoring Logic
Risk Score	Session Type
0 – 50	Legitimate
51 – 55	Suspicious
56 – 100	Malicious

This allows continuous and fine-grained security decisions instead of simple yes/no output.

🧪 Features Used for Prediction

The Streamlit UI accepts the following features:

Mouse Average Speed

Latitude

Longitude

Typing Speed (characters per second)

Cluster ID

Scroll Speed

These features are scaled using the same scaler used during training.

📈 Model Evaluation

The model is evaluated using:

Confusion Matrix – correct vs incorrect predictions

ROC Curve & AUC – separation ability

Risk Score Distribution – score spread

🚀 Web Application (Streamlit)

The Streamlit app:

Takes user input

Scales input features

Predicts risk score

Displays session status in real time

Output Examples

✅ Legitimate (Low Risk)

⚠️ Suspicious (Medium Risk)

🚨 Malicious (High Risk)

▶️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/Suvodeepr/Behavioural-Auth-App
cd behaviour-authentication-system

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py
