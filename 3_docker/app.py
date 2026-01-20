import joblib
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

model = joblib.load("linreg.pkl")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def ui():
    return """
    <html>
        <body>
            <h2>Linear Regression Predictor</h2>

            <form method="post">
                <label>Enter x:</label>
                <input type="number" step="any" name="x">
                <button type="submit">Predict</button>
            </form>
        </body>
    </html>
    """

@app.post("/", response_class=HTMLResponse)
def predict(x: str = Form(...)):
    if x.strip() == "":
        return """
        <html>
            <body>
                <h3 style="color:red;">Error: x cannot be empty</h3>
                <a href="/">Go back</a>
            </body>
        </html>
        """

    x_val = float(x)
    y = model.predict([[x_val]])[0][0]

    return f"""
    <html>
        <body>
            <h2>Linear Regression Predictor</h2>
            <p><b>x:</b> {x_val}</p>
            <p><b>Prediction y:</b> {y}</p>
            <a href="/">Predict again</a>
        </body>
    </html>
    """
