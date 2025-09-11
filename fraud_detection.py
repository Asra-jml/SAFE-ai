
import streamlit as st
import pandas as pd
import joblib

try:
    model = joblib.load('fraud_detection_model.pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.markdown("""
    <style>
    body, .main, .stApp {
        background-color: #181818 !important;
        color: #a259ec !important;
    }
    .block-container {
        background: #181818 !important;
        border-radius: 18px;
        box-shadow: 0 4px 24px 0 rgba(162, 89, 236, 0.08);
        color: #a259ec !important;
    }
    h1, h2, h3, h4 {
        color: #a259ec !important;
        font-family: 'Montserrat', sans-serif;
    }
    .stButton>button {
        background: #a259ec !important;
        color: #181818 !important;
        border-radius: 8px;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(162, 89, 236, 0.12);
        border: none;
    }
    .stTextInput>div>input, .stNumberInput>div>input {
        border-radius: 8px;
        border: 1px solid #a259ec !important;
        background: #181818 !important;
        color: #a259ec !important;
    }
    .stSelectbox>div>div {
        border-radius: 8px;
        border: 1px solid #a259ec !important;
        background: #181818 !important;
        color: #a259ec !important;
    }
    .stSuccess, .stError {
        border-radius: 8px;
        font-size: 1.1rem;
        background: #181818 !important;
        color: #a259ec !important;
        border: 1px solid #a259ec !important;
    }
    .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stCaption {
        color: #a259ec !important;
    }
    .stSidebar, .stSidebarContent {
        background: #181818 !important;
        color: #a259ec !important;
    }
    img {
        filter: grayscale(100%) brightness(0.7) sepia(1) hue-rotate(-60deg) saturate(8) !important;
        border: 2px solid #a259ec !important;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)


with st.sidebar:
    #st.image("https://cdn.pixabay.com/photo/2017/01/31/13/14/money-2025467_1280.png", width=120)
    st.markdown("<h2 style='color:#a259ec;'>SAFE - Smart AI for Fraud Elimination</h2>", unsafe_allow_html=True)
    st.markdown("<span style='color:#fff;'>Hii, this project was built by Asra Jamal to demonstrate fraud detection in financial transactions.<br> This is a modern tool for financial transaction analysis. <br>The goal is to provide a reliable tool for identifying fraudulent activities.<br> In this project, we utilize machine learning algorithms to analyze transaction patterns and detect anomalies.</span>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#a259ec;'>Contact details:</h3>", unsafe_allow_html=True)
    st.markdown("<span style='color:#ffff;'>+91-9931377661<br> asrajamalashraf@gmail.com</span>", unsafe_allow_html=True)

#page navigation
st.session_state.setdefault('page', 'home')

def go_home():
    st.session_state['page'] = 'home'

def go_predict():
    st.session_state['page'] = 'predict'


if st.session_state['page'] == 'home':
    st.markdown("""
    <h1 style='text-align:center; font-family:Montserrat; color:#a259ec; margin-bottom: 0.5em;'>SAFE - Smart AI for Fraud Elimination</h1>
    <div style='text-align:center; color:#ffffff; font-size:1.1rem; max-width:600px; margin:auto;'>
        <p>
        SAFE leverages advanced machine learning techniques to analyze financial transactions and detect potential fraud.<br>
        Designed for accuracy and speed, it helps safeguard your assets.<br>
        Experience a secure and seamless way to validate your transactions with confidence.
        </p>
    </div>
    <div style='height: 60px;'></div>
    """, unsafe_allow_html=True)
    
    btn_col1, btn_col2, btn_col3 = st.columns([1,2,1])
    with btn_col2:
        st.button("Ready to check your transaction? Click here!", on_click=go_predict)

elif st.session_state['page'] == 'predict':
    st.markdown("""
    <h1 style='text-align:center; font-family:Montserrat; color:#a259ec;'>Fraud Detection in Financial Transactions</h1>
    <p style='text-align:center; color:#ffffff; font-size:1.2rem;'>Enter transaction details below to check for fraud.</p>
    """, unsafe_allow_html=True)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        transaction_type = st.selectbox("Transaction Type", ['CASH_OUT', 'PAYMENT', 'CASH_IN', 'TRANSFER', 'DEPOSIT'])
        amount = st.number_input("Amount", min_value=0.0, value=1000.0)
        oldbalanceOrg = st.number_input("Old Balance (sender)", min_value=0.0, value=10000.0)
    with col2:
        newbalanceOrig = st.number_input("New Balance (sender)", min_value=0.0, value=9000.0)
        oldbalanceDest = st.number_input("Old Balance (receiver)", min_value=0.0, value=0.0)
        newbalanceDest = st.number_input("New Balance (receiver)", min_value=0.0, value=0.0)
    st.markdown("---")
    if st.button("Predict Fraud", use_container_width=True):
        input_data = pd.DataFrame([{
            'type': transaction_type,
            'amount': amount,
            'oldbalanceOrg': oldbalanceOrg,
            'newbalanceOrig': newbalanceOrig,
            'oldbalanceDest': oldbalanceDest,
            'newbalanceDest': newbalanceDest
        }])
        prediction = model.predict(input_data)[0]
        st.subheader(f"Prediction: {'FRAUDULENT' if int(prediction)==1 else 'LEGITIMATE'}")
        if prediction == 1:
            st.error("The transaction is predicted to be FRAUDULENT.")
        else:
            st.success("The transaction is predicted to be LEGITIMATE.")
    st.button("Back to Home", on_click=go_home, use_container_width=True)