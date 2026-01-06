from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/predict")
def predict(x:float):
    return {"y": x**2}

