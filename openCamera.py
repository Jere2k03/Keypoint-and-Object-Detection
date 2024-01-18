import torch
import torchvision
import cv2

cap = cv2.VideoCapture(0)

while True:
    # Lies ein Frame von der Kamera
    ret, frame = cap.read()

    if frame is not None:
        # spiegel das Frame
        frame = cv2.flip(frame, 1)
        
        # Zeige das Frame an
        cv2.imshow('Camera', frame)

    # Warte auf die Tasteneingabe 'q', um die Schleife zu beenden
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Gib die Kameraressourcen frei
cap.release()
cv2.destroyAllWindows()
