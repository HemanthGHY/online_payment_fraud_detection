
# ONLINE PAYMENT FRAUD DETECTION SYSTEM

Online Payment Fraud Detection System is a Machine Learning–based application designed to detect fraudulent online payment transactions.
The system uses the PaySim mobile money transaction dataset and trained Machine Learning models to classify transactions as fraudulent or legitimate.

--------------------------------------------------
## FEATURES
--------------------------------------------------
- Online payment fraud detection using Machine Learning
- Flask-based backend application
- Multiple trained ML models for comparison
- Realistic transaction dataset (PaySim)
- Data preprocessing and feature engineering
- Fast prediction using pre-trained models

--------------------------------------------------
## PREREQUISITES
--------------------------------------------------
- Python 3.8 or higher
- Pip package manager
- Virtual environment (recommended)

--------------------------------------------------
### INSTALLATION AND EXECUTION
--------------------------------------------------
1. Clone the repository
   git clone https://github.com/HemanthGHY/online-payment-fraud-detection.git
   cd online-payment-fraud-detection

2. Navigate to the Flask directory
   cd "Project Files/flask"

3. Create and activate virtual environment
   python -m venv myenv
   myenv\Scripts\activate        (Windows)
   source myenv/bin/activate     (Linux / Mac)

4. Install required dependencies
   pip install -r requirements.txt

5. Run the application
   python app.py

6. Open browser and access
   http://127.0.0.1:5000/

--------------------------------------------------
### PROJECT STRUCTURE
--------------------------------------------------
Project Files/
|
|-- data/
|   |-- PS_20174392719_1491204439457_log.csv
|
|-- training/
|   |-- ofd_analysis.ipynb
|   |-- ofd_data_preprocessing_and_model_building_and_saving.ipynb
|   |-- online_payments_fraud_detection.ipynb
|
|-- flask/
|   |-- app.py
|   |
|   |-- models/
|   |   |-- fraud_model.pkl
|   |   |-- fraud_rfc.pkl
|   |   |-- svc_model.pkl
|   |   |-- xgb_model.pkl
|   |   |-- etc_model.pkl
|   |   |-- model.pkl
|   |   |-- type_encoder.pkl
|   |
|   |-- templates/ 
|   |   |-- index.html
|   |   |-- predict.html
|   |   |-- result.html
|   |
|   |-- static/
|   |   |-- index.css
|   |
|   |-- myenv/
|
|-- requirements.txt
|-- README.txt

--------------------------------------------------
### DATASET INFORMATION
--------------------------------------------------
Dataset Name: PaySim Mobile Money Dataset

Attributes:
- step               : Time step of transaction
- type               : Transaction type
- amount             : Transaction amount
- oldbalanceOrg      : Sender balance before transaction
- newbalanceOrig     : Sender balance after transaction
- oldbalanceDest     : Receiver balance before transaction
- newbalanceDest     : Receiver balance after transaction
- isFraud            : Target variable (1 = Fraud, 0 = Legitimate)

Note:
This dataset is synthetic and intended strictly for educational and research purposes.

--------------------------------------------------
### MACHINE LEARNING MODELS
--------------------------------------------------
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)
- XGBoost
- Extra Trees Classifier

Evaluation Metrics:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

--------------------------------------------------
### APPLICATION WORKFLOW
--------------------------------------------------
1. User provides transaction details
2. Data preprocessing and encoding
3. Model prediction
4. Transaction classified as Fraud or Legitimate

--------------------------------------------------
### USE CASES
--------------------------------------------------
- Banking and Financial Institutions
- Online Payment Systems
- FinTech Applications
- Fraud Detection and Risk Management


### Contact For questions or feedback, please contact:
- **Name**: Gaddam Hemanth
- **Email**: gaddamhemanthyadav@gmail.com
- **GitHub**: https://github.com/HemanthGHY