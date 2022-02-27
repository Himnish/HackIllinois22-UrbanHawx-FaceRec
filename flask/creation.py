import cv2, numpy, sys, os

import training
datasets = 'datasets'


#user = input('\nEnter your name and press <return> ==>')
#face_id = input('\n enter user id end press <return> ==>  ')
user = input("\nEnter name")

face_id = training.send_size()
training.receive(user)



#path_face = os.path.join(datasets,user)
#path_smile = os.path.join(datasets,user,'smile')
#path_eye = os.path.join(datasets,user,'eye')

#os.mkdir(path_face)
#os.mkdir(path_smile)
#os.mkdir(path_eye)

cam = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)                                                                           
count = 0

while count <= 300:
    rect, pic = cam.read()
    pic = cv2.flip(pic,1)
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
        cv2.imwrite("datasets/User." + str(face_id) + '.' + str(count) + ".jpg",img_g)
    
    cv2.imshow('video', pic)
    count = count + 1
    k = cv2.waitKey(20)
    if k == 27:  # 'ESC' to quit
        break

cam.release()
cv2.destroyAllWindows()


