import cv2
import threading
import pygame
import time

# Load Haar Cascade files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

alarm_on = False


# Alarm function
def play_alarm():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("alarm.wav")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    except Exception as e:
        print("Sound Error:", e)


# Main function
def detect_drowsiness():
    global alarm_on

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Camera warm-up
    time.sleep(2)

    if not cap.isOpened():
        print("Cannot access camera")
        return

    eye_closed_frames = 0
    threshold = 20

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            face = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(face)

            # Eyes closed
            if len(eyes) == 0:
                eye_closed_frames += 1

            else:
                eye_closed_frames = 0
                alarm_on = False

            # Alert condition
            if eye_closed_frames > threshold:

                cv2.putText(
                    frame,
                    "DROWSINESS ALERT!",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

                if not alarm_on:
                    alarm_on = True

                    threading.Thread(
                        target=play_alarm,
                        daemon=True
                    ).start()

        cv2.imshow("Driver Drowsiness Detection", frame)

        # Press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()