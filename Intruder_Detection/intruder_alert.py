import cv2
import os

# 1. Load the body detector (Make sure this XML is in your folder!)
detector = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# 2. Use the Webcam for live surveillance
cap = cv2.VideoCapture(0)
sample_id = 0 # To give each saved image a unique name

print("Surveillance System Active. Scanning for Intruders...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 3. Detect full bodies
    bodies = detector.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in bodies:
        # Draw the rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, "INTRUDER ALERT", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        # 4. EVIDENCE CAPTURE: Save the cropped intruder image
        # We only save one frame every time we detect something to avoid crashing
        if sample_id < 10: # Limits it to 10 photos so your PC doesn't lag
            crop_path = f"intruder_{sample_id}.jpg"
            cv2.imwrite(crop_path, frame[y:y+h, x:x+w])
            print(f"Evidence Saved: {crop_path}")
            sample_id += 1

    # Show the live feed
    cv2.imshow('Jail Surveillance - Restricted Zone', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()