from ultralytics import YOLO
import cv2
import os

# Load trained model
model = YOLO("models/best.pt")

# Load test image
image_path = "images/test1.jpg"
results = model(image_path, save=True)

# Save result image
save_dir = results[0].save_dir
print(f"✅ Detection complete! Image saved in: {save_dir}")
