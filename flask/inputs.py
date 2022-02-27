import creation
import cv2
import numpy as np
from PIL import Image
import os
import recognition
import training

names = ['None']


def append_list(username):
    # user = input("\nEnter ypur name <return> ==> ")
    names.append(username)
    creation.boss_create(len(names))

def get_list():
    return names

def recognize():
    return recognition.recog(names)

def train_finally():
    return training.train_the_model()














