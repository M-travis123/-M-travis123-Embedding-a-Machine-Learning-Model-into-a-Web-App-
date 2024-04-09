from fastapi import FastAPI, HTTPException, Response
import joblib
from pydantic import BaseModel
import pandas as pd
import uvicorn

# Initialize FastAPI app
api_app = FastAPI(
    title="🩺 Sepsis Detection API",
    description="API for predicting the likelihood of sepsis development in ICU patients based on clinical indicators.",
    version="1.0",
)


# Load the pipelines and encoder
forest_pipeline = joblib.load('./models/forest_pipeline.joblib')
gradientboosting_pipeline = joblib.load('./models/GradientBoosting_pipeline.joblib')
logistic_regression_pipeline = joblib.load('./models/LogisticRegression_pipeline.joblib')
encoder = joblib.load('./models/encoder.joblib')



# Welcome endpoint
@api_app.get('/')
async def home():
    return Response("Welcome to the Sepsis Detection API! Use the /predict endpoint to make predictions.")
    
   


# Define the input data model
class PatientFeatures(BaseModel):
    Plasma_glucose: int
    Blood_Work_R1: int
    Blood_Pressure: int
    Blood_Work_R2: int
    Blood_Work_R3: int
    BMI: float
    Blood_Work_R4: float
    Patient_age: int
    Insurance: int

    # Define output response model
class PredictionResult(BaseModel):
    predicted_class: str

# Endpoint for making predictions using Random Forest
@api_app.post('/predict_random_forest')
def random_forest_prediction(data: PatientFeatures):
    # Convert input data to a DataFrame
    df = pd.DataFrame([data.model_dump()])
    
    # Make predictions using Random Forest pipeline
    prediction = forest_pipeline.predict(df)
    prediction = int(prediction[0])  # Convert prediction to an int instead of an array
    prediction = encoder.inverse_transform([prediction])[0]  # Decode using the encoder
    
    # Extract probabilities
    probabilities = forest_pipeline.predict_proba(df)
    probabilities = probabilities.tolist()  # Convert probabilities to a list
    
    return {'Prediction': prediction, 'Probabilities': probabilities}


# Endpoint for making predictions using Gradient Boosting
@api_app.post('/predict_gradient_boosting')
def gradient_boosting_prediction(data: PatientFeatures):
    # Convert input data to a DataFrame
    df = pd.DataFrame([data.model_dump()])
    
    # Make predictions using Gradient Boosting pipeline
    prediction = gradientboosting_pipeline.predict(df)
    prediction = int(prediction[0])  # Convert prediction to an int instead of an array
    prediction = encoder.inverse_transform([prediction])[0]  # Decode using the encoder
    
    # Extract probabilities
    probabilities = gradientboosting_pipeline.predict_proba(df)
    probabilities = probabilities.tolist()  # Convert probabilities to a list
    
    return {'Prediction': prediction, 'Probabilities': probabilities}


# Endpoint for making predictions using Logistic Regression
@api_app.post('/predict_logistic_regression')
def logistic_regression_prediction(data: PatientFeatures):
    # Convert input data to a DataFrame
    df = pd.DataFrame([data.model_dump()])
    
    # Make predictions using Logistic Regression pipeline
    prediction = logistic_regression_pipeline.predict(df)
    prediction = int(prediction[0])  # Convert prediction to an int instead of an array
    prediction = encoder.inverse_transform([prediction])[0]  # Decode using the encoder
    
    # Extract probabilities
    probabilities = logistic_regression_pipeline.predict_proba(df)
    probabilities = probabilities.tolist()  # Convert probabilities to a list
    
    return {'Prediction': prediction, 'Probabilities': probabilities}