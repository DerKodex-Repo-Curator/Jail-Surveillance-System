import numpy as np 
import cv2 
import pyautogui # Use this just to get the screen size automatically
from PIL import ImageGrab

# 1. Automatically detect YOUR screen resolution
width, height = pyautogui.size()
resolution = (width, height)

# 2. Setup the Video Writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# We'll save it as 'shift_log.avi' to stay with the Jail theme
out = cv2.VideoWriter("shift_log.avi", fourcc, 8.0, resolution)

print(f"Recording System Active at {width}x{height}...")

while True:
    # 3. Grab the screen
    img = ImageGrab.grab()
    img_np = np.array(img)

    # 4. Correct the Color (Screen is RGB, OpenCV VideoWriter wants BGR)
    frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # 5. Write to file
    out.write(frame)

    # 6. Exit logic (using 'q' to match your other scripts)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
out.release()
cv2.destroyAllWindows()
print("Log saved to shift_log.avi")