from flask import Flask, render_template, request
import os
from auto_ocr_verify import auto_verify_from_image  # your OCR + verify function

app = Flask(__name__)
UPLOAD_FOLDER = '../cropped'  # relative to src folder, adjust if needed
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Save uploaded file
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)
            
            # Verify using your existing function
            result = auto_verify_from_image(image_path)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
