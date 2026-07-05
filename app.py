from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from ocr import extract_data
from calculator import calculate
from scorer import score

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return {
        "message": "RideIQ Backend Running 🚗"
    }


@app.route("/analyze", methods=["POST"])
def analyze():

    if "image" not in request.files:
        return jsonify({
            "success": False,
            "message": "No image uploaded."
        }), 400

    image = request.files["image"]

    filepath = os.path.join(UPLOAD_FOLDER, image.filename)

    image.save(filepath)

    ocr_data = extract_data(filepath)

    if (
        ocr_data["fare"] is None or
        ocr_data["pickup"] is None or
        ocr_data["trip"] is None
    ):
        return jsonify({
            "success": False,
            "message": "OCR could not extract all ride information.",
            "ocr": ocr_data
        }), 400

    result = calculate(
        ocr_data["fare"],
        ocr_data["pickup"],
        ocr_data["trip"]
    )

    result = score(result)

    return jsonify({
        "success": True,
        "ocr": ocr_data,
        "analysis": result
    })


if __name__ == "__main__":
    app.run(debug=True)