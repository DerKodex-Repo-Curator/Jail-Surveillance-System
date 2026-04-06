# 🚨 Jail Surveillance System (OpenCV)

A comprehensive, multi-module security suite designed for automated monitoring and digital logging within correctional facilities. This project leverages **Computer Vision** and **Machine Learning** to automate inmate tracking, intruder detection, and real-time evidence capture.

## 🛠 Features

The system is divided into 8 specialized security modules:

### 👤 Inmate Management
* **Inmate Identification:** Real-time face and eye detection using Haar Cascades to monitor subject presence.
* **Identity Verification:** A biometric-style scanner using **Tesseract OCR** to read and verify Inmate ID numbers from physical cards.

### 🛡 Perimeter & Zone Control
* **Intruder Detection:** Scans for full human silhouettes in restricted hallways using HOG descriptors.
* **Restricted Zone Analysis:** A "Virtual Fence" system that triggers an alarm if a boundary (detected via Hough Line Transform) is crossed.
* **Perimeter Monitoring:** Target "lock-on" and tracking using **HSV Color Masking** (optimized for inmate uniforms).

### 📹 Evidence & Logging
* **Main Surveillance Feed:** A background-subtraction engine that triggers automated image capture upon detecting motion.
* **Control Room Log:** Background screen recording to document guard activity and monitor feeds during shifts.
* **Evidence Capture:** Manual "Panic Button" for high-resolution snapshots with automated timestamps for incident reporting.

---

## 🚀 Tech Stack

**Python | OpenCV | NumPy | Tesseract OCR | PyAutoGUI | Pillow | Git**

---

## 🏗 Project Structure

- `Control_Room_Log/` - Background screen recording and logging.
- `Evidence_Capture/` - On-demand incident snapshots with timestamps.
- `Identity_Verification/` - OCR-based text and ID recognition.
- `Inmate_Identification/` - Biometric face and eye monitoring.
- `Intruder_Detection/` - Human silhouette detection in restricted areas.
- `Main_Surveillance_Feed/` - Motion-triggered automated security engine.
- `Perimeter_Monitoring/` - Object tracking via color isolation.
- `Restricted_Zone_Analysis/` - Boundary breach detection using line transforms.

---

## ⚖ License
Distributed under the **MIT License**.
