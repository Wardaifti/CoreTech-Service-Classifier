import streamlit as st
import joblib

# App Title and Styling
st.set_page_config(page_title="CoreTech Smart Service Classifier", page_icon="⚡", layout="centered")

# Custom CSS for better design
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    h1 {
        color: #2C3E50;
        text-align: center;
        font-size: 2.5rem;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #6c757d;
        margin-top: 30px;
    }
    .stTextArea textarea {
        font-size: 16px;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #2C3E50;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton button:hover {
        background-color: #1ABC9C;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("⚡ CoreTech Smart Service Classifier ⚡")
st.write("### Predict the category of a job or service description using AI.")

# Load Model
model_path = "job_classification_model.pkl"
try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Input Section
with st.container():
    job_description = st.text_area("✏️ Enter Job / Service Description", placeholder="Type job details here...")

    # Prediction Button
    if st.button("🔍 Classify"):
        if job_description.strip() == "":
            st.warning("Please enter a job description.")
        else:
            try:
                prediction = model.predict([job_description])[0]
                st.success(f"✅ Predicted Category: **{prediction}**")
            except Exception as e:
                st.error(f"Prediction error: {e}")

# Footer
st.markdown("<div class='footer'>Powered by <b>CoreTech</b> | AI Smart Services</div>", unsafe_allow_html=True)
