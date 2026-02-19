from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/predict')
def predict_page():
    return render_template("predict.html")

@app.route("/pred", methods=["POST"])
def predict():
    try:
        step = int(request.form["step"])
        tx_type = request.form["type"]
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])

        type_encoder = pickle.load(open("./models/type_encoder.pkl", "rb"))
        encoded_type = type_encoder.transform([tx_type])[0]
        amount = np.log(amount + 1)

        df = pd.DataFrame([[
            step,
            encoded_type,
            amount,
            oldbalanceOrg,
            newbalanceOrig,
            oldbalanceDest,
            newbalanceDest
        ]], columns=[
            "step",
            "type",
            "amount",
            "oldbalanceOrg",
            "newbalanceOrig",
            "oldbalanceDest",
            "newbalanceDest"
        ])

        model = pickle.load(open("./models/fraud_model.pkl", "rb"))
        proba = model.predict_proba(df)[0]

        fraud_index = list(model.classes_).index(1)
        fraud_prob = proba[fraud_index]

        prediction = "Fraud" if fraud_prob >= 0.5 else "Not Fraud"

        rfc = pickle.load(open("./models/fraud_rfc.pkl", "rb"))
        proba_rfc = rfc.predict_proba(df)[0]
        fraud_index_rfc = list(rfc.classes_).index(1)
        fraud_prob_rfc = proba_rfc[fraud_index_rfc]
        print("==== DEBUG ====")
        print("RFC Prediction:", rfc.predict(df))
        print("RFC Probabilities:", rfc.predict_proba(df))
        
        print(df)   
        print("Prediction:", model.predict(df))
        print("Probabilities:", model.predict_proba(df))
        print("================")
        
        return render_template(
            "result.html",
            prediction=prediction,
            probability=round(fraud_prob * 100, 2)
        )

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)