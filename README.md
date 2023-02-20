# Malaria Detection

Deep learning/software engineering project. Prompts user for malaria image sample. Use API call to make prediction. Tell user whether malaria is detected or not.

## Modules
* TensorFlow: Convolutional Neural Networks
* Streamlit: Front-end
* FastAPI: API call

## To train

Unzip Dataset.zip (for CPU)

Bigger dataset from [here](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria/download?datasetVersionNumber=1) for GPU.

Python needed, then run
```
    pip install -r requirements.txt
    python model.py
```
## To run

Open two terminals:

* Terminal one
```
    uvicorn api:app --reload
```
* Terminal two
```
    streamlit run app.py
```
When done with application, revert back to latest Protobuf by running:
```
    pip install --upgrade protobuf
```