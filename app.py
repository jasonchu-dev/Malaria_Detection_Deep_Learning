import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

model = tf.keras.models.load_model('model.h5')

col1, col2, col3 = st.columns(3)

def predict(f):
    img = Image.open(f)
    img = ImageOps.fit(img, (225, 225), Image.ANTIALIAS)
    img = np.array(img)
    img = img[np.newaxis,...]
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

st.markdown("<h1 style='text-align:center;font-size:40px;'>Malaria Detection Using Deep Learning</h1>", unsafe_allow_html=True)

file = st.file_uploader('Upload an image', type=['jpg', 'png'])

if st.button('Predict'):
    if not file: 
        st.write('Please put in image')
    else:
        result, percent = predict(file)
        st.image(file, use_column_width=True)
        if result == 'INFECTED':
            st.markdown(f'<h1 style="color:red;font-size:24px;">INFECTED</h1>', unsafe_allow_html=True)
        else:
            st.markdown(f'<h1 style="color:green;font-size:24px;">UNINFECTED</h1>', unsafe_allow_html=True)
        st.write(f"{percent}% confidence")