# -----------------------------------------
# IMPORT REQUIRED LIBRARIES
# -----------------------------------------

import streamlit as st          # Build web UI
import joblib                   # Load ML models
import pandas as pd             # Data handling

# -----------------------------------------
# LOAD MODEL, SCALER & ENCODERS (CACHED)
# -----------------------------------------

@st.cache_resource
def load_all():
    model = joblib.load("best_model_compressed.joblib")     # Trained ML model
    scaler = joblib.load("scaler.joblib")                   # Feature scaler
    selected_features = joblib.load("selected_features.joblib")  # Feature list
    cluster_encoder = joblib.load("cluster_encoder.joblib") # Label encoder
    return model, scaler, selected_features, cluster_encoder

model, scaler, selected_features, cluster_encoder = load_all()

# -----------------------------------------
# PAGE TITLE & DESCRIPTION
# -----------------------------------------

st.title("🔐 Behaviour-Based Authentication System")

st.write(
    """
    This app predicts whether a user session is **Legitimate**, **Suspicious**  
    or **Malicious** using behavioural patterns.
    """
)

st.subheader("Enter Feature Values Below")

# -----------------------------------------
# USER INPUT SECTION
# -----------------------------------------

user_input = {}   # Dictionary to store user inputs

for feature in selected_features:

    # ---------- CLUSTER FEATURE (TEXT INPUT) ----------
    if feature == "cluster":
        cluster_text = st.selectbox(
            "Cluster Type",
            options=list(cluster_encoder.classes_)
        )

        # Convert text cluster → numeric encoded value
        user_input["cluster"] = cluster_encoder.transform([cluster_text])[0]

    # ---------- NUMERIC FEATURES ----------
    else:
        user_input[feature] = st.number_input(
            feature.replace("_", " ").title(),
            value=None,          # IMPORTANT → allows empty input
            step=0.01
        )

# -----------------------------------------
# PREDICTION BUTTON
# -----------------------------------------

if st.button("🔍 Predict Session Status"):

    # -------------------------------------
    # VALIDATION: CHECK MISSING INPUTS
    # -------------------------------------

    missing_fields = []   # To store empty fields

    for key, value in user_input.items():
        if value is None:
            missing_fields.append(key)

    # If any field is empty → STOP prediction
    if missing_fields:
        st.warning("⚠ Please fill ALL feature fields before prediction.")
        st.stop()   # Stops further execution

    # -------------------------------------
    # MODEL PREDICTION
    # -------------------------------------

    # Convert user input → DataFrame
    input_df = pd.DataFrame([user_input])[selected_features]

    # Scale input features
    scaled_input = scaler.transform(input_df)

    # Predict probability of malicious session
    prob_malicious = model.predict_proba(scaled_input)[0][1]
    risk_score = round(prob_malicious * 100, 2)

    # -------------------------------------
    # DECISION LOGIC
    # -------------------------------------

    if risk_score <= 50:
        st.success(f"✅ ALLOW SESSION | Legitimate | Risk Score: {risk_score}")

    elif risk_score <= 55:
        st.warning(f"⚠ ALERT SESSION | Suspicious | Risk Score: {risk_score}")

    else:
        st.error(f"🚨 BLOCK SESSION | Malicious | Risk Score: {risk_score}")

    # -------------------------------------
    # EXTRA DETAILS
    # -------------------------------------

    st.write("### 🔎 Prediction Details")
    st.write(f"**Risk Score (0–100):** {risk_score}")
    st.write(f"**Raw Probability:** {prob_malicious}")
