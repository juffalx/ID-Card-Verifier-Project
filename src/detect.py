# from ultralytics import YOLO
# import cv2
# from cvzone.Utils import putTextRect

# # Load trained model
# model = YOLO("models/best.pt")

# # Load image
# image_path = "images/test1.jpg"
# image = cv2.imread(image_path)

# if image is None:
#     raise FileNotFoundError(f"❌ Image not found at {image_path}")

# # Run detection
# results = model.predict(source=image, imgsz=640, conf=0.25, device=0, verbose=False)
# boxes = results[0].boxes

# print(f"📦 Total Detections: {len(boxes)}")

# if len(boxes) == 0:
#     print("⚠️ No ID cards detected!")
# else:
#     for box in boxes:
#         # Get box data
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         conf = float(box.conf[0])
#         label = f"ID Card: {conf:.2%}"

#         print(f"🟩 Box: ({x1}, {y1}), ({x2}, {y2}) | Confidence: {conf:.2f}")

#         # Draw bounding box
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 165, 255), 2)
#         putTextRect(image, label, (x1, y1 - 10), scale=1, thickness=1,
#                     colorR=(255, 0, 0), colorT=(255, 255, 255))

# # Save and show result
# output_path = "images/annotated.jpg"
# cv2.imwrite(output_path, image)
# cv2.imshow("Annotated Detection", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



from ultralytics import YOLO
import cv2

# Load your trained model (update path to your best.pt)
model = YOLO("models/best.pt")

# Load image
image_path = "images/test.jpg"
img = cv2.imread(image_path)

# Run detection
results = model.predict(source=img, imgsz=640, conf=0.3, device=0, verbose=False)

# Get detections
boxes = results[0].boxes

# Check if any ID card detected
if boxes:
    print("✅ ID card detected!")
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        print(f"📦 Confidence: {conf:.2f}")

        # Draw rectangle and confidence
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"ID Card: {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

else:
    print("⚠️ No ID card detected!")

# Show the result
cv2.imshow("Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()