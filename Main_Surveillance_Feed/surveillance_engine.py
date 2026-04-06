import cv2
import os

# 1. Setup Camera and Baseline
cap = cv2.VideoCapture(0)
first_frame = None
sample_taken = False 

print("Main Surveillance Feed: SYSTEM LIVE")

while True:
    ret, frame = cap.read()
    if not ret: break

    # Prepare image for motion detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    # 2. Detect the Difference (Motion)
    delta = cv2.absdiff(first_frame, gray)
    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000: # Sensitivity: Ignore small movements
            continue
        
        # 3. Motion Found! Draw Box
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "MOTION DETECTED", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 4. AUTO-SAVE LOGIC (Your logic hybridized)
        if not sample_taken:
            filename = "motion_incident_1.jpg"
            # Save the specific crop where motion happened
            cv2.imwrite(filename, frame[y:y+h, x:x+w])
            print(f"Alert! Evidence saved to {filename}")
            sample_taken = True # Only take one photo per session

    cv2.imshow("Jail Main Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or sample_taken:
        # We can choose to break after 1 photo like your code did
        print("Surveillance trigger complete. System standby.")
        break

cap.release()
cv2.destroyAllWindows()