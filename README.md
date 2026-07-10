# 🚗 Driver Drowsiness Detection System

A real-time Driver Drowsiness Detection System developed using **Python**, **OpenCV**, **Dlib**, and **Pygame**. The application monitors the driver's eyes through a webcam and detects signs of drowsiness using the **Eye Aspect Ratio (EAR)** technique. When drowsiness is detected, the system triggers an alarm to alert the driver and help prevent accidents.

---

## 📌 Features

- 👁️ Real-time face and eye detection
- 📷 Webcam-based monitoring
- 🧠 Eye Aspect Ratio (EAR) based drowsiness detection
- 🔔 Alarm sound when drowsiness is detected
- 📊 Event logging for drowsiness alerts
- ⚡ Real-time video processing

---

## 🛠️ Technologies Used

- Python
- OpenCV
- Dlib
- SciPy
- Imutils
- Pygame
- NumPy

---

## 📁 Project Structure

```
Driver-Drowsiness-Detection/
│
├── app.py
├── drowsiness_detector.py
├── utils.py
├── alarm.wav
├── shape_predictor_68_face_landmarks.dat
├── drowsiness_log.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Driver-Drowsiness-Detection.git
cd Driver-Drowsiness-Detection
```

### 2. Install required libraries

```bash
pip install -r requirements.txt
```

### 3. Download the facial landmark model

Download:

`shape_predictor_68_face_landmarks.dat`

Place the file inside the project folder.

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 📖 How It Works

1. The webcam captures live video frames.
2. The system detects the driver's face.
3. Facial landmarks are identified using Dlib.
4. The Eye Aspect Ratio (EAR) is calculated continuously.
5. If the EAR remains below the threshold for several consecutive frames, the system identifies the driver as drowsy.
6. An alarm sound is played, and the event is logged.

---

## 📷 Output

- Live webcam feed
- Eye detection with facial landmarks
- Drowsiness alert message
- Alarm notification
- Event logging

---

## 🎯 Future Enhancements

- Yawn detection
- Head pose estimation
- Mobile camera support
- Web dashboard
- Cloud-based alert logging
- Deep learning-based fatigue detection

---

## 👩‍💻 Author

**Kalaipriya**

Final Year B.E. Computer Science and Engineering

```

### Before uploading to GitHub:
- Replace `your-username` in the GitHub link with your actual GitHub username.
- If your current project is the Haar Cascade version (not the EAR version), I can also provide a README specifically for that version.
