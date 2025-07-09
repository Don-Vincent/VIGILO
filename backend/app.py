from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from feature_extractor import extract_features
import numpy as np
import os

app = Flask(__name__)
model = load_model("model/model_02.h5")

@app.route("/predict", methods=["POST"])
def predict():
    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["audio"]
    file_path = os.path.join("temp.wav")
    file.save(file_path)

    features = extract_features(file_path)
    if isinstance(features, dict) and "error" in features:
        return jsonify(features), 400

    input_data = np.array(features).reshape(1, -1, 1)
    prediction = np.argmax(model.predict(input_data), axis=1)[0]

    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
