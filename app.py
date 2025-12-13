import streamlit as st
import joblib
import pandas as pd

# -----------------------------------------
# LOAD MODEL, SCALER & SELECTED FEATURES
# -----------------------------------------

@st.cache_resource
def load_all():
    model = joblib.load("best_model_compressed.joblib")
    scaler = joblib.load("scaler.joblib")
    selected_features = joblib.load("selected_features.joblib")
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
# USER INPUT
# -----------------------------------------

user_input = {}

for feature in selected_features:
    user_input[feature] = st.number_input(
        feature.replace("_", " ").title(),
        value=0.0
    )

# -----------------------------------------
# PREDICTION
# -----------------------------------------

if st.button("🔍 Predict Session Status"):

    # Block empty input
    if all(value == 0 for value in user_input.values()):
        st.warning("⚠ Please enter feature values before prediction.")
        st.stop()

    # Convert input → DataFrame
    input_df = pd.DataFrame([user_input])[selected_features]

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Predict probability
    prob_malicious = model.predict_proba(scaled_input)[0][1]
    risk_score = round(prob_malicious * 100, 2)

    # Decision logic
    if risk_score <= 50:
        st.success(f"✅ ALLOW SESSION | Legitimate | Risk Score: {risk_score}")

    elif risk_score <= 55:
        st.warning(f"⚠ ALERT SESSION | Suspicious | Risk Score: {risk_score}")

    else:
        st.error(f"🚨 BLOCK SESSION | Malicious | Risk Score: {risk_score}")

    # Extra details
    st.write("### 🔎 Prediction Details")
    st.write(f"**Risk Score (0–100):** {risk_score}")
    st.write(f"**Raw Probability:** {prob_malicious}")

