# Save this in a file, e.g., app.py
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load('batting_runs_model.pkl')

@app.route('/')

@app.route('/predictRuns', methods=['POST'])


def index():
    return "Hello world"
def predictRuns():
    # Get input data from request
    data = request.get_json()
    X_new = data['input']  # input should be a 2D array

    # Make prediction
    prediction = model.predict([X_new])

    # Return the prediction as a response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
