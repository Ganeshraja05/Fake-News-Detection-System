from flask import Flask, request, jsonify
import joblib
from preprocess import clean_text
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the trained model and vectorizer
MODEL_PATH = "../models/model.pkl"
VECTORIZER_PATH = "../models/vectorizer.pkl"

print("Loading model and vectorizer...")
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
print("Model and vectorizer loaded.")

@app.route("/")
def home():
    return jsonify({"message": "Fake News Detection System Backend is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the input text from the request
        data = request.get_json()
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "Empty text input"}), 400

        # Preprocess and vectorize the input text
        cleaned_text = clean_text(text)
        vectorized_text = vectorizer.transform([cleaned_text]).toarray()

        # Make the prediction
        prediction = model.predict(vectorized_text)[0]
        confidence = model.predict_proba(vectorized_text).max()

        # Convert prediction to label
        result = "Fake News" if prediction == 1 else "Real News"

        return jsonify({
            "result": result,
            "confidence": f"{confidence * 100:.2f}"
        })
    except Exception as e:
        print("Error during prediction:", str(e))
        return jsonify({"error": "An error occurred during prediction"}), 500

if __name__ == "__main__":
    app.run(debug=True)
