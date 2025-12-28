import cv2
import time
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Window settings
cv2.namedWindow("AI Object Detection & Tracking", cv2.WINDOW_NORMAL)

prev_time = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # YOLO detection + tracking
    results = model.track(frame, persist=True)
    annotated_frame = results[0].plot()

    # FPS calculation
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time)) if prev_time != 0 else 0
    prev_time = curr_time

    # Dark overlay for text
    overlay = annotated_frame.copy()
    cv2.rectangle(overlay, (0, 0), (320, 90), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.6, annotated_frame, 0.4, 0, annotated_frame)

    # Display text
    cv2.putText(annotated_frame, "AI Object Detection & Tracking",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.putText(annotated_frame, f"FPS: {fps}",
                (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("AI Object Detection & Tracking", annotated_frame)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
