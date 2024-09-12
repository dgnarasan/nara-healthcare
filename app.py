from flask import Flask, request, jsonify
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the dataset (CSV) at the start
df = pd.read_csv('common_diseases_dataset.csv')

# A simple route to handle disease prediction based on symptoms
@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    data = request.get_json()
    symptoms = data.get('symptoms').lower()

    # Simple search based on symptoms in the dataset
    matched_diseases = df[df['Symptoms'].str.contains(symptoms, case=False, na=False)]

    if not matched_diseases.empty:
        result = matched_diseases[['Disease Name', 'Severity', 'Immediate Fast Response Treatment']].to_dict(orient='records')
        return jsonify({'predicted_diseases': result})
    else:
        return jsonify({'error': 'No matching disease found'}), 404

if __name__ == "__main__":
    app.run(debug=True)
