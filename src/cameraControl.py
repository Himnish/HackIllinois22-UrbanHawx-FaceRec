from platform import python_branch
from tkinter import pic
import numpy as np
import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 360)
cam.set(4, 480)

while True:
    rect, pic = cam.read()
    gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', pic)
    cv2.imshow('gray', gray)

    k = cv2.waitKey(20)
    if k == 27:  # 'ESC' to quit
        break

cam.release()
cv2.destroyAllWindows()
