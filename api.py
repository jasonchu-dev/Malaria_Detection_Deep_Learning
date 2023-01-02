from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict

class Input(BaseModel):
    path : str

app = FastAPI()

@app.post("/")
def python_call(input:Input):
    return predict(input.path)