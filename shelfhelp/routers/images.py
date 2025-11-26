from fastapi import APIRouter, File, UploadFile
from shelfhelp.models.ingredient import IngredientMatch

router = APIRouter()

@router.post("/upload", response_model=list[IngredientMatch])
async def upload_image(image: UploadFile = File(...)):
    contents = await image.read()
    # ML model inference
    return await detect_ingredients(contents)


'''
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

    return jsonify({"detections": detections})'''