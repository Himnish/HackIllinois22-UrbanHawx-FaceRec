import creation
import cv2
import numpy as np
from PIL import Image
import os
import recognition
import training

names= ['None']


def append_list():
    user = input("\nEnter ypur name <return> ==> ")
    names.append(user)
    creation.boss_create(len(names))

def get_list():
    return names

def recognize():
    recognition.recog(names)

def train_finally():
    training.train_the_model()














