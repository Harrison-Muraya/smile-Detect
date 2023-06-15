import cv2
import mediapipe as mp
import time

cap = cv2.VidoeCapture(1)
while True:
    success, img =cap.read()

    cv2.imshow("image", img)
    cv2.waitKey(1)

print("code complete")