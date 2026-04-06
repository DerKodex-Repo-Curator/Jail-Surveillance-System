import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print("Restricted Zone Line Detection: ONLINE")

while True:
    ret, frame = cap.read()
    if not ret: break

    # 1. Smooth the image to reduce noise
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    # 2. Yellow Color Range (Standard for 'Caution' lines)
    lower_yellow = np.array([18, 94, 140])
    upper_yellow = np.array([48, 255, 255])
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # 3. Detect Edges and Lines
    edges = cv2.Canny(mask, 74, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=50, maxLineGap=50)
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # Draw Green lines over detected yellow floor markings
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            cv2.putText(frame, "BOUNDARY DETECTED", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow("Security Boundary Analysis", frame)
    
    if cv2.waitKey(25) & 0xFF == 27: # Press ESC to quit
        break

cap.release()
cv2.destroyAllWindows()