from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/predict")
def predict(x:float, y: float):
    return {"sum": x+y, 
            "difference": x-y,
            "product": x*y,
            "division": x/y,
            "square": x**2,
            "cube": x**3}

