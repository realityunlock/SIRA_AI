from flask import Flask, render_template, request
from modules.text_ai import analyze_text_threat
from modules.image_ai import analyze_image_threat
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "text":
            user_text = request.form.get("text_input", "")
            result = analyze_text_threat(user_text)

        elif action == "image":
            if "file" not in request.files:
                result = "No file uploaded."
            else:
                file = request.files["file"]
                if file.filename == "":
                    result = "No selected file."
                else:
                    # Ajiye temporary image
                    filepath = os.path.join("temp.jpg")
                    file.save(filepath)
                    result = analyze_image_threat(filepath)
                    os.remove(filepath)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)