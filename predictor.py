import tensorflow as tf
import numpy as np
import cv2 as cv

model = tf.keras.models.load_model('model.h5')

def predict(path):
    img = cv.imread(path)
    img = cv.resize(img, (225, 225))
    img = img.reshape(1, 225, 225, 3)
    img = img/255

    nodes = model.predict(img)
    a = np.argmax(nodes, axis=1)
    percent, result = None, None

    if a == 0:
        result = 'INFECTED'
        percent = nodes[0][0] * 100
    else: 
        result = 'UNINFECTED'
        percent = nodes[0][1] * 100

    return result, percent