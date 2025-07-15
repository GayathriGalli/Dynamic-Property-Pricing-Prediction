from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

HBGR_pipeline = joblib.load('HBGR_pipeline.pkl')

class InputData(BaseModel):
    FinishedSqft : float
    Bdrms : int
    Fbath : int
    Hbath : int
    Stories : int
    Year_Built : int
    Style : str

@app.get("/home")
def homePage():
    return "Hello World"

# @app.post("/predict")
# def predict(data: InputData):
#     try:
#         # Convert the input list into a numpy array and reshape for prediction
#         input_data = np.array(data.features).reshape(1, -1)

#         # Make prediction using the pipeline
#         prediction = pipeline.predict(input_data)

#         # Return the prediction result
#         return {"prediction": prediction.tolist()}

#     except Exception as e:
#         return {"error": str(e)}