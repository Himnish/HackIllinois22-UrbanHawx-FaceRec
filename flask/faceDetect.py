import numpy as np
import cv2

def facedetection():
        
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
    eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
    smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')

    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        rect, pic = cam.read()
        gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray, #input grayscale image
            scaleFactor = 1.3, # how much the image is reduced in size by
            minNeighbors = 5, # higher number means lower false +ves
            minSize = (30, 30) # minimum rectangle size for a face
        )

        for (x, y, w, h) in faces: # (x,y) -> top left corner coordinate, w -> width, h -> height
            cv2.rectangle(pic, (x, y), (x+w, y+h), (255, 0, 0), 2)
            img_g = gray[y:y+h, x:x+w]
            img_c = pic[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(
            img_g,
            scaleFactor = 1.5,
            minNeighbors = 5,
            minSize = (5, 5),
            )
        
        for (x_e, y_e, w_e, h_e) in eyes:
            cv2.rectangle(img_c, (x_e, y_e), (x_e + w_e, y_e + h_e), (0, 255, 0), 2)
        
        smile = smileCascade.detectMultiScale(
            img_g,
            scaleFactor = 1.5,
            minNeighbors = 15,
            minSize = (25, 25),
            )
        for (x_s, y_s, w_s, h_s) in smile:
            cv2.rectangle(img_c, (x_s, y_s), (x_s + w_s, y_s + h_s), (0, 255, 0), 2)
            
        cv2.imshow('video', pic)

        k = cv2.waitKey(20)
        if k == 27:  # 'ESC' to quit
            break

    cam.release()
    cv2.destroyAllWindows()
