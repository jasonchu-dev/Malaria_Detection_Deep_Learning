from flask import Flask, render_template, request, send_from_directory
import cv2 as cv
import numpy as np
import tensorflow as tf
import os

app = Flask(__name__)
model = tf.keras.models.load_model('model.h5')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    file = request.files['file']
    if not file: return render_template('index.html')
    path = './samples/' + file.filename
    file.save(path)

    img = cv.imread(path)
    img = cv.resize(img, (225, 225))
    img = img.reshape(1, 225, 225, 3)
    img = img/255
    nodes = model.predict(img)
    # nodes is np.array within array and cannot flatten so it must be [0][0] and [0][1] not [0] and [1]
    a = np.argmax(nodes, axis=1)
    percent, result = None, None

    if a == 0: 
        result = 'Infected'
        percent = nodes[0][0] * 100
    else: 
        result = 'Uninfected'
        percent = nodes[0][1] * 100

    imagename = os.listdir(os.getcwd() + r'\samples')[-1]

    return render_template('index.html', result=result, percent=percent, imagename=imagename)

if __name__ == '__main__':
    app.run(debug=True)