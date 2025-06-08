import cv2
from ultralytics import YOLO

# Load your trained YOLOv8 model
model = YOLO("models/best.pt")

# Class name (replace with yours if different)
CLASS_NAME = "ID Card"

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot access webcam")
    exit()

print("📷 Real-time ID Card Detection started... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model.predict(source=frame, imgsz=640, conf=0.25, device=0, verbose=False)
    detections = results[0].boxes

    # Draw detections manually
    for box in detections:
        # Get coordinates and confidence
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        label = f"{CLASS_NAME}: {conf:.2%}"

        # Draw bounding box and label
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    if len(detections) == 0:
        cv2.putText(frame, "No ID Card Detected", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display result
    cv2.imshow("ID Card Detector (Press 'q' to exit)", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
