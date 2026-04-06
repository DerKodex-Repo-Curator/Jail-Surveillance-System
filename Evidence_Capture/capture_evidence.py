import numpy as np
import cv2
import pyautogui
import time # To add timestamps to filenames

print("--- EVIDENCE CAPTURE SYSTEM ---")
print("Press 's' to save a screenshot, or 'q' to quit.")

# Start the camera feed (Optional: So you can see what you're capturing)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    cv2.imshow("Surveillance Monitoring", frame)
    
    key = cv2.waitKey(1) & 0xFF

    # If 's' is pressed, capture the ENTIRE SCREEN as evidence
    if key == ord('s'):
        # 1. Take screenshot
        image = pyautogui.screenshot()

        # 2. Convert PIL/RGB to Numpy/BGR (Your logic)
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # 3. Create a unique filename based on the current time
        # Format: evidence_YYYYMMDD_HHMMSS.png
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"incident_{timestamp}.png"

        # 4. Write to disk
        cv2.imwrite(filename, image_cv)
        print(f"[!] EVIDENCE SAVED: {filename}")

    # Exit the system
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()