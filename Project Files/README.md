ONLINE PAYMENT FRAUD DETECTION SYSTEM
====================================

An end-to-end Machine Learning–based fraud detection system that identifies
fraudulent online payment transactions using transaction behavior and balance
inconsistencies.

The project covers data preprocessing, model training, evaluation, and
deployment using Flask.

--------------------------------------------------------------------

PROJECT OVERVIEW
----------------
Online payment fraud is a major financial risk.
This project classifies transactions into:

- Fraud (1)
- Not Fraud (0)

using supervised machine learning models trained on a PaySim-style dataset.

The system:
- Learns fraud patterns from historical transaction data
- Predicts fraud probability for new transactions
- Provides a web-based interface using Flask

--------------------------------------------------------------------

PROJECT STRUCTURE
-----------------
online_payments_fraud_detection/
    training/
        ofd_analysis.ipynb
        ofd_data_preprocessing_and_model_building_and_saving.ipynb
        online_payments_fraud_detection.ipynb
    training_ibm/
        online_payments_fraud_prediction_using_ibm.ipynb
    flask/
        models/
            type_encoder.pkl
            fraud_model.pkl
        templates/
            index.html
            predict.html
            result.html
        static/
            style.css
        app.py
    requirements.txt
    README.md

--------------------------------------------------------------------

DATASET DESCRIPTION
-------------------
The dataset is based on PaySim, a financial transaction simulator.

FEATURES USED:
- step              : Time step of the transaction
- type              : Transaction type (PAYMENT, TRANSFER, CASH_OUT, etc.)
- amount            : Transaction amount
- oldbalanceOrg     : Sender balance before transaction
- newbalanceOrig    : Sender balance after transaction
- oldbalanceDest    : Receiver balance before transaction
- newbalanceDest    : Receiver balance after transaction

TARGET VARIABLE:
- isFraud
    0 -> Not Fraud
    1 -> Fraud

IMPORTANT NOTE:
The column "isFlaggedFraud" is intentionally excluded to avoid data leakage.
It is a system-generated rule-based flag and is not available at real
transaction time.

--------------------------------------------------------------------

TECHNOLOGIES USED
-----------------
- Python
- NumPy
- Pandas
- Scikit-learn
- Flask
- Matplotlib
- Seaborn
- Joblib / Pickle

--------------------------------------------------------------------

MACHINE LEARNING MODELS
----------------------
Models experimented with in this project:

- Decision Tree Classifier (primary deployed model)
- Random Forest Classifier (comparison model)
- Logistic Regression (baseline)
- Support Vector Classifier (optional)

KEY CHALLENGES ADDRESSED:
- Severe class imbalance
- Feature consistency between training and inference
- Probability-based fraud detection

--------------------------------------------------------------------

MODEL EVALUATION
----------------
Due to heavy class imbalance, the following metrics are emphasized:

- Confusion Matrix
- Precision, Recall, F1-score
- ROC-AUC Score
- Fraud probability thresholding

--------------------------------------------------------------------

FLASK WEB APPLICATION
--------------------
The Flask application allows users to:
1. Enter transaction details
2. Submit the transaction
3. View fraud prediction and probability

SAMPLE FRAUD INPUT:
step: 45
type: TRANSFER
amount: 9000
oldbalanceOrg: 10000
newbalanceOrig: 10000
oldbalanceDest: 0
newbalanceDest: 0

OUTPUT:
Fraud Detected (High Probability)

--------------------------------------------------------------------

HOW TO RUN THE PROJECT
---------------------

1. CREATE AND ACTIVATE VIRTUAL ENVIRONMENT

Windows:
python -m venv myenv
myenv\Scripts\activate

2. INSTALL DEPENDENCIES

pip install -r requirements.txt

3. RUN FLASK APPLICATION

cd flask
python app.py

4. OPEN IN BROWSER

http://127.0.0.1:5000

--------------------------------------------------------------------

REQUIREMENTS.TXT CONTENT
------------------------
flask
numpy
pandas
scikit-learn
matplotlib
seaborn
joblib

--------------------------------------------------------------------

KEY LEARNINGS
-------------
- Handling highly imbalanced datasets
- Avoiding data leakage in machine learning projects
- Importance of probability-based decision making
- End-to-end ML deployment using Flask
- Understanding differences between Decision Trees and Random Forests

--------------------------------------------------------------------

CONCLUSION
----------
This project demonstrates a complete machine learning pipeline, from data
preprocessing and model training to real-time fraud detection using a Flask
web application.

It is suitable for academic submission, portfolio projects, and ML
demonstrations.

--------------------------------------------------------------------

AUTHOR
------
Online Payment Fraud Detection System
Developed as part of Machine Learning and Flask deployment practice.
HemanthGHY
