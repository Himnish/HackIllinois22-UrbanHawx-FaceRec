import cv2, numpy, sys, os

size = 5
datasets = 'datasets'

(images, tags, names, id) = ([], [], {}, 0) #assignment 

for (sub, directory, files) in os.walk(datasets):
    for s in directory:
        names[id] = s #list of names
        subjectpath = os.path.join(datasets, s)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            photos.append(cv2.imread(path, 0))
            tags.append(int(label))
        id += 1
(width, height) = (130, 100)

for lis in [photos, tags]:
    (photos, tags) = numpy.array(lis) # array of pictures and tags
 
# OpenCV trains a model from the images

model = cv2.face.LBPHFaceRecognizer_create()
model.train(photos, tags)