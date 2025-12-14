🔐 Behaviour-Based Authentication System
This project is a machine learning–based security system that detects malicious user sessions using behavioral data instead of only passwords.

It assigns a risk score (0–100) to each session and classifies it as:

Legitimate

Suspicious

Malicious

📌 Project Overview

Traditional login systems depend only on usernames and passwords.
This project improves security by analyzing how users behave during a session.

It continuously checks behavior patterns such as mouse speed, typing speed, and scrolling activity to detect abnormal or malicious sessions.

## 🌐 Live Demo

🔗 **Streamlit App:**  
https://behavioural-app-app-hbutiypvisspj3pjjk2jij.streamlit.app/

📽 **Demo SCREENSHOT :**  

<img width="380" height="517" alt="Screenshot 2025-12-14 201808" src="https://github.com/user-attachments/assets/56d49e76-14d7-47ae-a065-9744d93ffa79" />

DEMO VIDEO :- 





## 💡 Why This Project?

Password-based authentication alone is not enough to prevent attacks such as
account takeover, session hijacking, and automated bots.

This project adds an extra security layer by analyzing user behavior during a session,
making authentication smarter and more secure.

Clarify Binary vs Risk-Based Output:- 
The model internally predicts whether a session is anomalous (0 or 1),
but the final output shown to the user is a risk score and risk label.



🔍 What This System Does

For every user session, the system:

Extracts behavioral features

Uses a trained ML model to predict anomaly probability

Converts probability into a risk score (0–100)

Assigns a risk label based on that score

⚙️ Technologies Used

Python

Streamlit – Web application

Scikit-learn – Machine learning models

Pandas & NumPy – Data processing

Joblib – Saving and loading trained models

🧠 Machine Learning Models Used

Logistic Regression

Random Forest Classifier

The best model is selected automatically based on F1-score, which balances false positives and false negatives.

“Model Selection Logic”:- 
The final model is chosen automatically based on the highest F1-score
to ensure balanced detection of malicious sessions.




🎯 Feature Selection

Important features are selected using Random Forest Feature Importance, which helps:

Remove unnecessary features

Improve model accuracy

Reduce noise in prediction

Only the most influential features are used in the final model.

📊 Risk Scoring Logic (MATCHES YOUR CODE ✅)
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

Confusion Matrix – shows correct and wrong predictions

ROC Curve & AUC – shows how well the model separates normal vs malicious sessions

Risk Score Distribution – shows how risk scores are spread across sessions

🚀 Web Application (Streamlit)

The Streamlit app:

Takes user input for selected features

Scales the input

Predicts risk score

Displays session status in real time

Output Example:

✅ Legitimate (Low Risk)

⚠️ Suspicious (Medium Risk)

🚨 Malicious (High Risk)

▶️ How to Run Locally:- 

1️⃣ Clone the Repository
git clone https://github.com/your-username/behaviour-authentication-system.git
cd behaviour-authentication-system

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py
