
# import cv2, sys, os
# import numpy as np
# size = 4
# datasets = 'datasets'


# (images, labels, names, id) = ([], [], {}, 0)
# for (subdirs, dirs, files) in os.walk(datasets):
#     for subdir in dirs:
#         names[id] = subdir
#         subjectpath = os.path.join(datasets, subdir)
#         for filename in os.listdir(subjectpath):
#             path = subjectpath + '/' + filename
#             label = id
#             images.append(cv2.imread(path, 0))
#             labels.append(int(label))
#         id += 1
# (width, height) = (130, 100)
 
# # Create a Numpy array from the two lists above
# (images, labels) = [np.array(lis) for lis in [images, labels]]
 

# # (photos, tags, names, id) = ([], [], {}, 0) #assignment 

# # for (sub, directory, files) in os.walk(datasets):
# #     for s in directory:
# #         names[id] = s #list of names
# #         subjectpath = os.path.join(datasets, s)
# #         for filename in os.listdir(subjectpath):
# #             path = subjectpath + '/' + filename
# #             label = id
# #             photos.append(cv2.imread(path, 0))
# #             tags.append(int(label))
# #         id += 1
# # (width, height) = (130, 100)

# # # print(len(photos))
# # # # print("-----")
# # # print(len(tags))

# # (photo,ta) = [np.array(lis, dtype=object) for lis in [photos,tags]] # array of pictures and tags
 
# # OpenCV trains a model from the images

# # model = cv2.face.LBPHFaceRecognizer_create()
# # model.train(photo, ta)

# # pic = '/Users/drs/Desktop/BackIllinois/HackIllinois22-FaceRec/datasets/Himnish/2.png'

# # def confid(pic):
# #     confidence = model.predict(pic)
# #     print (confidence[0])
# #     return confidence

# # a = confid(pic)


import cv2
import numpy as np
from PIL import Image
import os

# Path for face image database
path = 'datasets'

recognizer = cv2.face.LBPHFaceRecognizer_create()
#detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids


print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
#recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))



cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter


# names related to ids: example ==> Marcelo: id=1,  etc
#names = ['None', 'Ribhav', 'Ribhav', 'Ribhav', 'Kushal','Kushal', 'Kushal', 'Himnish', 'Himnish', 'Himnish']
names = ['None', 'Ribhav', 'Kushal', 'Himnish']
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
# minW = 0.1*cam.get(3)
# minH = 0.1*cam.get(4)

while True:
    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = detector.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        print (id)

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 50):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(40) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()