from flask import Flask, request, jsonify
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained models and symptom encoder
model_disease = joblib.load('model_disease.pkl')
model_severity = joblib.load('model_severity.pkl')
model_treatment = joblib.load('model_treatment.pkl')
mlb = joblib.load('mlb.pkl')  # Load the symptom encoder

@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    data = request.get_json()
    symptoms = data.get('symptoms')

    # Preprocess the symptoms input using the encoder
    symptoms_encoded = mlb.transform([symptoms])

    # Predict the disease, severity, and treatment
    predicted_disease = model_disease.predict(symptoms_encoded)
    predicted_severity = model_severity.predict(symptoms_encoded)
    predicted_treatment = model_treatment.predict(symptoms_encoded)

    # Prepare the response
    response = {
        'disease': predicted_disease[0],
        'severity': predicted_severity[0],
        'treatment': predicted_treatment[0]
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)




