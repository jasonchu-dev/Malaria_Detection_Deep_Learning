# Malaria Detection

Deep learning/software engineering project. Prompts user for malaria image sample. Use API call to make prediction. Tell user whether malaria is detected or not.

## Modules
* TensorFlow: Convolutional Neural Networks
* Streamlit: Front-end
* FastAPI: API call

## To run
Python needed, then run
```
    pip install -r requirements.txt
```
Unzip model.zip

Bigger dataset from [here](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria/download?datasetVersionNumber=1) can used on hardware acceleration if there is one.

Open two terminals:
* Terminal one
```
    uvicorn api:app --reload
```
* Terminal two
```
    streamlit run app.py
```

## To train

Unzip Dataset.zip (for CPU)

Bigger dataset from [here](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria/download?datasetVersionNumber=1) for GPU.

Run model.ipynb