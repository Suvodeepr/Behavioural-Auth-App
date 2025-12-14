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

▶️ How to Run This Project on Your Own Computer (Step by Step)

🔹 Step 1: Install Required Software (One Time Only)

Before starting, make sure these are installed on your computer:

Python (version 3.8 or higher)
👉 Download from: https://www.python.org/downloads/

Git (used to download the project from GitHub)
👉 Download from: https://git-scm.com/downloads

After installation, restart your computer once.

🔹 Step 2: Clone (Download) the Project from GitHub

Cloning means downloading the full project from GitHub to your computer.

Open Command Prompt (Windows) or Terminal (Mac/Linux)

Copy and paste the command below, then press Enter:

git clone https://github.com/Suvodeepr/Behavioural-Auth-App.git


This will create a folder named Behavioural-Auth-App on your computer.

🔹 Step 3: Go Inside the Project Folder

After cloning, you must move into the project folder.

In the same terminal / command prompt, type:

cd Behavioural-Auth-App


Now you are inside the project directory.

🔹 Step 4: Install Required Python Libraries (Dependencies)

The project needs some Python libraries to run (Streamlit, Scikit-learn, etc.).

Run this command:

pip install -r requirements.txt


This will automatically install all required libraries listed in requirements.txt.

⏳ This may take a few minutes the first time.

🔹 Step 5: Run the Streamlit Web Application

After successful installation, start the app by running:

streamlit run app.py in cmd

🔹 Step 6: Open the App in Your Browser

A browser window will open automatically

If not, copy the local URL shown in the terminal, usually:

http://localhost:8501


Paste it into your browser and press Enter.

🎉 The Behaviour-Based Authentication System is now running on your computer!
