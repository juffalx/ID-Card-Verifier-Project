import easyocr
import cv2
import os

# Initialize EasyOCR Reader (English only for now)
reader = easyocr.Reader(['en'])

cropped_folder = "../cropped"
images = [f for f in os.listdir(cropped_folder) if f.endswith((".jpg", ".png"))]

for img_name in images:
    img_path = os.path.join(cropped_folder, img_name)
    image = cv2.imread(img_path)

    # Run OCR
    result = reader.readtext(image)

    # Combine text results
    text = "\n".join([res[1] for res in result])

    print(f"\n🆔 OCR Result for: {img_name}")
    print("--------------------------------------------------")
    print(text)
    print("--------------------------------------------------")

    # Save text
    txt_name = img_name.rsplit('.', 1)[0] + ".txt"
    txt_path = os.path.join(cropped_folder, txt_name)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
        print(f"💾 Saved OCR text: {txt_path}")
