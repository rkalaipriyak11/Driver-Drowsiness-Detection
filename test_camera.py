import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# allow camera to warm up
time.sleep(2)

if not cap.isOpened():
    print("❌ Cannot access camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        continue   # 🔥 don't break, retry

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()