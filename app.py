import streamlit as st
import joblib
import numpy as np
import pandas as pd

# -----------------------------------------
# LOAD MODEL, SCALER & SELECTED FEATURES
# -----------------------------------------

@st.cache_resource
def load_all():
    model = joblib.load("best_model_compressed.joblib")       # ML model
    scaler = joblib.load("scaler.joblib")                     # StandardScaler
    selected_features = joblib.load("selected_features.joblib")  # List of features
    return model, scaler, selected_features

model, scaler, selected_features = load_all()

# -----------------------------------------
# STREAMLIT PAGE UI
# -----------------------------------------

st.title("🔐 Behaviour-Based Authentication System")
st.write(
    """
    This app predicts whether a user session is **Legitimate**, **Suspicious**,  
    or **Malicious** using behavioural patterns.
    """
)

st.subheader("Enter Feature Values Below")

# -----------------------------------------
# TAKE USER INPUT FOR EACH FEATURE
# -----------------------------------------

user_input = {}

for feature in selected_features:
    user_input[feature] = st.number_input(
        f"{feature}", 
        value=0.0, 
        help="Enter numerical value for this feature"
    )

# Convert input to DataFrame
input_df = pd.DataFrame([user_input])[selected_features]

# Scale input data
scaled_input = scaler.transform(input_df)

# -----------------------------------------
# PREDICTION BUTTON
# -----------------------------------------

if st.button("🔍 Predict Session Status"):


    # Check if all inputs are zero
    if all(value == 0 for value in user_input.values()):
        st.warning("⚠ Please enter feature values before prediction.")
        st.stop()

    # Probability of malicious behaviour
    prob_malicious = model.predict_proba(scaled_input)[0][1]

    # Convert probability → risk score
    risk_score = round(prob_malicious * 100, 2)

    # Risk-based decision logic
    if risk_score <= 65:
        decision = "✅ ALLOW SESSION"
        label = "Legitimate Session"
        st.success(f"{decision} — {label} | Risk Score: {risk_score}")

    elif risk_score <= 70:
        decision = "⚠ ALERT SESSION"
        label = "Suspicious Behaviour"
        st.warning(f"{decision} — {label} | Risk Score: {risk_score}")

    else:
        decision = "🚨 BLOCK SESSION"
        label = "Malicious Session"
        st.error(f"{decision} — {label} | Risk Score: {risk_score}")

    # Technical details (optional)
    st.write("### 🔎 Prediction Details")
    st.write(f"**Risk Score (0–100):** {risk_score}")
    st.write(f"**Raw Probability:** {prob_malicious}")






