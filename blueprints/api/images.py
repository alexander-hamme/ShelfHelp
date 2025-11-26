from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os

images = Blueprint("images", __name__, url_prefix="/api/images")

@images.route("/upload", methods=["POST"])
def upload_image():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    filename = secure_filename(file.filename)
    saved_path = os.path.join("uploads", filename)
    file.save(saved_path)

    # Call your ML model here later
    detections = detect_ingredients_from_image(saved_path)

    return jsonify({"detections": detections})