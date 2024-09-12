from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Existing code
@app.route('/')
def home():
    return "Welcome to the Nara Healthcare Bot! Use the /predict_disease endpoint."

# Function to map symptoms to diseases (using a simple logic for now)
def predict_from_symptoms(symptoms):
    # Simple logic to predict disease from symptoms, to be replaced by real model logic
    if "fever" in symptoms and "chills" in symptoms:
        return "Flu"
    elif "itchy" in symptoms and "sneezing" in symptoms:
        return "Allergies"
    else:
        return "Unknown Disease"

# New route for predicting diseases
@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    # Get JSON data from request
    data = request.get_json()
    symptoms = data.get('symptoms')
    
    # Check if symptoms are provided
    if symptoms:
        disease = predict_from_symptoms(symptoms)
        return jsonify({"disease": disease})
    else:
        return jsonify({"error": "No symptoms provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)



