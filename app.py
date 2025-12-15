# Import Streamlit → build web UI
import streamlit as st

# Import joblib → load saved ML files
import joblib

# Import pandas → create DataFrame
import pandas as pd

# -----------------------------------------
# LOAD MODEL, SCALER, FEATURES & ENCODER
# -----------------------------------------

@st.cache_resource
def load_all():
    model = joblib.load("best_model_compressed.joblib")
    scaler = joblib.load("scaler.joblib")
    selected_features = joblib.load("selected_features.joblib")
    cluster_encoder = joblib.load("cluster_encoder.joblib")
    return model, scaler, selected_features, cluster_encoder

model, scaler, selected_features, cluster_encoder = load_all()

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

    # SPECIAL CASE: CLUSTER (TEXT INPUT)
    if feature == "cluster":
        cluster_text = st.selectbox(
            "Cluster Type",
            options=list(cluster_encoder.classes_)
        )

        # Convert text → encoded number
        user_input["cluster"] = cluster_encoder.transform([cluster_text])[0]

    # ALL OTHER FEATURES (NUMERIC)
    else:
        user_input[feature] = st.number_input(
            feature.replace("_", " ").title(),
            value=0.0
        )

# -----------------------------------------
# PREDICTION
# -----------------------------------------

if st.button("🔍 Predict Session Status"):

    # Convert input → DataFrame
    input_df = pd.DataFrame([user_input])[selected_features]

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Predict probability
    prob_malicious = model.predict_proba(scaled_input)[0][1]
    risk_score = round(prob_malicious * 100, 2)

    # Decision logic (MATCHES COLAB)
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
