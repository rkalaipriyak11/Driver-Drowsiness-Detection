import cv2
import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

alarm_on = False
eye_closed_start = None   # ⏱️ timer

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes_detected = False

    for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    roi_gray = gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)

    if len(eyes) > 0:
        eyes_detected = True

    # ✅ TIMER LOGIC
    if not eyes_detected:
        if eye_closed_start is None:
            eye_closed_start = time.time()

        elapsed = time.time() - eye_closed_start

        if elapsed > 2:  # ⏱️ 2 seconds threshold
            if not alarm_on:
                pygame.mixer.music.play(-1)
                alarm_on = True
    else:
        eye_closed_start = None
        if alarm_on:
            pygame.mixer.music.stop()
            alarm_on = False
    status = "Eyes Open" if eyes_detected else "Eyes Closed"
    cv2.putText(frame, status, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if alarm_on:
        cv2.putText(frame, "DROWSY ALERT!", (100, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)


    cv2.imshow("Driver Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()