# Malaria Detection

Deep learning/software engineering project. Prompts user for malaria image sample. Use API call to make prediction. Tell user whether malaria is detected or not.

## Modules
* TensorFlow: Convolutional Neural Networks
* Streamlit: Front-end
* FastAPI: Back-end, API call

## To run
Python needed, then run
```
    pip install -r requirements.txt
```
Unzip model.zip

Open two terminals:
* Terminal one
```
    uvicorn api:app --reload
```
* Terminal two
```
    streamlit run app.py
```
(protobuf 3.20.* required, once done revert back to latest protobuf)

## To train

Unzip Dataset.zip (for CPU)

Bigger dataset from [here](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria/download?datasetVersionNumber=1) for GPU.

Run model.ipynb
