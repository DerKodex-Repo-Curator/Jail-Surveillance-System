import cv2
import pytesseract
import numpy as np

# 1. THE HANDSHAKE: Tell Python exactly where the engine is
# The 'r' before the string is CRITICAL for Windows paths
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)

print("--- JAIL IDENTITY VERIFICATION SYSTEM ---")
print("Instructions: Hold Inmate ID clearly in front of camera.")
print("Press 'q' to shut down system.")

while True:
    ret, frame = cap.read()
    if not ret: break

    # 2. IMAGE PRE-PROCESSING (Crucial for OCR accuracy)
    # Convert to gray and use Thresholding to make text black/white
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # We use Otsu's thresholding to automatically find the best contrast
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 3. OCR EXECUTION
    # We tell Tesseract to look for digits/text in a single block (--psm 6)
    try:
        raw_data = pytesseract.image_to_string(thresh, config='--psm 6')
        
        # Clean the text: Remove extra spaces and newlines
        clean_text = raw_data.strip()

        if len(clean_text) > 0:
            # Theme: Identification Box
            cv2.rectangle(frame, (10, 10), (350, 80), (0, 0, 0), -1) # Black background for text
            cv2.putText(frame, f"READING: {clean_text[:15]}", (20, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    except Exception as e:
        print(f"OCR Error: {e}")

    # 4. DISPLAY THE FEEDS
    cv2.imshow("Security Monitor - ID Verification", frame)
    # This helps you see if the lighting is good enough for the AI
    cv2.imshow("AI Vision (Threshold)", thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()