from PIL import Image
import numpy as np

def analyze_image_threat(image_path):
    # Check if the file name contains threat-related keywords
    file_name = image_path.lower()
    keywords = ["gun", "bomb", "explosive", "weapon", "knife"]

    if any(word in file_name for word in keywords):
        return f"⚠️ Threat detected based on filename: {file_name}"
    
    # Basic pixel intensity check (optional - can be improved)
    try:
        img = Image.open(image_path).convert("L")  # Convert to grayscale
        data = np.array(img)
        mean_pixel = np.mean(data)

        if mean_pixel < 50:
            return "❗ Warning: Image may contain dark or threatening content."
        else:
            return "✅ Image appears to be safe."
    except Exception as e:
        return f"❌ Error while analyzing image: {str(e)}"