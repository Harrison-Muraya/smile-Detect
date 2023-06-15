import cv2

#face classfier
f_detec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detec = cv2.CascadeClassifier('haarcascade_smile.xml')

webcam = cv2.VideoCapture(0)
while(True):
    successful_frame_read, frame = webcam.read()
     
    if not successful_frame_read:
        break
    frame_gryscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces =f_detec.detectMultiScale(frame_gryscale)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x, y), (x+w, y+h),(100, 200, 50),4)
        the_face = frame[y:y+h, x:x+w]
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        smiles = smile_detec.detectMultiScale(face_grayscale, scaleFactor=1.7,minNeighbors=20)

        if len(smiles)>0:
            cv2.putText(frame, 'smiling', (x, y+h+40),fontScale=3, fontFace = cv2.FONT_HERSHEY_PLAIN, color =(255, 255, 255))

    cv2.imshow('smile detector',frame)

    cv2.waitKey(1)

webcam.release()
cv2.destroyAallWindows()


print("complet")