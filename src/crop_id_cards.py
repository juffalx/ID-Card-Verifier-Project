from ultralytics import YOLO
import cv2
import os

# Load model
model = YOLO("models/best.pt")

# Input/output folders
input_folder = "images"
output_folder = "cropped"
os.makedirs(output_folder, exist_ok=True)

# Loop through all images in folder
for image_name in os.listdir(input_folder):
    if not image_name.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    image_path = os.path.join(input_folder, image_name)
    img = cv2.imread(image_path)

    results = model.predict(source=img, imgsz=640, conf=0.3, device=0, verbose=False)
    boxes = results[0].boxes

    if boxes:
        print(f"\n✅ {image_name} - {len(boxes)} ID Card(s) detected")

        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            crop = img[y1:y2, x1:x2]

            crop_name = f"{image_name.split('.')[0]}_IDCard_{i+1}_conf_{conf:.2f}.jpg"
            crop_path = os.path.join(output_folder, crop_name)
            cv2.imwrite(crop_path, crop)
            print(f"💾 Saved: {crop_path}")

    else:
        print(f"⚠️ No ID card detected in {image_name}")
