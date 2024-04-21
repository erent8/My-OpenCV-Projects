import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Renk aralıklarını tanımlar
color_ranges = {
    'Kirmizi': ([0, 120, 70], [10, 255, 255]),
    'Turuncu': ([10, 100, 100], [20, 255, 255]),
    'Sari': ([20, 100, 100], [30, 255, 255]),
    'Yesil': ([50, 50, 50], [70, 255, 255]),
    'Mavi': ([110, 50, 50], [130, 255, 255]),
    'Koyu Mavi': ([130, 50, 50], [150, 255, 255]),
    'Mor': ([130, 50, 50], [160, 255, 255]),
    'Pembe': ([160, 100, 100], [170, 255, 255]),
    'Beyaz': ([0, 0, 200], [180, 20, 255]),
    'Gri/Siyah': ([0, 0, 0], [180, 50, 120])
    # Diğer renk aralıkları eklenebilir...
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(hsv, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 200:  # Min alan kriteri
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
                cv2.putText(frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
