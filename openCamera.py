import cv2
import mediapipe as mp

# Initialisiere die MediaPipe Hands Komponente
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if frame is not None:
        frame = cv2.flip(frame, 1)

        # Konvertiere das Bild in RGB, da mediapipe Bilder in RGB erwartet
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Verarbeite das Bild und finde die Handlandmarken
        results = hands.process(rgb_image)

        # Zeichne die Handlandmarken auf das Bild
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

                # detect finger
                finger_up = [False] * 5
                if hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mpHands.HandLandmark.THUMB_MCP].x:
                    finger_up[0] = True
                if hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_MCP].y:
                    finger_up[1] = True
                if hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP].y:
                    finger_up[2] = True
                if hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_MCP].y:
                    finger_up[3] = True
                if hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mpHands.HandLandmark.PINKY_MCP].y:
                    finger_up[4] = True

                # Erkenne die Geste
                gesture = ""
                if finger_up.count(True) == 0:
                    gesture = "Stein"
                elif finger_up.count(True) == 2 and finger_up[1] and finger_up[4]:
                    gesture = "Rock 'n' Roll"
                elif finger_up.count(True) == 2 and finger_up[1] and finger_up[2]:
                    gesture = "Peace"

                # Zeige die erkannte Geste in der oberen linken Ecke des Bildes
                cv2.putText(frame, gesture, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 2)

        # Zeige das Bild an
        cv2.imshow('Camera', frame)

    # Warte auf die Tasteneingabe 'q', um die Schleife zu beenden
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()