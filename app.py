from flask import Flask, request, jsonify

app = Flask(__name__)

# Function that maps symptoms to a disease (replace with your logic)
def predict_from_symptoms(symptoms):
    # This is where you'll implement your logic to predict disease from symptoms
    # You can use your dataset to make predictions here.
    if "fever" in symptoms and "chills" in symptoms:
        return "Flu"
    else:
        return "Unknown Disease"

# Define the route for predicting disease
@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    data = request.get_json()  # Extract JSON data from the request
    symptoms = data.get('symptoms')  # Get the 'symptoms' key from the JSON

    if symptoms:
        disease = predict_from_symptoms(symptoms)
        return jsonify({"disease": disease})  # Return the predicted disease in JSON
    else:
        return jsonify({"error": "No symptoms provided"}), 400  # Error handling for missing symptoms

if __name__ == '__main__':
    app.run(debug=True)
