import streamlit as st
import requests
import json
import os

col1, col2, col3 = st.columns(3)
result, percent, color = '', '', None

st.markdown(f"""<h1 style='text-align: center; font-size: 40px;'>
                    Malaria Detection Using Deep Learning
                </h1>""",
            unsafe_allow_html=True)

file = st.file_uploader('Upload an image', type=['jpg', 'png', 'jfif'])

if st.button('Predict'):
    if not file: 
        st.write('Please put in image')
    else:
        path = os.path.join(os.getcwd(), file.name)
        input = {'path':path}
        with open(file.name, 'wb') as f:
            f.write(file.getbuffer())
        res = requests.post(url='http://127.0.0.1:8000', data=json.dumps(input))

        os.remove(path)

        for i in res.text:
            if i in 'UNINFECTED':
                result += ''.join(i)
            elif i in '.0123456789':
                percent += ''.join(i)
        
        st.image(file, use_column_width=True)

        color = 'red' if result == 'INFECTED' else 'green'

        output = f"""<p>
                        <span style="float:left;font-size:25px;font-weight:bold;color:{color};">
                            {result}
                        </span>
                        <span style="font-size:24px;float:right;">
                            {percent}% &nbsp;&nbsp;confidence
                        </span>
                    </p>"""

        st.markdown(output, unsafe_allow_html=True)
