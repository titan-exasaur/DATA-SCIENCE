import joblib
import numpy as np
import pandas as pd

model = joblib.load("linreg.pkl")

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to Machine Learning"}

@app.get("/predict")
def predict(x: float):
    y = model.predict([[x]])[0][0]
    return {"x": x, "y": y}