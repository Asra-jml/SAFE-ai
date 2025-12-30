# SAFE-ai 🛡️

**SAFE (Smart AI for Fraud Elimination)** is an intelligent machine learning-powered web application designed to detect fraudulent financial transactions in real-time. With a modern, user-friendly interface and robust predictive capabilities, SAFE helps safeguard financial assets and ensure transaction security.

## 🎯 Project Overview

SAFE-ai is a fraud detection system that leverages machine learning algorithms to analyze financial transaction patterns and identify potentially fraudulent activities. The project demonstrates the practical application of data science and AI in the financial security domain, providing an accessible tool for fraud detection that can be deployed as a web service.

## ✨ Key Features

- **Real-time Fraud Detection**: Instant analysis of transaction data to predict fraudulent activities
- **Interactive Web Interface**: Built with Streamlit for a seamless user experience
- **Multiple Transaction Types**: Supports analysis of various transaction types (CASH_OUT, PAYMENT, CASH_IN, TRANSFER, DEPOSIT)
- **Balance Tracking**: Monitors sender and receiver account balances for anomaly detection
- **Modern UI/UX**: Dark theme with purple accent colors (#a259ec) for an elegant appearance
- **Easy-to-Use**: Simple form-based input with clear prediction results
- **Machine Learning Powered**: Pre-trained model for accurate fraud predictions

## 🛠️ Technology Stack

- **Python 3.x**: Core programming language
- **Streamlit**: Web application framework for the interactive UI
- **Pandas**: Data manipulation and analysis
- **Joblib**: Model serialization and loading
- **Scikit-learn** (implied): Machine learning framework for model training

## 📋 Prerequisites

Before running this application, ensure you have Python 3.7 or higher installed on your system.

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Asra-jml/SAFE-ai.git
   cd SAFE-ai
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Start the application**:
   ```bash
   streamlit run fraud_detection.py
   ```

2. **Access the web interface**:
   - The application will automatically open in your default web browser
   - If not, navigate to `http://localhost:8501`

3. **Using the application**:
   - **Home Page**: Welcome screen with project information
   - **Prediction Page**: Enter transaction details to check for fraud
     - Select transaction type from dropdown
     - Input transaction amount
     - Enter sender's old and new balance
     - Enter receiver's old and new balance
     - Click "Predict Fraud" to get results

4. **Interpreting results**:
   - **LEGITIMATE**: Transaction appears to be genuine (shown in green)
   - **FRAUDULENT**: Transaction appears to be fraudulent (shown in red)

## 📁 Project Structure

```
SAFE-ai/
├── fraud_detection.py          # Main Streamlit application
├── fraud_detection_model.pkl   # Pre-trained ML model
├── analysis_model.ipynb        # Jupyter notebook for model development
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore file
```

## 🧠 Model Information

The fraud detection model (`fraud_detection_model.pkl`) is a pre-trained machine learning model that analyzes the following features:

- **Transaction Type**: Category of the transaction (CASH_OUT, PAYMENT, CASH_IN, TRANSFER, DEPOSIT)
- **Amount**: Transaction value in currency units
- **Old Balance (Sender)**: Account balance before the transaction
- **New Balance (Sender)**: Account balance after the transaction
- **Old Balance (Receiver)**: Recipient's balance before receiving
- **New Balance (Receiver)**: Recipient's balance after receiving

The model uses these features to identify patterns commonly associated with fraudulent transactions, such as:
- Unusual balance changes
- Suspicious transaction amounts
- Irregular transaction types
- Inconsistent balance movements

## 🎨 UI Design

The application features a modern dark theme with:
- **Primary Color**: Dark background (#181818)
- **Accent Color**: Purple (#a259ec)
- **Font**: Montserrat for headers
- **Design Elements**: Rounded corners, subtle shadows, and clean layouts

## 👤 Developer Information

**Asra Jamal**
- 📧 Email: asrajamalashraf@gmail.com
- 📱 Phone: +91-9931377661

This project was developed to demonstrate the practical application of machine learning in financial fraud detection and to provide a reliable tool for identifying fraudulent activities in financial transactions.

## 🔮 Future Enhancements

Potential improvements for the project include:

1. **Model Improvements**:
   - Regular retraining with updated data
   - Ensemble methods for better accuracy
   - Deep learning models for complex pattern recognition

2. **Feature Additions**:
   - Historical transaction analysis
   - Batch processing capabilities
   - API endpoint for integration with other systems
   - Dashboard with analytics and statistics

3. **Security Enhancements**:
   - User authentication
   - Transaction logging
   - Data encryption
   - Audit trails

4. **Visualization**:
   - Transaction pattern graphs
   - Risk score visualization
   - Statistical reports
   - Fraud trend analysis

## 📄 License

This project is open-source and available for educational and research purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit pull requests.

## ⚠️ Disclaimer

This application is designed for educational and demonstration purposes. While the model provides predictions based on machine learning algorithms, it should not be used as the sole basis for financial decisions. Always consult with financial security experts and use multiple verification methods for critical transactions.

## 📚 References

- Machine Learning for Fraud Detection
- Financial Transaction Security
- Streamlit Documentation
- Scikit-learn Documentation

---

**SAFE - Smart AI for Fraud Elimination** | Protecting Your Financial Future with AI 🛡️
